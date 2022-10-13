# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainexAGwH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(56, 58, 89)")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setAutoFillBackground(False)
        self.Btn_Toggle.setStyleSheet(u"color: #FFC0CB;\n"
"border: 0px solid;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/24x24/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(100, 0))
        self.frame_left_menu.setMaximumSize(QSize(100, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        self.btn_page_1.setFont(font)
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: #FFC0CB;\n"
"	background-color: rgb(56, 58, 89);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:#6272A4;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/24x24/codesandbox.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_1.setIcon(icon1)
        self.btn_page_1.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setFont(font)
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: #FFC0CB;\n"
"	background-color: rgb(56, 58, 89);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:#6272A4;\n"
"}")
        self.btn_page_2.setIcon(icon1)
        self.btn_page_2.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setFont(font)
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: #FFC0CB;\n"
"	background-color: rgb(56, 58, 89);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:#6272A4;\n"
"}")
        self.btn_page_3.setIcon(icon1)
        self.btn_page_3.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.btn_page_3)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"background-color:rgb(34, 48, 60);	\n"
"color: rgb(220, 220, 220);")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"background-color:rgb(34, 48, 60);	\n"
"color: rgb(220, 220, 220);")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_header1 = QFrame(self.page_1)
        self.frame_header1.setObjectName(u"frame_header1")
        self.frame_header1.setMinimumSize(QSize(0, 50))
        self.frame_header1.setMaximumSize(QSize(16777215, 50))
        self.frame_header1.setBaseSize(QSize(0, 50))
        self.frame_header1.setFrameShape(QFrame.StyledPanel)
        self.frame_header1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_header1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_3 = QLabel(self.frame_header1)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color:rgb(34, 48, 60);	\n"
"color: rgb(220, 220, 220);")

        self.verticalLayout_13.addWidget(self.label_3)


        self.verticalLayout_7.addWidget(self.frame_header1)

        self.frame_body1 = QFrame(self.page_1)
        self.frame_body1.setObjectName(u"frame_body1")
        self.frame_body1.setFrameShape(QFrame.StyledPanel)
        self.frame_body1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_body1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_content1 = QFrame(self.frame_body1)
        self.frame_content1.setObjectName(u"frame_content1")
        self.frame_content1.setFrameShape(QFrame.StyledPanel)
        self.frame_content1.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_content1)

        self.frame_footer1 = QFrame(self.frame_body1)
        self.frame_footer1.setObjectName(u"frame_footer1")
        self.frame_footer1.setMinimumSize(QSize(0, 50))
        self.frame_footer1.setMaximumSize(QSize(16777215, 50))
        self.frame_footer1.setBaseSize(QSize(0, 50))
        self.frame_footer1.setFrameShape(QFrame.StyledPanel)
        self.frame_footer1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_footer1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_footer_left1 = QFrame(self.frame_footer1)
        self.frame_footer_left1.setObjectName(u"frame_footer_left1")
        self.frame_footer_left1.setFrameShape(QFrame.StyledPanel)
        self.frame_footer_left1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_footer_left1)

        self.frame_footer_right1 = QFrame(self.frame_footer1)
        self.frame_footer_right1.setObjectName(u"frame_footer_right1")
        self.frame_footer_right1.setFrameShape(QFrame.StyledPanel)
        self.frame_footer_right1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_footer_right1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_upload1 = QPushButton(self.frame_footer_right1)
        self.btn_upload1.setObjectName(u"btn_upload1")
        self.btn_upload1.setMinimumSize(QSize(0, 40))
        self.btn_upload1.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_6.addWidget(self.btn_upload1)

        self.btn_generate1 = QPushButton(self.frame_footer_right1)
        self.btn_generate1.setObjectName(u"btn_generate1")
        self.btn_generate1.setMinimumSize(QSize(0, 40))
        self.btn_generate1.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_6.addWidget(self.btn_generate1)


        self.horizontalLayout_5.addWidget(self.frame_footer_right1)


        self.verticalLayout_10.addWidget(self.frame_footer1)


        self.verticalLayout_7.addWidget(self.frame_body1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color:rgb(34, 48, 60);	\n"
"color: rgb(220, 220, 220);")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_head2 = QFrame(self.page_2)
        self.frame_head2.setObjectName(u"frame_head2")
        self.frame_head2.setMinimumSize(QSize(0, 50))
        self.frame_head2.setMaximumSize(QSize(16777215, 50))
        self.frame_head2.setBaseSize(QSize(50, 0))
        self.frame_head2.setFrameShape(QFrame.StyledPanel)
        self.frame_head2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_head2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_2 = QLabel(self.frame_head2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color:rgb(34, 48, 60);	\n"
"color: rgb(220, 220, 220);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_2)


        self.verticalLayout_6.addWidget(self.frame_head2)

        self.frame_body2 = QFrame(self.page_2)
        self.frame_body2.setObjectName(u"frame_body2")
        self.frame_body2.setFrameShape(QFrame.StyledPanel)
        self.frame_body2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_body2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_content2 = QFrame(self.frame_body2)
        self.frame_content2.setObjectName(u"frame_content2")
        self.frame_content2.setFrameShape(QFrame.StyledPanel)
        self.frame_content2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_content2)

        self.frame_footer2 = QFrame(self.frame_body2)
        self.frame_footer2.setObjectName(u"frame_footer2")
        self.frame_footer2.setMinimumSize(QSize(0, 50))
        self.frame_footer2.setMaximumSize(QSize(16777215, 50))
        self.frame_footer2.setBaseSize(QSize(0, 50))
        self.frame_footer2.setFrameShape(QFrame.StyledPanel)
        self.frame_footer2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_footer2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_footer_left2 = QFrame(self.frame_footer2)
        self.frame_footer_left2.setObjectName(u"frame_footer_left2")
        self.frame_footer_left2.setFrameShape(QFrame.StyledPanel)
        self.frame_footer_left2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_footer_left2)

        self.frame_footer_right2 = QFrame(self.frame_footer2)
        self.frame_footer_right2.setObjectName(u"frame_footer_right2")
        self.frame_footer_right2.setFrameShape(QFrame.StyledPanel)
        self.frame_footer_right2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_footer_right2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_upload2 = QPushButton(self.frame_footer_right2)
        self.btn_upload2.setObjectName(u"btn_upload2")
        self.btn_upload2.setMinimumSize(QSize(30, 40))
        self.btn_upload2.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_4.addWidget(self.btn_upload2)

        self.btn_generate2 = QPushButton(self.frame_footer_right2)
        self.btn_generate2.setObjectName(u"btn_generate2")
        self.btn_generate2.setMinimumSize(QSize(0, 40))
        self.btn_generate2.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_4.addWidget(self.btn_generate2)


        self.horizontalLayout_3.addWidget(self.frame_footer_right2)


        self.verticalLayout_9.addWidget(self.frame_footer2)


        self.verticalLayout_6.addWidget(self.frame_body2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"background-color:rgb(34, 48, 60);	\n"
"color: rgb(220, 220, 220);")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_header3 = QFrame(self.page_3)
        self.frame_header3.setObjectName(u"frame_header3")
        self.frame_header3.setMinimumSize(QSize(0, 50))
        self.frame_header3.setMaximumSize(QSize(16777215, 50))
        self.frame_header3.setBaseSize(QSize(0, 50))
        self.frame_header3.setFrameShape(QFrame.StyledPanel)
        self.frame_header3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_header3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label = QLabel(self.frame_header3)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:rgb(34, 48, 60);	\n"
"color: rgb(220, 220, 220);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label)


        self.verticalLayout_8.addWidget(self.frame_header3)

        self.frame_body3 = QFrame(self.page_3)
        self.frame_body3.setObjectName(u"frame_body3")
        self.frame_body3.setFrameShape(QFrame.StyledPanel)
        self.frame_body3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_body3)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_content3 = QFrame(self.frame_body3)
        self.frame_content3.setObjectName(u"frame_content3")
        self.frame_content3.setFrameShape(QFrame.StyledPanel)
        self.frame_content3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_content3)

        self.frame_footer3 = QFrame(self.frame_body3)
        self.frame_footer3.setObjectName(u"frame_footer3")
        self.frame_footer3.setMaximumSize(QSize(16777215, 50))
        self.frame_footer3.setFrameShape(QFrame.StyledPanel)
        self.frame_footer3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_footer3)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_footer_left3 = QFrame(self.frame_footer3)
        self.frame_footer_left3.setObjectName(u"frame_footer_left3")
        self.frame_footer_left3.setFrameShape(QFrame.StyledPanel)
        self.frame_footer_left3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_footer_left3)

        self.frame_footer_right3 = QFrame(self.frame_footer3)
        self.frame_footer_right3.setObjectName(u"frame_footer_right3")
        self.frame_footer_right3.setFrameShape(QFrame.StyledPanel)
        self.frame_footer_right3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_footer_right3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_upload3 = QPushButton(self.frame_footer_right3)
        self.btn_upload3.setObjectName(u"btn_upload3")
        self.btn_upload3.setMinimumSize(QSize(0, 40))
        self.btn_upload3.setMaximumSize(QSize(150, 16777215))
        self.btn_upload3.setBaseSize(QSize(150, 200))

        self.horizontalLayout_8.addWidget(self.btn_upload3)

        self.btn_generate3 = QPushButton(self.frame_footer_right3)
        self.btn_generate3.setObjectName(u"btn_generate3")
        self.btn_generate3.setMinimumSize(QSize(200, 40))
        self.btn_generate3.setMaximumSize(QSize(200, 16777215))
        self.btn_generate3.setBaseSize(QSize(200, 40))

        self.horizontalLayout_8.addWidget(self.btn_generate3)


        self.horizontalLayout_7.addWidget(self.frame_footer_right3)


        self.verticalLayout_12.addWidget(self.frame_footer3)


        self.verticalLayout_8.addWidget(self.frame_body3)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Algo 1", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Algo 2", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Algo 3", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Unbounded Interleaved-state Recurrent Neural Networks (UIS-RNN)", None))
        self.btn_upload1.setText(QCoreApplication.translate("MainWindow", u"Upload File", None))
        self.btn_generate1.setText(QCoreApplication.translate("MainWindow", u"Generate Transcript", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LSTM-based d-vector audio embeddings ", None))
        self.btn_upload2.setText(QCoreApplication.translate("MainWindow", u"Upload File", None))
        self.btn_generate2.setText(QCoreApplication.translate("MainWindow", u"Generate Transcript", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Variational Bayes HMM over x-vector\n"
"", None))
        self.btn_upload3.setText(QCoreApplication.translate("MainWindow", u"Upload File", None))
        self.btn_generate3.setText(QCoreApplication.translate("MainWindow", u"Generate Transcript", None))
    # retranslateUi

