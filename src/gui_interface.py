# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_with_layouts_no_groupsAngcAQ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1324, 794)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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

        self.horizontalLayout_4.setStretch(1, 9)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 429, 380))
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

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.style_layer_box_label = QLabel(self.centralwidget)
        self.style_layer_box_label.setObjectName(u"style_layer_box_label")
        self.style_layer_box_label.setTextFormat(Qt.AutoText)
        self.style_layer_box_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.style_layer_box_label)

        self.style_layer_box_2 = QScrollArea(self.centralwidget)
        self.style_layer_box_2.setObjectName(u"style_layer_box_2")
        self.style_layer_box_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.style_layer_box_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 428, 380))
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

        self.style_layer_box_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.style_layer_box_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.verticalLayout_10.setStretch(0, 20)
        self.verticalLayout_10.setStretch(1, 1)
        self.verticalLayout_10.setStretch(2, 10)

        self.horizontalLayout_9.addLayout(self.verticalLayout_10)

        self.horizontalLayout_9.setStretch(0, 3)
        self.horizontalLayout_9.setStretch(1, 7)

        self.horizontalLayout.addLayout(self.horizontalLayout_9)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.optimizer_box.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.source_in.setText(QCoreApplication.translate("MainWindow", u"*click to choose content*", None))
        self.style_in.setText(QCoreApplication.translate("MainWindow", u"*click to choose style*", None))
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
    # retranslateUi

