# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_with_layouts_no_groupsFUQquL.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from nst import *


class Ui_MainWindow(QMainWindow):
    def setupUi(self):
        if self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(1324, 794)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(800, 600))
        self.setSizeIncrement(QSize(0, 0))
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setLayoutDirection(Qt.LeftToRight)
        self.setAutoFillBackground(True)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.source_in = QPushButton(self.centralwidget)
        self.source_in.setObjectName(u"source_in")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.source_in.sizePolicy().hasHeightForWidth())
        self.source_in.setSizePolicy(sizePolicy1)
        self.source_in.setMinimumSize(QSize(224, 224))

        self.verticalLayout_4.addWidget(self.source_in)

        self.style_in = QPushButton(self.centralwidget)
        self.style_in.setObjectName(u"style_in")
        sizePolicy1.setHeightForWidth(self.style_in.sizePolicy().hasHeightForWidth())
        self.style_in.setSizePolicy(sizePolicy1)
        self.style_in.setMinimumSize(QSize(224, 224))

        self.verticalLayout_4.addWidget(self.style_in)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_8.addWidget(self.label)

        self.iterations = QSpinBox(self.centralwidget)
        self.iterations.setObjectName(u"iterations")
        self.iterations.setMinimum(1)
        self.iterations.setMaximum(10000)

        self.horizontalLayout_8.addWidget(self.iterations)

        self.horizontalLayout_8.setStretch(0, 7)
        self.horizontalLayout_8.setStretch(1, 16)

        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.optimizer_label = QLabel(self.centralwidget)
        self.optimizer_label.setObjectName(u"optimizer_label")
        self.optimizer_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.optimizer_label)

        self.optimizer_box = QComboBox(self.centralwidget)
        self.optimizer_box.addItem("")
        self.optimizer_box.addItem("")
        self.optimizer_box.addItem("")
        self.optimizer_box.addItem("")
        self.optimizer_box.addItem("")
        self.optimizer_box.addItem("")
        self.optimizer_box.addItem("")
        self.optimizer_box.addItem("")
        self.optimizer_box.setObjectName(u"optimizer_box")
        self.optimizer_box.setInsertPolicy(QComboBox.InsertAtBottom)
        self.optimizer_box.setFrame(True)

        self.horizontalLayout_6.addWidget(self.optimizer_box)

        self.horizontalLayout_6.setStretch(0, 7)
        self.horizontalLayout_6.setStretch(1, 16)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.learning_rate_label = QLabel(self.centralwidget)
        self.learning_rate_label.setObjectName(u"learning_rate_label")

        self.horizontalLayout_7.addWidget(self.learning_rate_label)

        self.learning_rate = QDoubleSpinBox(self.centralwidget)
        self.learning_rate.setObjectName(u"learning_rate")
        self.learning_rate.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.learning_rate.setKeyboardTracking(True)
        self.learning_rate.setMinimum(0.010000000000000)
        self.learning_rate.setMaximum(10.000000000000000)
        self.learning_rate.setSingleStep(0.010000000000000)

        self.horizontalLayout_7.addWidget(self.learning_rate)

        self.horizontalLayout_7.setStretch(0, 7)
        self.horizontalLayout_7.setStretch(1, 16)

        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.out_size_label = QLabel(self.centralwidget)
        self.out_size_label.setObjectName(u"out_size_label")
        self.out_size_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.out_size_label)

        self.out_width = QSpinBox(self.centralwidget)
        self.out_width.setObjectName(u"out_width")
        self.out_width.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.out_width.setMinimum(112)
        self.out_width.setMaximum(1920)

        self.horizontalLayout_3.addWidget(self.out_width)

        self.out_xsep = QLabel(self.centralwidget)
        self.out_xsep.setObjectName(u"out_xsep")
        self.out_xsep.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.out_xsep)

        self.out_height = QSpinBox(self.centralwidget)
        self.out_height.setObjectName(u"out_height")
        self.out_height.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.out_height.setMinimum(112)
        self.out_height.setMaximum(1080)

        self.horizontalLayout_3.addWidget(self.out_height)

        self.horizontalLayout_3.setStretch(0, 7)
        self.horizontalLayout_3.setStretch(1, 7)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 7)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comp_size_label = QLabel(self.centralwidget)
        self.comp_size_label.setObjectName(u"comp_size_label")
        self.comp_size_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.comp_size_label)

        self.comp_width = QSpinBox(self.centralwidget)
        self.comp_width.setObjectName(u"comp_width")
        self.comp_width.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.comp_width.setMinimum(112)
        self.comp_width.setMaximum(1920)

        self.horizontalLayout_2.addWidget(self.comp_width)

        self.comp_xsep = QLabel(self.centralwidget)
        self.comp_xsep.setObjectName(u"comp_xsep")
        self.comp_xsep.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.comp_xsep)

        self.comp_height = QSpinBox(self.centralwidget)
        self.comp_height.setObjectName(u"comp_height")
        self.comp_height.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.comp_height.setMinimum(112)
        self.comp_height.setMaximum(1080)

        self.horizontalLayout_2.addWidget(self.comp_height)

        self.horizontalLayout_2.setStretch(0, 7)
        self.horizontalLayout_2.setStretch(1, 7)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 7)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4.setStretch(0, 7)
        self.verticalLayout_4.setStretch(1, 7)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_4.setStretch(4, 1)
        self.verticalLayout_4.setStretch(5, 1)
        self.verticalLayout_4.setStretch(6, 1)

        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.output_image = QLabel(self.centralwidget)
        self.output_image.setObjectName(u"output_image")
        self.output_image.setMinimumSize(QSize(224, 224))
        font = QFont()
        font.setPointSize(12)
        self.output_image.setFont(font)
        self.output_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.output_image)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.run_button = QPushButton(self.centralwidget)
        self.run_button.setObjectName(u"run_button")

        self.horizontalLayout_4.addWidget(self.run_button)

        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setEnabled(True)
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        self.progress_bar.setFont(font1)
        self.progress_bar.setValue(30)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setInvertedAppearance(False)

        self.horizontalLayout_4.addWidget(self.progress_bar)

        self.save_to_file_button = QPushButton(self.centralwidget)
        self.save_to_file_button.setObjectName(u"save_to_file_button")
        self.save_to_file_button.setEnabled(True)
        self.save_to_file_button.setCheckable(False)
        self.save_to_file_button.setChecked(False)

        self.horizontalLayout_4.addWidget(self.save_to_file_button)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 8)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.content_layer_box_label = QLabel(self.centralwidget)
        self.content_layer_box_label.setObjectName(u"content_layer_box_label")
        self.content_layer_box_label.setTextFormat(Qt.AutoText)
        self.content_layer_box_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.content_layer_box_label)

        self.content_layer_box = QScrollArea(self.centralwidget)
        self.content_layer_box.setObjectName(u"content_layer_box")
        self.content_layer_box.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.content_layer_box.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 201, 380))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.block1_conv1_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block1_conv1_box.setObjectName(u"block1_conv1_box")

        self.verticalLayout.addWidget(self.block1_conv1_box)

        self.block1_conv2_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block1_conv2_box.setObjectName(u"block1_conv2_box")

        self.verticalLayout.addWidget(self.block1_conv2_box)

        self.block2_conv1_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block2_conv1_box.setObjectName(u"block2_conv1_box")
        self.block2_conv1_box.setChecked(False)

        self.verticalLayout.addWidget(self.block2_conv1_box)

        self.block2_conv2_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block2_conv2_box.setObjectName(u"block2_conv2_box")

        self.verticalLayout.addWidget(self.block2_conv2_box)

        self.block3_conv1_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block3_conv1_box.setObjectName(u"block3_conv1_box")

        self.verticalLayout.addWidget(self.block3_conv1_box)

        self.block3_conv2_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block3_conv2_box.setObjectName(u"block3_conv2_box")

        self.verticalLayout.addWidget(self.block3_conv2_box)

        self.block3_conv3_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block3_conv3_box.setObjectName(u"block3_conv3_box")

        self.verticalLayout.addWidget(self.block3_conv3_box)

        self.block3_conv4_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block3_conv4_box.setObjectName(u"block3_conv4_box")

        self.verticalLayout.addWidget(self.block3_conv4_box)

        self.block4_conv1_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block4_conv1_box.setObjectName(u"block4_conv1_box")

        self.verticalLayout.addWidget(self.block4_conv1_box)

        self.block4_conv2_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block4_conv2_box.setObjectName(u"block4_conv2_box")

        self.verticalLayout.addWidget(self.block4_conv2_box)

        self.block4_conv3_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block4_conv3_box.setObjectName(u"block4_conv3_box")

        self.verticalLayout.addWidget(self.block4_conv3_box)

        self.block4_conv4_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block4_conv4_box.setObjectName(u"block4_conv4_box")

        self.verticalLayout.addWidget(self.block4_conv4_box)

        self.block5_conv1_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block5_conv1_box.setObjectName(u"block5_conv1_box")

        self.verticalLayout.addWidget(self.block5_conv1_box)

        self.block5_conv2_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block5_conv2_box.setObjectName(u"block5_conv2_box")

        self.verticalLayout.addWidget(self.block5_conv2_box)

        self.block5_conv3_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block5_conv3_box.setObjectName(u"block5_conv3_box")

        self.verticalLayout.addWidget(self.block5_conv3_box)

        self.block5_conv4_box = QCheckBox(self.scrollAreaWidgetContents)
        self.block5_conv4_box.setObjectName(u"block5_conv4_box")

        self.verticalLayout.addWidget(self.block5_conv4_box)

        self.content_layer_box.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.content_layer_box)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.content_weight_box_label = QLabel(self.centralwidget)
        self.content_weight_box_label.setObjectName(u"content_weight_box_label")

        self.verticalLayout_6.addWidget(self.content_weight_box_label)

        self.content_weight_box = QScrollArea(self.centralwidget)
        self.content_weight_box.setObjectName(u"content_weight_box")
        self.content_weight_box.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.content_weight_box.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 201, 428))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.block1_conv1_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block1_conv1_label.setObjectName(u"block1_conv1_label")
        self.block1_conv1_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block1_conv1_label)

        self.block1_conv2_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block1_conv2_label.setObjectName(u"block1_conv2_label")
        self.block1_conv2_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block1_conv2_label)

        self.block2_conv1_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block2_conv1_label.setObjectName(u"block2_conv1_label")
        self.block2_conv1_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block2_conv1_label)

        self.block2_conv2_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block2_conv2_label.setObjectName(u"block2_conv2_label")
        self.block2_conv2_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block2_conv2_label)

        self.block3_conv1_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block3_conv1_label.setObjectName(u"block3_conv1_label")
        self.block3_conv1_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block3_conv1_label)

        self.block3_conv2_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block3_conv2_label.setObjectName(u"block3_conv2_label")
        self.block3_conv2_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block3_conv2_label)

        self.block3_conv3_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block3_conv3_label.setObjectName(u"block3_conv3_label")
        self.block3_conv3_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block3_conv3_label)

        self.block3_conv4_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block3_conv4_label.setObjectName(u"block3_conv4_label")
        self.block3_conv4_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block3_conv4_label)

        self.block4_conv1_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block4_conv1_label.setObjectName(u"block4_conv1_label")
        self.block4_conv1_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block4_conv1_label)

        self.block4_conv2_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block4_conv2_label.setObjectName(u"block4_conv2_label")
        self.block4_conv2_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block4_conv2_label)

        self.block4_conv3_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block4_conv3_label.setObjectName(u"block4_conv3_label")
        self.block4_conv3_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block4_conv3_label)

        self.block4_conv4_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block4_conv4_label.setObjectName(u"block4_conv4_label")
        self.block4_conv4_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block4_conv4_label)

        self.block5_conv1_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block5_conv1_label.setObjectName(u"block5_conv1_label")
        self.block5_conv1_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block5_conv1_label)

        self.block5_conv2_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block5_conv2_label.setObjectName(u"block5_conv2_label")
        self.block5_conv2_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block5_conv2_label)

        self.block5_conv3_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block5_conv3_label.setObjectName(u"block5_conv3_label")
        self.block5_conv3_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block5_conv3_label)

        self.block5_conv4_label = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.block5_conv4_label.setObjectName(u"block5_conv4_label")
        self.block5_conv4_label.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_8.addWidget(self.block5_conv4_label)

        self.content_weight_box.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_6.addWidget(self.content_weight_box)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.style_layer_box_label = QLabel(self.centralwidget)
        self.style_layer_box_label.setObjectName(u"style_layer_box_label")
        self.style_layer_box_label.setTextFormat(Qt.AutoText)
        self.style_layer_box_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.style_layer_box_label)

        self.style_layer_box = QScrollArea(self.centralwidget)
        self.style_layer_box.setObjectName(u"style_layer_box")
        self.style_layer_box.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.style_layer_box.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 200, 380))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.block1_conv1_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block1_conv1_box_2.setObjectName(u"block1_conv1_box_2")

        self.verticalLayout_2.addWidget(self.block1_conv1_box_2)

        self.block1_conv2_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block1_conv2_box_2.setObjectName(u"block1_conv2_box_2")

        self.verticalLayout_2.addWidget(self.block1_conv2_box_2)

        self.block2_conv1_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block2_conv1_box_2.setObjectName(u"block2_conv1_box_2")

        self.verticalLayout_2.addWidget(self.block2_conv1_box_2)

        self.block2_conv2_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block2_conv2_box_2.setObjectName(u"block2_conv2_box_2")

        self.verticalLayout_2.addWidget(self.block2_conv2_box_2)

        self.block3_conv1_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block3_conv1_box_2.setObjectName(u"block3_conv1_box_2")

        self.verticalLayout_2.addWidget(self.block3_conv1_box_2)

        self.block3_conv2_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block3_conv2_box_2.setObjectName(u"block3_conv2_box_2")

        self.verticalLayout_2.addWidget(self.block3_conv2_box_2)

        self.block3_conv3_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block3_conv3_box_2.setObjectName(u"block3_conv3_box_2")

        self.verticalLayout_2.addWidget(self.block3_conv3_box_2)

        self.block3_conv4_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block3_conv4_box_2.setObjectName(u"block3_conv4_box_2")

        self.verticalLayout_2.addWidget(self.block3_conv4_box_2)

        self.block4_conv1_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block4_conv1_box_2.setObjectName(u"block4_conv1_box_2")

        self.verticalLayout_2.addWidget(self.block4_conv1_box_2)

        self.block4_conv2_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block4_conv2_box_2.setObjectName(u"block4_conv2_box_2")

        self.verticalLayout_2.addWidget(self.block4_conv2_box_2)

        self.block4_conv3_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block4_conv3_box_2.setObjectName(u"block4_conv3_box_2")

        self.verticalLayout_2.addWidget(self.block4_conv3_box_2)

        self.block4_conv4_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block4_conv4_box_2.setObjectName(u"block4_conv4_box_2")

        self.verticalLayout_2.addWidget(self.block4_conv4_box_2)

        self.block5_conv1_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block5_conv1_box_2.setObjectName(u"block5_conv1_box_2")

        self.verticalLayout_2.addWidget(self.block5_conv1_box_2)

        self.block5_conv2_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block5_conv2_box_2.setObjectName(u"block5_conv2_box_2")

        self.verticalLayout_2.addWidget(self.block5_conv2_box_2)

        self.block5_conv3_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block5_conv3_box_2.setObjectName(u"block5_conv3_box_2")

        self.verticalLayout_2.addWidget(self.block5_conv3_box_2)

        self.block5_conv4_box_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.block5_conv4_box_2.setObjectName(u"block5_conv4_box_2")

        self.verticalLayout_2.addWidget(self.block5_conv4_box_2)

        self.style_layer_box.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.style_layer_box)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.style_weight_box_label = QLabel(self.centralwidget)
        self.style_weight_box_label.setObjectName(u"style_weight_box_label")

        self.verticalLayout_7.addWidget(self.style_weight_box_label)

        self.style_weight_box = QScrollArea(self.centralwidget)
        self.style_weight_box.setObjectName(u"style_weight_box")
        self.style_weight_box.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.style_weight_box.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 201, 428))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.block1_conv1_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block1_conv1_label_2.setObjectName(u"block1_conv1_label_2")
        self.block1_conv1_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block1_conv1_label_2)

        self.block1_conv2_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block1_conv2_label_2.setObjectName(u"block1_conv2_label_2")
        self.block1_conv2_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block1_conv2_label_2)

        self.block2_conv1_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block2_conv1_label_2.setObjectName(u"block2_conv1_label_2")
        self.block2_conv1_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block2_conv1_label_2)

        self.block2_conv2_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block2_conv2_label_2.setObjectName(u"block2_conv2_label_2")
        self.block2_conv2_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block2_conv2_label_2)

        self.block3_conv1_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block3_conv1_label_2.setObjectName(u"block3_conv1_label_2")
        self.block3_conv1_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block3_conv1_label_2)

        self.block3_conv2_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block3_conv2_label_2.setObjectName(u"block3_conv2_label_2")
        self.block3_conv2_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block3_conv2_label_2)

        self.block3_conv3_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block3_conv3_label_2.setObjectName(u"block3_conv3_label_2")
        self.block3_conv3_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block3_conv3_label_2)

        self.block3_conv4_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block3_conv4_label_2.setObjectName(u"block3_conv4_label_2")
        self.block3_conv4_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block3_conv4_label_2)

        self.block4_conv1_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block4_conv1_label_2.setObjectName(u"block4_conv1_label_2")
        self.block4_conv1_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block4_conv1_label_2)

        self.block4_conv2_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block4_conv2_label_2.setObjectName(u"block4_conv2_label_2")
        self.block4_conv2_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block4_conv2_label_2)

        self.block4_conv3_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block4_conv3_label_2.setObjectName(u"block4_conv3_label_2")
        self.block4_conv3_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block4_conv3_label_2)

        self.block4_conv4_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block4_conv4_label_2.setObjectName(u"block4_conv4_label_2")
        self.block4_conv4_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block4_conv4_label_2)

        self.block5_conv1_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block5_conv1_label_2.setObjectName(u"block5_conv1_label_2")
        self.block5_conv1_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block5_conv1_label_2)

        self.block5_conv2_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block5_conv2_label_2.setObjectName(u"block5_conv2_label_2")
        self.block5_conv2_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block5_conv2_label_2)

        self.block5_conv3_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block5_conv3_label_2.setObjectName(u"block5_conv3_label_2")
        self.block5_conv3_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block5_conv3_label_2)

        self.block5_conv4_label_2 = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.block5_conv4_label_2.setObjectName(u"block5_conv4_label_2")
        self.block5_conv4_label_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.verticalLayout_9.addWidget(self.block5_conv4_label_2)

        self.style_weight_box.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_7.addWidget(self.style_weight_box)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 1)
        self.horizontalLayout_5.setStretch(3, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.verticalLayout_10.setStretch(0, 20)
        self.verticalLayout_10.setStretch(1, 1)
        self.verticalLayout_10.setStretch(2, 9)

        self.horizontalLayout_9.addLayout(self.verticalLayout_10)

        self.horizontalLayout_9.setStretch(0, 3)
        self.horizontalLayout_9.setStretch(1, 7)

        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.optimizer_box.setCurrentIndex(2)
        QMetaObject.connectSlotsByName(self)

        # bind callback to stateChanged event
        self.block1_conv1_box.stateChanged.connect(self.uncheck)
        self.block1_conv2_box.stateChanged.connect(self.uncheck)
        self.block2_conv1_box.stateChanged.connect(self.uncheck)
        self.block2_conv2_box.stateChanged.connect(self.uncheck)
        self.block3_conv1_box.stateChanged.connect(self.uncheck)
        self.block3_conv2_box.stateChanged.connect(self.uncheck)
        self.block3_conv3_box.stateChanged.connect(self.uncheck)
        self.block3_conv4_box.stateChanged.connect(self.uncheck)
        self.block4_conv1_box.stateChanged.connect(self.uncheck)
        self.block4_conv2_box.stateChanged.connect(self.uncheck)
        self.block4_conv3_box.stateChanged.connect(self.uncheck)
        self.block4_conv4_box.stateChanged.connect(self.uncheck)
        self.block5_conv1_box.stateChanged.connect(self.uncheck)
        self.block5_conv2_box.stateChanged.connect(self.uncheck)
        self.block5_conv3_box.stateChanged.connect(self.uncheck)
        self.block5_conv4_box.stateChanged.connect(self.uncheck)
        self.block1_conv1_box_2.stateChanged.connect(self.uncheck)
        self.block1_conv2_box_2.stateChanged.connect(self.uncheck)
        self.block2_conv1_box_2.stateChanged.connect(self.uncheck)
        self.block2_conv2_box_2.stateChanged.connect(self.uncheck)
        self.block3_conv1_box_2.stateChanged.connect(self.uncheck)
        self.block3_conv2_box_2.stateChanged.connect(self.uncheck)
        self.block3_conv3_box_2.stateChanged.connect(self.uncheck)
        self.block3_conv4_box_2.stateChanged.connect(self.uncheck)
        self.block4_conv1_box_2.stateChanged.connect(self.uncheck)
        self.block4_conv2_box_2.stateChanged.connect(self.uncheck)
        self.block4_conv3_box_2.stateChanged.connect(self.uncheck)
        self.block4_conv4_box_2.stateChanged.connect(self.uncheck)
        self.block5_conv1_box_2.stateChanged.connect(self.uncheck)
        self.block5_conv2_box_2.stateChanged.connect(self.uncheck)
        self.block5_conv3_box_2.stateChanged.connect(self.uncheck)
        self.block5_conv4_box_2.stateChanged.connect(self.uncheck)

        # bind callback to clicked event
        self.source_in.clicked.connect(self.chooseImage)
        self.style_in.clicked.connect(self.chooseImage)

        # bind callback to scrolled event
        self.content_layer_box.verticalScrollBar().valueChanged.connect(self.syncScrollbar)
        self.style_layer_box.verticalScrollBar().valueChanged.connect(self.syncScrollbar)
        self.content_weight_box.verticalScrollBar().valueChanged.connect(self.syncScrollbar)
        self.style_weight_box.verticalScrollBar().valueChanged.connect(self.syncScrollbar)

        # bind callback to update run_button
        self.block1_conv1_box.stateChanged.connect(self.unlockRunButton)
        self.block1_conv2_box.stateChanged.connect(self.unlockRunButton)
        self.block2_conv1_box.stateChanged.connect(self.unlockRunButton)
        self.block2_conv2_box.stateChanged.connect(self.unlockRunButton)
        self.block3_conv1_box.stateChanged.connect(self.unlockRunButton)
        self.block3_conv2_box.stateChanged.connect(self.unlockRunButton)
        self.block3_conv3_box.stateChanged.connect(self.unlockRunButton)
        self.block3_conv4_box.stateChanged.connect(self.unlockRunButton)
        self.block4_conv1_box.stateChanged.connect(self.unlockRunButton)
        self.block4_conv2_box.stateChanged.connect(self.unlockRunButton)
        self.block4_conv3_box.stateChanged.connect(self.unlockRunButton)
        self.block4_conv4_box.stateChanged.connect(self.unlockRunButton)
        self.block5_conv1_box.stateChanged.connect(self.unlockRunButton)
        self.block5_conv2_box.stateChanged.connect(self.unlockRunButton)
        self.block5_conv3_box.stateChanged.connect(self.unlockRunButton)
        self.block5_conv4_box.stateChanged.connect(self.unlockRunButton)
        self.block1_conv1_box_2.stateChanged.connect(self.unlockRunButton)
        self.block1_conv2_box_2.stateChanged.connect(self.unlockRunButton)
        self.block2_conv1_box_2.stateChanged.connect(self.unlockRunButton)
        self.block2_conv2_box_2.stateChanged.connect(self.unlockRunButton)
        self.block3_conv1_box_2.stateChanged.connect(self.unlockRunButton)
        self.block3_conv2_box_2.stateChanged.connect(self.unlockRunButton)
        self.block3_conv3_box_2.stateChanged.connect(self.unlockRunButton)
        self.block3_conv4_box_2.stateChanged.connect(self.unlockRunButton)
        self.block4_conv1_box_2.stateChanged.connect(self.unlockRunButton)
        self.block4_conv2_box_2.stateChanged.connect(self.unlockRunButton)
        self.block4_conv3_box_2.stateChanged.connect(self.unlockRunButton)
        self.block4_conv4_box_2.stateChanged.connect(self.unlockRunButton)
        self.block5_conv1_box_2.stateChanged.connect(self.unlockRunButton)
        self.block5_conv2_box_2.stateChanged.connect(self.unlockRunButton)
        self.block5_conv3_box_2.stateChanged.connect(self.unlockRunButton)
        self.block5_conv4_box_2.stateChanged.connect(self.unlockRunButton)
        self.source_in.clicked.connect(self.unlockRunButton)
        self.style_in.clicked.connect(self.unlockRunButton)

        # bind callback to unlock save button once the progress bar hits 100%
        # self.progress_bar.valueChanged.connect(self.unlockSaveButton)
        self.save_to_file_button.clicked.connect(self.chooseSavePath)

        # block widgets which can't work at the start of the app
        self.run_button.setEnabled(False)
        # self.save_to_file_button.setEnabled(False)
        self.progress_bar.setEnabled(False)
        self.progress_bar.setValue(0)
        self.block1_conv1_label.setEnabled(False)
        self.block1_conv2_label.setEnabled(False)
        self.block2_conv1_label.setEnabled(False)
        self.block2_conv2_label.setEnabled(False)
        self.block3_conv1_label.setEnabled(False)
        self.block3_conv2_label.setEnabled(False)
        self.block3_conv3_label.setEnabled(False)
        self.block3_conv4_label.setEnabled(False)
        self.block4_conv1_label.setEnabled(False)
        self.block4_conv2_label.setEnabled(False)
        self.block4_conv3_label.setEnabled(False)
        self.block4_conv4_label.setEnabled(False)
        self.block5_conv1_label.setEnabled(False)
        self.block5_conv2_label.setEnabled(False)
        self.block5_conv3_label.setEnabled(False)
        self.block5_conv4_label.setEnabled(False)
        self.block1_conv1_label_2.setEnabled(False)
        self.block1_conv2_label_2.setEnabled(False)
        self.block2_conv1_label_2.setEnabled(False)
        self.block2_conv2_label_2.setEnabled(False)
        self.block3_conv1_label_2.setEnabled(False)
        self.block3_conv2_label_2.setEnabled(False)
        self.block3_conv3_label_2.setEnabled(False)
        self.block3_conv4_label_2.setEnabled(False)
        self.block4_conv1_label_2.setEnabled(False)
        self.block4_conv2_label_2.setEnabled(False)
        self.block4_conv3_label_2.setEnabled(False)
        self.block4_conv4_label_2.setEnabled(False)
        self.block5_conv1_label_2.setEnabled(False)
        self.block5_conv2_label_2.setEnabled(False)
        self.block5_conv3_label_2.setEnabled(False)
        self.block5_conv4_label_2.setEnabled(False)

        # bind run_button to nst
        self.run_button.clicked.connect(self.runNST)

        # additional flags
        self.contentImageSet = False
        self.styleImageSet = False
        self.save_path = ""
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.source_in.setText(QCoreApplication.translate("MainWindow", u"*click to choose content*", None))
        self.style_in.setText(QCoreApplication.translate("MainWindow", u"*click to choose style*", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Number of iterations:", None))
        self.optimizer_label.setText(QCoreApplication.translate("MainWindow", u"Optimizer:", None))
        self.optimizer_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Adadelta", None))
        self.optimizer_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Adagrad", None))
        self.optimizer_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Adam", None))
        self.optimizer_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Adamax", None))
        self.optimizer_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Ftrl", None))
        self.optimizer_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Nadam", None))
        self.optimizer_box.setItemText(6, QCoreApplication.translate("MainWindow", u"RMSprop", None))
        self.optimizer_box.setItemText(7, QCoreApplication.translate("MainWindow", u"SGD", None))

        self.learning_rate_label.setText(QCoreApplication.translate("MainWindow", u"Learning rate:", None))
        self.out_size_label.setText(QCoreApplication.translate("MainWindow", u"Output size:", None))
        self.out_xsep.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.comp_size_label.setText(QCoreApplication.translate("MainWindow", u"Computation size:", None))
        self.comp_xsep.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.output_image.setText(QCoreApplication.translate("MainWindow", u"output", None))
        self.run_button.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.progress_bar.setFormat(QCoreApplication.translate("MainWindow", u"completion: %p%", None))
        self.save_to_file_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.content_layer_box_label.setText(QCoreApplication.translate("MainWindow", u"Choose content layers:", None))
        self.block1_conv1_box.setText(QCoreApplication.translate("MainWindow", u"block1_conv1", None))
        self.block1_conv2_box.setText(QCoreApplication.translate("MainWindow", u"block1_conv2", None))
        self.block2_conv1_box.setText(QCoreApplication.translate("MainWindow", u"block2_conv1", None))
        self.block2_conv2_box.setText(QCoreApplication.translate("MainWindow", u"block2_conv2", None))
        self.block3_conv1_box.setText(QCoreApplication.translate("MainWindow", u"block3_conv1", None))
        self.block3_conv2_box.setText(QCoreApplication.translate("MainWindow", u"block3_conv2", None))
        self.block3_conv3_box.setText(QCoreApplication.translate("MainWindow", u"block3_conv3", None))
        self.block3_conv4_box.setText(QCoreApplication.translate("MainWindow", u"block3_conv4", None))
        self.block4_conv1_box.setText(QCoreApplication.translate("MainWindow", u"block4_conv1", None))
        self.block4_conv2_box.setText(QCoreApplication.translate("MainWindow", u"block4_conv2", None))
        self.block4_conv3_box.setText(QCoreApplication.translate("MainWindow", u"block4_conv3", None))
        self.block4_conv4_box.setText(QCoreApplication.translate("MainWindow", u"block4_conv4", None))
        self.block5_conv1_box.setText(QCoreApplication.translate("MainWindow", u"block5_conv1", None))
        self.block5_conv2_box.setText(QCoreApplication.translate("MainWindow", u"block5_conv2", None))
        self.block5_conv3_box.setText(QCoreApplication.translate("MainWindow", u"block5_conv3", None))
        self.block5_conv4_box.setText(QCoreApplication.translate("MainWindow", u"block5_conv4", None))
        self.content_weight_box_label.setText(QCoreApplication.translate("MainWindow", u"Choose content weights:", None))
        self.style_layer_box_label.setText(QCoreApplication.translate("MainWindow", u"Choose style layers:", None))
        self.block1_conv1_box_2.setText(QCoreApplication.translate("MainWindow", u"block1_conv1", None))
        self.block1_conv2_box_2.setText(QCoreApplication.translate("MainWindow", u"block1_conv2", None))
        self.block2_conv1_box_2.setText(QCoreApplication.translate("MainWindow", u"block2_conv1", None))
        self.block2_conv2_box_2.setText(QCoreApplication.translate("MainWindow", u"block2_conv2", None))
        self.block3_conv1_box_2.setText(QCoreApplication.translate("MainWindow", u"block3_conv1", None))
        self.block3_conv2_box_2.setText(QCoreApplication.translate("MainWindow", u"block3_conv2", None))
        self.block3_conv3_box_2.setText(QCoreApplication.translate("MainWindow", u"block3_conv3", None))
        self.block3_conv4_box_2.setText(QCoreApplication.translate("MainWindow", u"block3_conv4", None))
        self.block4_conv1_box_2.setText(QCoreApplication.translate("MainWindow", u"block4_conv1", None))
        self.block4_conv2_box_2.setText(QCoreApplication.translate("MainWindow", u"block4_conv2", None))
        self.block4_conv3_box_2.setText(QCoreApplication.translate("MainWindow", u"block4_conv3", None))
        self.block4_conv4_box_2.setText(QCoreApplication.translate("MainWindow", u"block4_conv4", None))
        self.block5_conv1_box_2.setText(QCoreApplication.translate("MainWindow", u"block5_conv1", None))
        self.block5_conv2_box_2.setText(QCoreApplication.translate("MainWindow", u"block5_conv2", None))
        self.block5_conv3_box_2.setText(QCoreApplication.translate("MainWindow", u"block5_conv3", None))
        self.block5_conv4_box_2.setText(QCoreApplication.translate("MainWindow", u"block5_conv4", None))
        self.style_weight_box_label.setText(QCoreApplication.translate("MainWindow", u"Choose style weights:", None))
    # retranslateUi

    # uncheck if respective another checkbox is checked
    def uncheck(self, state):
        if state == Qt.Checked:
            if self.sender() == self.block1_conv1_box:
                self.block1_conv1_box_2.setChecked(False)
                self.block1_conv1_label_2.setEnabled(False)
                self.block1_conv1_label.setEnabled(True)
            elif self.sender() == self.block1_conv2_box:
                self.block1_conv2_box_2.setChecked(False)
                self.block1_conv2_label_2.setEnabled(False)
                self.block1_conv2_label.setEnabled(True)
            elif self.sender() == self.block2_conv1_box:
                self.block2_conv1_box_2.setChecked(False)
                self.block2_conv1_label_2.setEnabled(False)
                self.block2_conv1_label.setEnabled(True)
            elif self.sender() == self.block2_conv2_box:
                self.block2_conv2_box_2.setChecked(False)
                self.block2_conv2_label_2.setEnabled(False)
                self.block2_conv2_label.setEnabled(True)
            elif self.sender() == self.block3_conv1_box:
                self.block3_conv1_box_2.setChecked(False)
                self.block3_conv1_label_2.setEnabled(False)
                self.block3_conv1_label.setEnabled(True)
            elif self.sender() == self.block3_conv2_box:
                self.block3_conv2_box_2.setChecked(False)
                self.block3_conv2_label_2.setEnabled(False)
                self.block3_conv2_label.setEnabled(True)
            elif self.sender() == self.block3_conv3_box:
                self.block3_conv3_box_2.setChecked(False)
                self.block3_conv3_label_2.setEnabled(False)
                self.block3_conv3_label.setEnabled(True)
            elif self.sender() == self.block3_conv4_box:
                self.block3_conv4_box_2.setChecked(False)
                self.block3_conv4_label_2.setEnabled(False)
                self.block3_conv4_label.setEnabled(True)
            elif self.sender() == self.block4_conv1_box:
                self.block4_conv1_box_2.setChecked(False)
                self.block4_conv1_label_2.setEnabled(False)
                self.block4_conv1_label.setEnabled(True)
            elif self.sender() == self.block4_conv2_box:
                self.block4_conv2_box_2.setChecked(False)
                self.block4_conv2_label_2.setEnabled(False)
                self.block4_conv2_label.setEnabled(True)
            elif self.sender() == self.block4_conv3_box:
                self.block4_conv3_box_2.setChecked(False)
                self.block4_conv3_label_2.setEnabled(False)
                self.block4_conv3_label.setEnabled(True)
            elif self.sender() == self.block4_conv4_box:
                self.block4_conv4_box_2.setChecked(False)
                self.block4_conv4_label_2.setEnabled(False)
                self.block4_conv4_label.setEnabled(True)
            elif self.sender() == self.block5_conv1_box:
                self.block5_conv1_box_2.setChecked(False)
                self.block5_conv1_label_2.setEnabled(False)
                self.block5_conv1_label.setEnabled(True)
            elif self.sender() == self.block5_conv2_box:
                self.block5_conv2_box_2.setChecked(False)
                self.block5_conv2_label_2.setEnabled(False)
                self.block5_conv2_label.setEnabled(True)
            elif self.sender() == self.block5_conv3_box:
                self.block5_conv3_box_2.setChecked(False)
                self.block5_conv3_label_2.setEnabled(False)
                self.block5_conv3_label.setEnabled(True)
            elif self.sender() == self.block5_conv4_box:
                self.block5_conv4_box_2.setChecked(False)
                self.block5_conv4_label_2.setEnabled(False)
                self.block5_conv4_label.setEnabled(True)
            elif self.sender() == self.block1_conv1_box_2:
                self.block1_conv1_box.setChecked(False)
                self.block1_conv1_label.setEnabled(False)
                self.block1_conv1_label_2.setEnabled(True)
            elif self.sender() == self.block1_conv2_box_2:
                self.block1_conv2_box.setChecked(False)
                self.block1_conv2_label.setEnabled(False)
                self.block1_conv2_label_2.setEnabled(True)
            elif self.sender() == self.block2_conv1_box_2:
                self.block2_conv1_box.setChecked(False)
                self.block2_conv1_label.setEnabled(False)
                self.block2_conv1_label_2.setEnabled(True)
            elif self.sender() == self.block2_conv2_box_2:
                self.block2_conv2_box.setChecked(False)
                self.block2_conv2_label.setEnabled(False)
                self.block2_conv2_label_2.setEnabled(True)
            elif self.sender() == self.block3_conv1_box_2:
                self.block3_conv1_box.setChecked(False)
                self.block3_conv1_label.setEnabled(False)
                self.block3_conv1_label_2.setEnabled(True)
            elif self.sender() == self.block3_conv2_box_2:
                self.block3_conv2_box.setChecked(False)
                self.block3_conv2_label.setEnabled(False)
                self.block3_conv2_label_2.setEnabled(True)
            elif self.sender() == self.block3_conv3_box_2:
                self.block3_conv3_box.setChecked(False)
                self.block3_conv3_label.setEnabled(False)
                self.block3_conv3_label_2.setEnabled(True)
            elif self.sender() == self.block3_conv4_box_2:
                self.block3_conv4_box.setChecked(False)
                self.block3_conv4_label.setEnabled(False)
                self.block3_conv4_label_2.setEnabled(True)
            elif self.sender() == self.block4_conv1_box_2:
                self.block4_conv1_box.setChecked(False)
                self.block4_conv1_label.setEnabled(False)
                self.block4_conv1_label_2.setEnabled(True)
            elif self.sender() == self.block4_conv2_box_2:
                self.block4_conv2_box.setChecked(False)
                self.block4_conv2_label.setEnabled(False)
                self.block4_conv2_label_2.setEnabled(True)
            elif self.sender() == self.block4_conv3_box_2:
                self.block4_conv3_box.setChecked(False)
                self.block4_conv3_label.setEnabled(False)
                self.block4_conv3_label_2.setEnabled(True)
            elif self.sender() == self.block4_conv4_box_2:
                self.block4_conv4_box.setChecked(False)
                self.block4_conv4_label.setEnabled(False)
                self.block4_conv4_label_2.setEnabled(True)
            elif self.sender() == self.block5_conv1_box_2:
                self.block5_conv1_box.setChecked(False)
                self.block5_conv1_label.setEnabled(False)
                self.block5_conv1_label_2.setEnabled(True)
            elif self.sender() == self.block5_conv2_box_2:
                self.block5_conv2_box.setChecked(False)
                self.block5_conv2_label.setEnabled(False)
                self.block5_conv2_label_2.setEnabled(True)
            elif self.sender() == self.block5_conv3_box_2:
                self.block5_conv3_box.setChecked(False)
                self.block5_conv3_label.setEnabled(False)
                self.block5_conv3_label_2.setEnabled(True)
            elif self.sender() == self.block5_conv4_box_2:
                self.block5_conv4_box.setChecked(False)
                self.block5_conv4_label.setEnabled(False)
                self.block5_conv4_label_2.setEnabled(True)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        return QFileDialog.getOpenFileName(self,"Choose an image...", "","JPG file (*.jpg);;PNG file (*.png);;Bitmap file (*.bmp)", options=options)

    # prompt the user to choose an image from file
    def chooseImage(self):
        self.sender().setText("")
        if self.sender() == self.source_in:
            self.img_content, _ = self.openFileNameDialog()
            pixmap = QPixmap(str(self.img_content))
            self.contentImageSet = True
        elif self.sender() == self.style_in:
            self.img_style, _ = self.openFileNameDialog()
            pixmap = QPixmap(str(self.img_style))
            self.styleImageSet = True
        
        icon = QIcon(pixmap)
        self.sender().setIcon(icon)
        self.sender().setIconSize(self.sender().rect().size())

    # adjust other scrollbars to current one's value
    def syncScrollbar(self, value):
        # the range is different so we need to normalize
        sb = self.sender()
        rang = sb.maximum() - sb.minimum()
        percent = value / rang

        slb = self.style_layer_box.verticalScrollBar()
        cwb = self.content_weight_box.verticalScrollBar()
        swb = self.style_weight_box.verticalScrollBar()
        clb = self.content_layer_box.verticalScrollBar()

        sb.blockSignals(True) # dodging infinite recursion
        slb.setValue(percent * (slb.maximum() - slb.minimum()))
        cwb.setValue(percent * (cwb.maximum() - cwb.minimum()))
        swb.setValue(percent * (swb.maximum() - swb.minimum()))
        clb.setValue(percent * (clb.maximum() - clb.minimum()))
        sb.blockSignals(False)

    def isAnyLayerChecked(self):
        return ((
            self.block1_conv1_box.isChecked() or
            self.block1_conv2_box.isChecked() or
            self.block2_conv1_box.isChecked() or
            self.block2_conv2_box.isChecked() or
            self.block3_conv1_box.isChecked() or
            self.block3_conv2_box.isChecked() or
            self.block3_conv3_box.isChecked() or
            self.block3_conv4_box.isChecked() or
            self.block4_conv1_box.isChecked() or
            self.block4_conv2_box.isChecked() or
            self.block4_conv3_box.isChecked() or
            self.block4_conv4_box.isChecked() or
            self.block5_conv1_box.isChecked() or
            self.block5_conv2_box.isChecked() or
            self.block5_conv3_box.isChecked() or
            self.block5_conv4_box.isChecked()) and
            (self.block1_conv1_box_2.isChecked() or
            self.block1_conv2_box_2.isChecked() or
            self.block2_conv1_box_2.isChecked() or
            self.block2_conv2_box_2.isChecked() or
            self.block3_conv1_box_2.isChecked() or
            self.block3_conv2_box_2.isChecked() or
            self.block3_conv3_box_2.isChecked() or
            self.block3_conv4_box_2.isChecked() or
            self.block4_conv1_box_2.isChecked() or
            self.block4_conv2_box_2.isChecked() or
            self.block4_conv3_box_2.isChecked() or
            self.block4_conv4_box_2.isChecked() or
            self.block5_conv1_box_2.isChecked() or
            self.block5_conv2_box_2.isChecked() or
            self.block5_conv3_box_2.isChecked() or
            self.block5_conv4_box_2.isChecked()))

    def areBothImagesSet(self):
        return self.contentImageSet and self.styleImageSet

    def unlockRunButton(self):
        self.run_button.setEnabled(self.isAnyLayerChecked() and self.areBothImagesSet())

    def chooseSavePath(self):
        options = QFileDialog.Options()
        self.save_path = QFileDialog.getExistingDirectory(self, "Choose a path...", options=options)
        if self.save_path != "":
            url = self.save_path + "/generated.jpg"
            last_dir =  ".../"+url.split('/')[-2]
        else:
            url = "generated.jpg"
            last_dir = "./"
        self.save_to_file_button.setText(last_dir)
    
    def getStyleLayers(self):
        result = []
        if self.block1_conv1_box_2.isChecked():
            result.append("block1_conv1")
        elif self.block1_conv2_box_2.isChecked():
            result.append("block1_conv2")
        elif self.block2_conv1_box_2.isChecked():
            result.append("block2_conv1")
        elif self.block2_conv2_box_2.isChecked():
            result.append("block2_conv2")
        elif self.block3_conv1_box_2.isChecked():
            result.append("block3_conv1")
        elif self.block3_conv2_box_2.isChecked():
            result.append("block3_conv2")
        elif self.block3_conv3_box_2.isChecked():
            result.append("block3_conv3")
        elif self.block3_conv4_box_2.isChecked():
            result.append("block3_conv4")
        elif self.block4_conv1_box_2.isChecked():
            result.append("block4_conv1")
        elif self.block4_conv2_box_2.isChecked():
            result.append("block4_conv2")
        elif self.block4_conv3_box_2.isChecked():
            result.append("block4_conv3")
        elif self.block4_conv4_box_2.isChecked():
            result.append("block4_conv4")
        elif self.block5_conv1_box_2.isChecked():
            result.append("block5_conv1")
        elif self.block5_conv2_box_2.isChecked():
            result.append("block5_conv2")
        elif self.block5_conv3_box_2.isChecked():
            result.append("block5_conv3")
        elif self.block5_conv4_box_2.isChecked():
            result.append("block5_conv4")
        return result

    def getContentLayers(self):
        result = []
        if self.block1_conv1_box.isChecked():
            result.append("block1_conv1")
        elif self.block1_conv2_box.isChecked():
            result.append("block1_conv2")
        elif self.block2_conv1_box.isChecked():
            result.append("block2_conv1")
        elif self.block2_conv2_box.isChecked():
            result.append("block2_conv2")
        elif self.block3_conv1_box.isChecked():
            result.append("block3_conv1")
        elif self.block3_conv2_box.isChecked():
            result.append("block3_conv2")
        elif self.block3_conv3_box.isChecked():
            result.append("block3_conv3")
        elif self.block3_conv4_box.isChecked():
            result.append("block3_conv4")
        elif self.block4_conv1_box.isChecked():
            result.append("block4_conv1")
        elif self.block4_conv2_box.isChecked():
            result.append("block4_conv2")
        elif self.block4_conv3_box.isChecked():
            result.append("block4_conv3")
        elif self.block4_conv4_box.isChecked():
            result.append("block4_conv4")
        elif self.block5_conv1_box.isChecked():
            result.append("block5_conv1")
        elif self.block5_conv2_box.isChecked():
            result.append("block5_conv2")
        elif self.block5_conv3_box.isChecked():
            result.append("block5_conv3")
        elif self.block5_conv4_box.isChecked():
            result.append("block5_conv4")
        return result

    def getStyleWeights(self):
        result = []
        if self.block1_conv1_box_2.isChecked():
            result.append(self.block1_conv1_label_2.value())
        elif self.block1_conv2_box_2.isChecked():
            result.append(self.block1_conv2_label_2.value())
        elif self.block2_conv1_box_2.isChecked():
            result.append(self.block2_conv1_label_2.value())
        elif self.block2_conv2_box_2.isChecked():
            result.append(self.block2_conv2_label_2.value())
        elif self.block3_conv1_box_2.isChecked():
            result.append(self.block3_conv1_label_2.value())
        elif self.block3_conv2_box_2.isChecked():
            result.append(self.block3_conv2_label_2.value())
        elif self.block3_conv3_box_2.isChecked():
            result.append(self.block3_conv3_label_2.value())
        elif self.block3_conv4_box_2.isChecked():
            result.append(self.block3_conv4_label_2.value())
        elif self.block4_conv1_box_2.isChecked():
            result.append(self.block4_conv1_label_2.value())
        elif self.block4_conv2_box_2.isChecked():
            result.append(self.block4_conv2_label_2.value())
        elif self.block4_conv3_box_2.isChecked():
            result.append(self.block4_conv3_label_2.value())
        elif self.block4_conv4_box_2.isChecked():
            result.append(self.block4_conv4_label_2.value())
        elif self.block5_conv1_box_2.isChecked():
            result.append(self.block5_conv1_label_2.value())
        elif self.block5_conv2_box_2.isChecked():
            result.append(self.block5_conv2_label_2.value())
        elif self.block5_conv3_box_2.isChecked():
            result.append(self.block5_conv3_label_2.value())
        elif self.block5_conv4_box_2.isChecked():
            result.append(self.block5_conv4_label_2.value())
        return result

    def getContentWeights(self):
        result = []
        if self.block1_conv1_box.isChecked():
            result.append(self.block1_conv1_label.value())
        elif self.block1_conv2_box.isChecked():
            result.append(self.block1_conv2_label.value())
        elif self.block2_conv1_box.isChecked():
            result.append(self.block2_conv1_label.value())
        elif self.block2_conv2_box.isChecked():
            result.append(self.block2_conv2_label.value())
        elif self.block3_conv1_box.isChecked():
            result.append(self.block3_conv1_label.value())
        elif self.block3_conv2_box.isChecked():
            result.append(self.block3_conv2_label.value())
        elif self.block3_conv3_box.isChecked():
            result.append(self.block3_conv3_label.value())
        elif self.block3_conv4_box.isChecked():
            result.append(self.block3_conv4_label.value())
        elif self.block4_conv1_box.isChecked():
            result.append(self.block4_conv1_label.value())
        elif self.block4_conv2_box.isChecked():
            result.append(self.block4_conv2_label.value())
        elif self.block4_conv3_box.isChecked():
            result.append(self.block4_conv3_label.value())
        elif self.block4_conv4_box.isChecked():
            result.append(self.block4_conv4_label.value())
        elif self.block5_conv1_box.isChecked():
            result.append(self.block5_conv1_label.value())
        elif self.block5_conv2_box.isChecked():
            result.append(self.block5_conv2_label.value())
        elif self.block5_conv3_box.isChecked():
            result.append(self.block5_conv3_label.value())
        elif self.block5_conv4_box.isChecked():
            result.append(self.block5_conv4_label.value())
        return result

    def getOptimizerName(self):
        return self.optimizer_box.currentText()

    def getOptimizer(self):
        if self.getOptimizerName() == "Adam":
            return tf.optimizers.Adam(learning_rate = self.getLearningRate())
        elif self.getOptimizerName() == "Adadelta":
            return tf.optimizers.Adadelta(learning_rate = self.getLearningRate())
        elif self.getOptimizerName() == "Adagrad":
            return tf.optimizers.Adagrad(learning_rate = self.getLearningRate())
        elif self.getOptimizerName() == "Adamax":
            return tf.optimizers.Adamax(learning_rate = self.getLearningRate())
        elif self.getOptimizerName() == "Ftrl":
            return tf.optimizers.Ftrl(learning_rate = self.getLearningRate())
        elif self.getOptimizerName() == "Nadam":
            return tf.optimizers.Nadam(learning_rate = self.getLearningRate())
        elif self.getOptimizerName() == "RMSprop":
            return tf.optimizers.RMSprop(learning_rate = self.getLearningRate())
        elif self.getOptimizerName() == "SGD":
            return tf.optimizers.SGD(learning_rate = self.getLearningRate())

    def getStyleImagePath(self):
        return str(self.img_style)

    def getContentImagePath(self):
        return str(self.img_content)

    def getIterationCount(self):
        return self.iterations.value()

    def getOutputSize(self):
        return [self.out_width.value(), self.out_height.value()]

    def getComputationSize(self):
        return [self.comp_width.value(), self.comp_height.value()]

    def getLearningRate(self):
        return self.learning_rate.value()

    def runNST(self):
        self.progress_bar.setEnabled(True)
        if self.save_path != "":
            url = self.save_path + "/generated.jpg"
        else:
            url = "generated.jpg"
        neural_style_transfer(
            self.progress_bar,
            self.getStyleLayers(),
            self.getStyleWeights(),
            self.getContentLayers(),
            self.getContentWeights(),
            69,
            self.getOptimizer(),
            self.getStyleImagePath(),
            self.getContentImagePath(),
            url,
            0.5,
            self.getIterationCount(),
            self.getOutputSize(),
            self.getComputationSize())
        self.output_image.setText("")
        self.output_pixmap = QPixmap(url)
        self.output_image.setPixmap(self.output_pixmap.scaled(self.output_image.size(), aspectRatioMode = Qt.KeepAspectRatio))
