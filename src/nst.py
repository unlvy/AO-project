from tensorflow import keras
from PIL import Image
import numpy as np
import tensorflow as tf

#################### image processing utilities ####################

def load_image(image_path, computation_size):
    """ 
    Loads and resizes image
    
    Args:
        param1: path to image
        param2: size as [width, height]
    
    Returns: 
        resized image
    """
    return keras.preprocessing.image.load_img(image_path, target_size = computation_size)
    
    
def preprocess_image(image):
    """
    Converts image to NumPy array, preprocessing 
    it through net (vgg19) and returning it as tensor
    
    Args:
        param1: image
        
    Returns:
        preprocessed image stored in tensor
    """
    image = keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis = 0)
    image = keras.applications.vgg19.preprocess_input(image)
    return tf.convert_to_tensor(image, dtype = tf.float32)

def init_result_image(base_image, noise_ratio):
    """
    Initializes result image by combining base
    image and noise * noise ratio, returning result as tensor
    
    Args:
        param1: base image
        param2: noise ratio
    
    Returns:
        initialized result image as tensor
    """
    image = keras.preprocessing.image.img_to_array(base_image)
    noise_image = 80 * np.random.rand(image.shape[0], image.shape[1], image.shape[2]) - 40
    image = noise_image * noise_ratio + image * (1 - noise_ratio)
    image = np.clip(image, 0, 255)
    image = np.expand_dims(image, axis = 0)
    image =  keras.applications.vgg19.preprocess_input(image)
    return tf.convert_to_tensor(image, dtype = tf.float32)    


def save_image(image_path, image_tensor, image_size):
    """
    Reizes ans saves image
    
    Args:
        param1: path to file
        param2: image as a tensor
        param3: new size of image as [w, h]  
    """
    image = image_tensor.numpy()
    # Remove zero-center by mean pixel
    # https://github.com/keras-team/keras-applications/blob/master/keras_applications/imagenet_utils.py
    image[:, :, 0] += 103.939
    image[:, :, 1] += 116.779
    image[:, :, 2] += 123.68
    # BGR -> RGB
    image = image[:, :, :: -1]
    image = np.clip(image, 0, 255).astype('uint8')
    image = keras.utils.array_to_img(image);
    image = image.resize(image_size)
    image.save(image_path);

#################### loss calculation ####################

def gram_matrix(input_tensor):
    """
    Calculates gram matrix of an image tensor
    
    Args:
        param1: image tensor
        
    Returns:
        gram matrix
    """
    result = tf.linalg.einsum('bijc,bijd->bcd', input_tensor, input_tensor)
    input_shape = tf.shape(input_tensor)
    n = tf.cast(input_shape[1] * input_shape[2], tf.float32)
    return result / (n)

def style_loss(style_features, result_features, style_weights):
    """
    Calculates style loss
    
    Args:
        param1: style features extracted by net from style image
        param2: result features extracted by net from result image
        param3: style weights for net layers
    """
    result = 0
    for i in range(len(style_features)):
        S = gram_matrix(style_features[i])
        R = gram_matrix(result_features[i])
        result += style_weights[i] * tf.reduce_mean((S - R) ** 2)
    return result

def content_loss(content_features, result_features, content_weights):
    """
    Calculates content loss
    
    Args:
        param1: content features extracted by net from content image
        param2: content features extracted by net from result image
        param3: content weights for net layers
    """
    result = 0
    for i in range(len(content_features)):
        result += content_weights[i] * tf.reduce_mean(
            (content_features[i] - result_features[i]) ** 2
        )
    return result

#################### model extracting style and content ####################

class NSTModel(keras.models.Model):
    """
    Class representing nst model
    """
    def __init__(self, style_layers, content_layers):
        """
        Constructor preparing model
        
        Args:
            param1: names of style layers
            param2: names of content layers
        """
        super().__init__()
        vgg = keras.applications.VGG19(include_top = False, weights = 'imagenet')
        vgg.trainable = False
        self.model = keras.Model(
            [vgg.input], 
            [vgg.get_layer(layer_name).output 
                for layer_name in (style_layers + content_layers)]
        )
        self.model.trainable = False
        
    def call(self, inputs):
        """
        Extracts image features by forwarding image
        tensor through net
        
        Args:
            param1: input tensor
        """
        return self.model(inputs)
    
#################### neural style transfer algorithm ####################
        
def neural_style_transfer(
    style_layers, 
    style_weights, 
    content_layers, 
    content_weights,
    total_variation_loss_weight,
    optimizer,
    style_image_path,
    content_image_path,
    result_image_path,
    noise_ratio,
    iterations,
    result_size = (224, 224),
    computation_size = (224, 224)
):
    """
    Implementation of NST algorithm
    
    Args:
        param1: names of style layers
        param2: style weights
        param3: names of content layers
        param4: content weights
        param5: total variation loss weight
        param6: optimizer
        param7: path to style image
        param8: path to content image
        param9: path to filr where result will be saved
        param10: noise ratio
        param11: number of iterations
        param12: size of result image
        param13: size of computated tensor 
                 WARNING! changing this property 
                 affects performance drastically
    """
    # load and preprocess style and content images
    style_image = load_image(style_image_path, computation_size)
    content_image = load_image(content_image_path, computation_size)
    
    result_tensor = tf.Variable(init_result_image(content_image, noise_ratio))
    style_tensor = preprocess_image(style_image)
    content_tensor = preprocess_image(content_image)
    
    # create model extracting style and content from image tensors
    model = NSTModel(style_layers, content_layers)
    
    # number of style layers
    n = len(style_layers)
    
    @tf.function
    def train_step():
        with tf.GradientTape() as tape:
            style_features = model(style_tensor)[:n]
            content_features = model(content_tensor)[n:]
            result_features = model(result_tensor)
            # calculate loss
            loss = 0
            loss += style_loss(style_features, result_features[:n], style_weights)
            loss += content_loss(content_features, result_features[n:], content_weights)
            # total variation loss, measure of noise in the image 
            loss += tf.image.total_variation(result_tensor) * total_variation_loss_weight
        grad = tape.gradient(loss, result_tensor)
        # update result
        optimizer.apply_gradients([(grad, result_tensor)])
        
    for i in range(iterations):
        train_step() 
    # save result
    # 4D -> 3D
    result_tensor = tf.reshape(result_tensor, [computation_size[0], computation_size[1], 3])
    save_image(result_image_path, result_tensor, result_size)
