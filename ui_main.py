# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainovvmid.ui'
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
        self.stackedWidget.setStyleSheet(u"background-color:rgb(136, 153, 166);	\n"
"color: rgb(220, 220, 220);")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"background-color:rgb(136, 153, 166);	\n"
"color: rgb(220, 220, 220);")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_1 = QLabel(self.page_1)
        self.label_1.setObjectName(u"label_1")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"background-color:rgb(34, 48, 60);	\n"
"color: rgb(220, 220, 220);")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color:rgb(34, 48, 60);	\n"
"color: rgb(220, 220, 220);")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color:rgb(34, 48, 60);	\n"
"color: rgb(220, 220, 220);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"background-color:rgb(34, 48, 60);	\n"
"color: rgb(220, 220, 220);")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:rgb(34, 48, 60);	\n"
"color: rgb(220, 220, 220);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

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
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Unbounded Interleaved-state Recurrent Neural Networks (UIS-RNN)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LSTM-based d-vector audio embeddings ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Variational Bayes HMM over x-vector\n"
"", None))
    # retranslateUi

