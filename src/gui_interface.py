# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_with_layouts_no_groupsgaHWMC.ui'
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
        MainWindow.resize(800, 636)
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
        self.btn_src_in = QPushButton(self.centralwidget)
        self.btn_src_in.setObjectName(u"btn_src_in")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_src_in.sizePolicy().hasHeightForWidth())
        self.btn_src_in.setSizePolicy(sizePolicy1)
        self.btn_src_in.setMinimumSize(QSize(224, 224))

        self.verticalLayout_4.addWidget(self.btn_src_in)

        self.btn_stl_in = QPushButton(self.centralwidget)
        self.btn_stl_in.setObjectName(u"btn_stl_in")
        sizePolicy1.setHeightForWidth(self.btn_stl_in.sizePolicy().hasHeightForWidth())
        self.btn_stl_in.setSizePolicy(sizePolicy1)
        self.btn_stl_in.setMinimumSize(QSize(224, 224))

        self.verticalLayout_4.addWidget(self.btn_stl_in)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.out_size_label = QLabel(self.centralwidget)
        self.out_size_label.setObjectName(u"out_size_label")
        self.out_size_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.out_size_label)

        self.out_width = QLineEdit(self.centralwidget)
        self.out_width.setObjectName(u"out_width")
        self.out_width.setFrame(True)
        self.out_width.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.out_width)

        self.out_xsep = QLabel(self.centralwidget)
        self.out_xsep.setObjectName(u"out_xsep")
        self.out_xsep.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.out_xsep)

        self.out_height = QLineEdit(self.centralwidget)
        self.out_height.setObjectName(u"out_height")
        self.out_height.setFrame(True)
        self.out_height.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.out_height)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comp_size_label = QLabel(self.centralwidget)
        self.comp_size_label.setObjectName(u"comp_size_label")
        self.comp_size_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.comp_size_label)

        self.comp_width = QLineEdit(self.centralwidget)
        self.comp_width.setObjectName(u"comp_width")
        self.comp_width.setFrame(True)
        self.comp_width.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.comp_width)

        self.comp_xsep = QLabel(self.centralwidget)
        self.comp_xsep.setObjectName(u"comp_xsep")
        self.comp_xsep.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.comp_xsep)

        self.comp_height = QLineEdit(self.centralwidget)
        self.comp_height.setObjectName(u"comp_height")
        self.comp_height.setFrame(True)
        self.comp_height.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.comp_height)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4.setStretch(0, 7)
        self.verticalLayout_4.setStretch(1, 7)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 1)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 221, 380))
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 220, 380))
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

        self.horizontalLayout_9.setStretch(0, 4)
        self.horizontalLayout_9.setStretch(1, 7)

        self.horizontalLayout.addLayout(self.horizontalLayout_9)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_src_in.setText(QCoreApplication.translate("MainWindow", u"*click to choose content*", None))
        self.btn_stl_in.setText(QCoreApplication.translate("MainWindow", u"*click to choose style*", None))
        self.out_size_label.setText(QCoreApplication.translate("MainWindow", u"Output size:", None))
        self.out_width.setText("")
        self.out_width.setPlaceholderText(QCoreApplication.translate("MainWindow", u"width", None))
        self.out_xsep.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.out_height.setText("")
        self.out_height.setPlaceholderText(QCoreApplication.translate("MainWindow", u"height", None))
        self.comp_size_label.setText(QCoreApplication.translate("MainWindow", u"Computation size:", None))
        self.comp_width.setText("")
        self.comp_width.setPlaceholderText(QCoreApplication.translate("MainWindow", u"width", None))
        self.comp_xsep.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.comp_height.setText("")
        self.comp_height.setPlaceholderText(QCoreApplication.translate("MainWindow", u"height", None))
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

