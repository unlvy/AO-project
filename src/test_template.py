import nst
import time

# layers from which style will be extracted
style_layers = []

# responding weights
style_weights = []

# layers from which content will be extracted
content_layers = []

# responding weights
content_weights = []

# total variation loss weight (removing noise from image)
total_variation_loss_weight = 

# optimizer, function/algorithm to minimize losses
optimizer = 

# path to style image
style_image_path = 

# path to content image
content_image_path = 

# path to result image
result_image_path = 

# nosie ratio <0, 1>
# result image is initialized with
# content image + noise * nosie_ratio
noise_ratio = 

# number of iterations
iterations = 

# image is resized to this size before processing it through net
# default = [224, 224]
computation_size = [ , ]

# result image size
result_size = [ , ]

# # # # # # # # # # # # # # # # # # # # # # # # # # # #

start = time.time()

nst.neural_style_transfer(
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
    result_size,
    computation_size
)

end = time.time()

print('Elapsed time:')
print(end - start)
print('Average step time:')
print((end - start) / iterations)
