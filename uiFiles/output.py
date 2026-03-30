# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prototype3.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QListView, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(970, 755)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(600, 480))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.forStretchVerticalLayout = QVBoxLayout()
        self.forStretchVerticalLayout.setObjectName(u"forStretchVerticalLayout")
        self.MainPages = QStackedWidget(Form)
        self.MainPages.setObjectName(u"MainPages")
        sizePolicy.setHeightForWidth(self.MainPages.sizePolicy().hasHeightForWidth())
        self.MainPages.setSizePolicy(sizePolicy)
        self.pageLogin = QWidget()
        self.pageLogin.setObjectName(u"pageLogin")
        sizePolicy.setHeightForWidth(self.pageLogin.sizePolicy().hasHeightForWidth())
        self.pageLogin.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.pageLogin)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.VLLogin = QVBoxLayout()
        self.VLLogin.setSpacing(0)
        self.VLLogin.setObjectName(u"VLLogin")
        self.VLLogin.setContentsMargins(-1, 0, -1, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLLogin.addItem(self.verticalSpacer_6)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_28 = QSpacerItem(80, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_28)

        self.label_2 = QLabel(self.pageLogin)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout_23.addWidget(self.label_2)

        self.horizontalSpacer_29 = QSpacerItem(80, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_29)


        self.VLLogin.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_22.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_27 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_27)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_9 = QLabel(self.pageLogin)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_9.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_9)

        self.loginUsername = QTextEdit(self.pageLogin)
        self.loginUsername.setObjectName(u"loginUsername")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.loginUsername.sizePolicy().hasHeightForWidth())
        self.loginUsername.setSizePolicy(sizePolicy2)
        self.loginUsername.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_13.addWidget(self.loginUsername)


        self.horizontalLayout_22.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_26 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_26)


        self.VLLogin.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_7 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_10 = QLabel(self.pageLogin)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setMaximumSize(QSize(16777215, 60))
        self.label_10.setFont(font1)

        self.verticalLayout_14.addWidget(self.label_10)

        self.loginPassword = QTextEdit(self.pageLogin)
        self.loginPassword.setObjectName(u"loginPassword")
        sizePolicy2.setHeightForWidth(self.loginPassword.sizePolicy().hasHeightForWidth())
        self.loginPassword.setSizePolicy(sizePolicy2)
        self.loginPassword.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_14.addWidget(self.loginPassword)


        self.horizontalLayout_3.addLayout(self.verticalLayout_14)

        self.horizontalSpacer_6 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.VLLogin.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLLogin.addItem(self.verticalSpacer_10)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 10, -1, 10)
        self.horizontalSpacer_30 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_30)

        self.loginRegisterBtn = QPushButton(self.pageLogin)
        self.loginRegisterBtn.setObjectName(u"loginRegisterBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.loginRegisterBtn.sizePolicy().hasHeightForWidth())
        self.loginRegisterBtn.setSizePolicy(sizePolicy4)
        self.loginRegisterBtn.setMaximumSize(QSize(16777215, 80))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.loginRegisterBtn.setFont(font2)

        self.horizontalLayout_18.addWidget(self.loginRegisterBtn)

        self.horizontalSpacer_31 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_31)

        self.loginConfirmBtn = QPushButton(self.pageLogin)
        self.loginConfirmBtn.setObjectName(u"loginConfirmBtn")
        sizePolicy4.setHeightForWidth(self.loginConfirmBtn.sizePolicy().hasHeightForWidth())
        self.loginConfirmBtn.setSizePolicy(sizePolicy4)
        self.loginConfirmBtn.setMaximumSize(QSize(16777215, 80))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.loginConfirmBtn.setFont(font3)

        self.horizontalLayout_18.addWidget(self.loginConfirmBtn)

        self.horizontalSpacer_21 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_21)


        self.VLLogin.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_5 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLLogin.addItem(self.verticalSpacer_5)


        self.verticalLayout_6.addLayout(self.VLLogin)

        self.MainPages.addWidget(self.pageLogin)
        self.pageRegister = QWidget()
        self.pageRegister.setObjectName(u"pageRegister")
        sizePolicy.setHeightForWidth(self.pageRegister.sizePolicy().hasHeightForWidth())
        self.pageRegister.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.pageRegister)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.VLRegister = QVBoxLayout()
        self.VLRegister.setSpacing(0)
        self.VLRegister.setObjectName(u"VLRegister")
        self.VLRegister.setContentsMargins(-1, 0, -1, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLRegister.addItem(self.verticalSpacer_7)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_33)

        self.label_3 = QLabel(self.pageRegister)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font)

        self.horizontalLayout_31.addWidget(self.label_3)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_34)


        self.VLRegister.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 5, -1, -1)
        self.horizontalSpacer_32 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_32)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_11 = QLabel(self.pageRegister)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 60))
        self.label_11.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_11)

        self.registerUsername = QTextEdit(self.pageRegister)
        self.registerUsername.setObjectName(u"registerUsername")
        sizePolicy2.setHeightForWidth(self.registerUsername.sizePolicy().hasHeightForWidth())
        self.registerUsername.setSizePolicy(sizePolicy2)
        self.registerUsername.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_15.addWidget(self.registerUsername)


        self.horizontalLayout_30.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_36 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_36)


        self.VLRegister.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_35.setContentsMargins(-1, 5, -1, -1)
        self.horizontalSpacer_51 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_51)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_17 = QLabel(self.pageRegister)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 60))
        self.label_17.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_17)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_23)

        self.label_14 = QLabel(self.pageRegister)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 60))
        self.label_14.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_14)


        self.verticalLayout_16.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.registerPhoneNumber = QTextEdit(self.pageRegister)
        self.registerPhoneNumber.setObjectName(u"registerPhoneNumber")
        sizePolicy2.setHeightForWidth(self.registerPhoneNumber.sizePolicy().hasHeightForWidth())
        self.registerPhoneNumber.setSizePolicy(sizePolicy2)
        self.registerPhoneNumber.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_19.addWidget(self.registerPhoneNumber)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_24)

        self.registerGmail = QTextEdit(self.pageRegister)
        self.registerGmail.setObjectName(u"registerGmail")
        sizePolicy2.setHeightForWidth(self.registerGmail.sizePolicy().hasHeightForWidth())
        self.registerGmail.setSizePolicy(sizePolicy2)
        self.registerGmail.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_19.addWidget(self.registerGmail)


        self.verticalLayout_16.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_35.addLayout(self.verticalLayout_16)

        self.horizontalSpacer_54 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_54)


        self.VLRegister.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(-1, 5, -1, -1)
        self.horizontalSpacer_37 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_37)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_12 = QLabel(self.pageRegister)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 60))
        self.label_12.setFont(font1)

        self.verticalLayout_17.addWidget(self.label_12)

        self.registerPassword = QTextEdit(self.pageRegister)
        self.registerPassword.setObjectName(u"registerPassword")
        sizePolicy2.setHeightForWidth(self.registerPassword.sizePolicy().hasHeightForWidth())
        self.registerPassword.setSizePolicy(sizePolicy2)
        self.registerPassword.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_17.addWidget(self.registerPassword)


        self.horizontalLayout_28.addLayout(self.verticalLayout_17)

        self.horizontalSpacer_38 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_38)


        self.VLRegister.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 5, -1, -1)
        self.horizontalSpacer_44 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_44)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_13 = QLabel(self.pageRegister)
        self.label_13.setObjectName(u"label_13")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy5)
        self.label_13.setMaximumSize(QSize(16777215, 60))
        self.label_13.setFont(font1)

        self.verticalLayout_18.addWidget(self.label_13)

        self.registerConfirmPassword = QTextEdit(self.pageRegister)
        self.registerConfirmPassword.setObjectName(u"registerConfirmPassword")
        sizePolicy2.setHeightForWidth(self.registerConfirmPassword.sizePolicy().hasHeightForWidth())
        self.registerConfirmPassword.setSizePolicy(sizePolicy2)
        self.registerConfirmPassword.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_18.addWidget(self.registerConfirmPassword)


        self.horizontalLayout_26.addLayout(self.verticalLayout_18)

        self.horizontalSpacer_41 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_41)


        self.VLRegister.addLayout(self.horizontalLayout_26)

        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLRegister.addItem(self.verticalSpacer_11)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 5, -1, 5)
        self.horizontalSpacer_42 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_42)

        self.registerLoginBtn = QPushButton(self.pageRegister)
        self.registerLoginBtn.setObjectName(u"registerLoginBtn")
        sizePolicy4.setHeightForWidth(self.registerLoginBtn.sizePolicy().hasHeightForWidth())
        self.registerLoginBtn.setSizePolicy(sizePolicy4)
        self.registerLoginBtn.setMaximumSize(QSize(16777215, 100))
        self.registerLoginBtn.setFont(font3)

        self.horizontalLayout_24.addWidget(self.registerLoginBtn)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_22)

        self.registerConfirmBtn = QPushButton(self.pageRegister)
        self.registerConfirmBtn.setObjectName(u"registerConfirmBtn")
        sizePolicy4.setHeightForWidth(self.registerConfirmBtn.sizePolicy().hasHeightForWidth())
        self.registerConfirmBtn.setSizePolicy(sizePolicy4)
        self.registerConfirmBtn.setMaximumSize(QSize(16777215, 100))
        self.registerConfirmBtn.setFont(font3)

        self.horizontalLayout_24.addWidget(self.registerConfirmBtn)

        self.horizontalSpacer_39 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_39)


        self.VLRegister.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLRegister.addItem(self.verticalSpacer_8)


        self.verticalLayout_7.addLayout(self.VLRegister)

        self.MainPages.addWidget(self.pageRegister)
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        sizePolicy.setHeightForWidth(self.pageHome.sizePolicy().hasHeightForWidth())
        self.pageHome.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.pageHome)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.VLHome = QVBoxLayout()
        self.VLHome.setObjectName(u"VLHome")
        self.VLHome.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.homeUserName = QLabel(self.pageHome)
        self.homeUserName.setObjectName(u"homeUserName")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.homeUserName.setFont(font4)

        self.horizontalLayout.addWidget(self.homeUserName)

        self.horizontalSpacer_14 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_14)

        self.homeSearchBar = QLineEdit(self.pageHome)
        self.homeSearchBar.setObjectName(u"homeSearchBar")

        self.horizontalLayout.addWidget(self.homeSearchBar)

        self.horizontalSpacer_13 = QSpacerItem(10, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_13)

        self.homeLogoutBtn = QPushButton(self.pageHome)
        self.homeLogoutBtn.setObjectName(u"homeLogoutBtn")
        font5 = QFont()
        font5.setBold(True)
        self.homeLogoutBtn.setFont(font5)

        self.horizontalLayout.addWidget(self.homeLogoutBtn)

        self.homeAddRoomBtn = QPushButton(self.pageHome)
        self.homeAddRoomBtn.setObjectName(u"homeAddRoomBtn")
        self.homeAddRoomBtn.setFont(font5)

        self.horizontalLayout.addWidget(self.homeAddRoomBtn)

        self.homeCreateRoomBtn = QPushButton(self.pageHome)
        self.homeCreateRoomBtn.setObjectName(u"homeCreateRoomBtn")
        self.homeCreateRoomBtn.setFont(font5)

        self.horizontalLayout.addWidget(self.homeCreateRoomBtn)


        self.VLHome.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.pageHome)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy6)
        self.scrollArea.setSizeIncrement(QSize(1, 1))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidget.setObjectName(u"scrollAreaWidget")
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 928, 675))
        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.VLHome.addWidget(self.scrollArea)


        self.verticalLayout_4.addLayout(self.VLHome)

        self.MainPages.addWidget(self.pageHome)
        self.pageCreateRoom = QWidget()
        self.pageCreateRoom.setObjectName(u"pageCreateRoom")
        sizePolicy.setHeightForWidth(self.pageCreateRoom.sizePolicy().hasHeightForWidth())
        self.pageCreateRoom.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.pageCreateRoom)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.VLCreateRoom = QVBoxLayout()
        self.VLCreateRoom.setSpacing(0)
        self.VLCreateRoom.setObjectName(u"VLCreateRoom")
        self.VLCreateRoom.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalSpacer = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLCreateRoom.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.pageCreateRoom)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.VLCreateRoom.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_7 = QLabel(self.pageCreateRoom)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 60))
        self.label_7.setFont(font1)

        self.verticalLayout_19.addWidget(self.label_7)

        self.createRoomName = QTextEdit(self.pageCreateRoom)
        self.createRoomName.setObjectName(u"createRoomName")
        self.createRoomName.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.createRoomName.sizePolicy().hasHeightForWidth())
        self.createRoomName.setSizePolicy(sizePolicy5)
        self.createRoomName.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_19.addWidget(self.createRoomName)


        self.horizontalLayout_14.addLayout(self.verticalLayout_19)

        self.horizontalSpacer_8 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_8)


        self.VLCreateRoom.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_4 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_8 = QLabel(self.pageCreateRoom)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 60))
        self.label_8.setFont(font1)

        self.verticalLayout_20.addWidget(self.label_8)

        self.createRoomDescription = QTextEdit(self.pageCreateRoom)
        self.createRoomDescription.setObjectName(u"createRoomDescription")
        sizePolicy2.setHeightForWidth(self.createRoomDescription.sizePolicy().hasHeightForWidth())
        self.createRoomDescription.setSizePolicy(sizePolicy2)
        self.createRoomDescription.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_20.addWidget(self.createRoomDescription)


        self.horizontalLayout_12.addLayout(self.verticalLayout_20)

        self.horizontalSpacer_5 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)


        self.VLCreateRoom.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLCreateRoom.addItem(self.verticalSpacer_12)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 10, -1, 10)
        self.horizontalSpacer_9 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.createRoomCancleBtn = QPushButton(self.pageCreateRoom)
        self.createRoomCancleBtn.setObjectName(u"createRoomCancleBtn")
        sizePolicy4.setHeightForWidth(self.createRoomCancleBtn.sizePolicy().hasHeightForWidth())
        self.createRoomCancleBtn.setSizePolicy(sizePolicy4)
        self.createRoomCancleBtn.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_10.addWidget(self.createRoomCancleBtn)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)

        self.createRoomConfirmBtn = QPushButton(self.pageCreateRoom)
        self.createRoomConfirmBtn.setObjectName(u"createRoomConfirmBtn")
        sizePolicy4.setHeightForWidth(self.createRoomConfirmBtn.sizePolicy().hasHeightForWidth())
        self.createRoomConfirmBtn.setSizePolicy(sizePolicy4)
        self.createRoomConfirmBtn.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_10.addWidget(self.createRoomConfirmBtn)

        self.horizontalSpacer_10 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.VLCreateRoom.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLCreateRoom.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addLayout(self.VLCreateRoom)

        self.MainPages.addWidget(self.pageCreateRoom)
        self.pageJoinRoom = QWidget()
        self.pageJoinRoom.setObjectName(u"pageJoinRoom")
        sizePolicy.setHeightForWidth(self.pageJoinRoom.sizePolicy().hasHeightForWidth())
        self.pageJoinRoom.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.pageJoinRoom)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.VLJoinRoom = QVBoxLayout()
        self.VLJoinRoom.setSpacing(0)
        self.VLJoinRoom.setObjectName(u"VLJoinRoom")
        self.VLJoinRoom.setContentsMargins(-1, 0, -1, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLJoinRoom.addItem(self.verticalSpacer_4)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_12)

        self.label_15 = QLabel(self.pageJoinRoom)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_15)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_15)


        self.VLJoinRoom.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 15, -1, 15)
        self.horizontalSpacer_16 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_16)

        self.label_16 = QLabel(self.pageJoinRoom)
        self.label_16.setObjectName(u"label_16")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy7)
        self.label_16.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_16)

        self.horizontalSpacer_50 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_50)

        self.joinRoomCode = QTextEdit(self.pageJoinRoom)
        self.joinRoomCode.setObjectName(u"joinRoomCode")
        sizePolicy2.setHeightForWidth(self.joinRoomCode.sizePolicy().hasHeightForWidth())
        self.joinRoomCode.setSizePolicy(sizePolicy2)
        self.joinRoomCode.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_17.addWidget(self.joinRoomCode)

        self.horizontalSpacer_17 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_17)


        self.VLJoinRoom.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 15, -1, 15)
        self.horizontalSpacer_19 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_19)

        self.joinRoomCancleBtn = QPushButton(self.pageJoinRoom)
        self.joinRoomCancleBtn.setObjectName(u"joinRoomCancleBtn")
        sizePolicy4.setHeightForWidth(self.joinRoomCancleBtn.sizePolicy().hasHeightForWidth())
        self.joinRoomCancleBtn.setSizePolicy(sizePolicy4)
        self.joinRoomCancleBtn.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_15.addWidget(self.joinRoomCancleBtn)

        self.horizontalSpacer_20 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_20)

        self.joinRoomConfirm = QPushButton(self.pageJoinRoom)
        self.joinRoomConfirm.setObjectName(u"joinRoomConfirm")
        sizePolicy4.setHeightForWidth(self.joinRoomConfirm.sizePolicy().hasHeightForWidth())
        self.joinRoomConfirm.setSizePolicy(sizePolicy4)
        self.joinRoomConfirm.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_15.addWidget(self.joinRoomConfirm)

        self.horizontalSpacer_18 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_18)


        self.VLJoinRoom.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_3 = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLJoinRoom.addItem(self.verticalSpacer_3)


        self.verticalLayout_5.addLayout(self.VLJoinRoom)

        self.MainPages.addWidget(self.pageJoinRoom)
        self.pageRoom = QWidget()
        self.pageRoom.setObjectName(u"pageRoom")
        sizePolicy.setHeightForWidth(self.pageRoom.sizePolicy().hasHeightForWidth())
        self.pageRoom.setSizePolicy(sizePolicy)
        self.verticalLayout_8 = QVBoxLayout(self.pageRoom)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.VLRoom = QVBoxLayout()
        self.VLRoom.setSpacing(0)
        self.VLRoom.setObjectName(u"VLRoom")
        self.VLRoom.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.roomHomeBtn = QPushButton(self.pageRoom)
        self.roomHomeBtn.setObjectName(u"roomHomeBtn")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.roomHomeBtn.sizePolicy().hasHeightForWidth())
        self.roomHomeBtn.setSizePolicy(sizePolicy8)
        self.roomHomeBtn.setFont(font2)

        self.horizontalLayout_34.addWidget(self.roomHomeBtn)

        self.horizontalSpacer_49 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_49)

        self.roomCode = QLabel(self.pageRoom)
        self.roomCode.setObjectName(u"roomCode")
        sizePolicy8.setHeightForWidth(self.roomCode.sizePolicy().hasHeightForWidth())
        self.roomCode.setSizePolicy(sizePolicy8)
        font6 = QFont()
        font6.setPointSize(15)
        font6.setBold(True)
        self.roomCode.setFont(font6)

        self.horizontalLayout_34.addWidget(self.roomCode)

        self.roomName = QLabel(self.pageRoom)
        self.roomName.setObjectName(u"roomName")
        sizePolicy4.setHeightForWidth(self.roomName.sizePolicy().hasHeightForWidth())
        self.roomName.setSizePolicy(sizePolicy4)
        self.roomName.setFont(font6)

        self.horizontalLayout_34.addWidget(self.roomName)


        self.VLRoom.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")

        self.VLRoom.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 20, 10, 20)
        self.roomChatBtn = QPushButton(self.pageRoom)
        self.roomChatBtn.setObjectName(u"roomChatBtn")
        sizePolicy4.setHeightForWidth(self.roomChatBtn.sizePolicy().hasHeightForWidth())
        self.roomChatBtn.setSizePolicy(sizePolicy4)

        self.verticalLayout_2.addWidget(self.roomChatBtn)

        self.roomCallBtn = QPushButton(self.pageRoom)
        self.roomCallBtn.setObjectName(u"roomCallBtn")
        sizePolicy4.setHeightForWidth(self.roomCallBtn.sizePolicy().hasHeightForWidth())
        self.roomCallBtn.setSizePolicy(sizePolicy4)

        self.verticalLayout_2.addWidget(self.roomCallBtn)

        self.roomWorkshopBtn = QPushButton(self.pageRoom)
        self.roomWorkshopBtn.setObjectName(u"roomWorkshopBtn")
        sizePolicy4.setHeightForWidth(self.roomWorkshopBtn.sizePolicy().hasHeightForWidth())
        self.roomWorkshopBtn.setSizePolicy(sizePolicy4)

        self.verticalLayout_2.addWidget(self.roomWorkshopBtn)

        self.roomMemberBtn = QPushButton(self.pageRoom)
        self.roomMemberBtn.setObjectName(u"roomMemberBtn")
        sizePolicy4.setHeightForWidth(self.roomMemberBtn.sizePolicy().hasHeightForWidth())
        self.roomMemberBtn.setSizePolicy(sizePolicy4)

        self.verticalLayout_2.addWidget(self.roomMemberBtn)


        self.horizontalLayout_32.addLayout(self.verticalLayout_2)

        self.SubPages = QStackedWidget(self.pageRoom)
        self.SubPages.setObjectName(u"SubPages")
        sizePolicy.setHeightForWidth(self.SubPages.sizePolicy().hasHeightForWidth())
        self.SubPages.setSizePolicy(sizePolicy)
        self.pageChat = QWidget()
        self.pageChat.setObjectName(u"pageChat")
        sizePolicy.setHeightForWidth(self.pageChat.sizePolicy().hasHeightForWidth())
        self.pageChat.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.pageChat)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.VLChat = QVBoxLayout()
        self.VLChat.setObjectName(u"VLChat")
        self.VLChat.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_46)

        self.label_5 = QLabel(self.pageChat)
        self.label_5.setObjectName(u"label_5")
        font7 = QFont()
        font7.setPointSize(14)
        font7.setBold(True)
        self.label_5.setFont(font7)

        self.horizontalLayout_36.addWidget(self.label_5)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_47)


        self.VLChat.addLayout(self.horizontalLayout_36)

        self.chatHistoryArea = QScrollArea(self.pageChat)
        self.chatHistoryArea.setObjectName(u"chatHistoryArea")
        self.chatHistoryArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 810, 546))
        self.chatHistoryArea.setWidget(self.scrollAreaWidgetContents_2)

        self.VLChat.addWidget(self.chatHistoryArea)

        self.verticalSpacer_9 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLChat.addItem(self.verticalSpacer_9)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(-1, 0, 0, -1)
        self.chatSendTextEdit = QTextEdit(self.pageChat)
        self.chatSendTextEdit.setObjectName(u"chatSendTextEdit")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.chatSendTextEdit.sizePolicy().hasHeightForWidth())
        self.chatSendTextEdit.setSizePolicy(sizePolicy9)
        self.chatSendTextEdit.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_37.addWidget(self.chatSendTextEdit)

        self.chatSendTextConfirmBtn = QPushButton(self.pageChat)
        self.chatSendTextConfirmBtn.setObjectName(u"chatSendTextConfirmBtn")
        sizePolicy4.setHeightForWidth(self.chatSendTextConfirmBtn.sizePolicy().hasHeightForWidth())
        self.chatSendTextConfirmBtn.setSizePolicy(sizePolicy4)
        self.chatSendTextConfirmBtn.setMaximumSize(QSize(16777215, 80))
        self.chatSendTextConfirmBtn.setFont(font2)

        self.horizontalLayout_37.addWidget(self.chatSendTextConfirmBtn)


        self.VLChat.addLayout(self.horizontalLayout_37)


        self.verticalLayout_10.addLayout(self.VLChat)

        self.SubPages.addWidget(self.pageChat)
        self.pageCall = QWidget()
        self.pageCall.setObjectName(u"pageCall")
        sizePolicy.setHeightForWidth(self.pageCall.sizePolicy().hasHeightForWidth())
        self.pageCall.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QVBoxLayout(self.pageCall)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.VLCall = QVBoxLayout()
        self.VLCall.setSpacing(0)
        self.VLCall.setObjectName(u"VLCall")
        self.VLCall.setContentsMargins(40, 40, 40, 40)
        self.enterOrLeaveCall = QPushButton(self.pageCall)
        self.enterOrLeaveCall.setObjectName(u"enterOrLeaveCall")
        sizePolicy3.setHeightForWidth(self.enterOrLeaveCall.sizePolicy().hasHeightForWidth())
        self.enterOrLeaveCall.setSizePolicy(sizePolicy3)

        self.VLCall.addWidget(self.enterOrLeaveCall)


        self.verticalLayout_9.addLayout(self.VLCall)

        self.SubPages.addWidget(self.pageCall)
        self.pageWorkShop = QWidget()
        self.pageWorkShop.setObjectName(u"pageWorkShop")
        sizePolicy.setHeightForWidth(self.pageWorkShop.sizePolicy().hasHeightForWidth())
        self.pageWorkShop.setSizePolicy(sizePolicy)
        self.verticalLayout_12 = QVBoxLayout(self.pageWorkShop)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.VLWorkShop = QVBoxLayout()
        self.VLWorkShop.setObjectName(u"VLWorkShop")
        self.VLWorkShop.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_6 = QLabel(self.pageWorkShop)
        self.label_6.setObjectName(u"label_6")
        sizePolicy8.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy8)
        self.label_6.setFont(font3)

        self.horizontalLayout_38.addWidget(self.label_6)

        self.workshopRunBtn = QPushButton(self.pageWorkShop)
        self.workshopRunBtn.setObjectName(u"workshopRunBtn")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.workshopRunBtn.sizePolicy().hasHeightForWidth())
        self.workshopRunBtn.setSizePolicy(sizePolicy10)
        self.workshopRunBtn.setFont(font3)

        self.horizontalLayout_38.addWidget(self.workshopRunBtn)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_48)

        self.workshopImportBtn = QPushButton(self.pageWorkShop)
        self.workshopImportBtn.setObjectName(u"workshopImportBtn")
        sizePolicy10.setHeightForWidth(self.workshopImportBtn.sizePolicy().hasHeightForWidth())
        self.workshopImportBtn.setSizePolicy(sizePolicy10)
        self.workshopImportBtn.setFont(font3)

        self.horizontalLayout_38.addWidget(self.workshopImportBtn)

        self.workshopExportBtn = QPushButton(self.pageWorkShop)
        self.workshopExportBtn.setObjectName(u"workshopExportBtn")
        sizePolicy10.setHeightForWidth(self.workshopExportBtn.sizePolicy().hasHeightForWidth())
        self.workshopExportBtn.setSizePolicy(sizePolicy10)
        self.workshopExportBtn.setFont(font3)

        self.horizontalLayout_38.addWidget(self.workshopExportBtn)


        self.VLWorkShop.addLayout(self.horizontalLayout_38)

        self.workshopCodeSpace = QTextEdit(self.pageWorkShop)
        self.workshopCodeSpace.setObjectName(u"workshopCodeSpace")

        self.VLWorkShop.addWidget(self.workshopCodeSpace)


        self.verticalLayout_12.addLayout(self.VLWorkShop)

        self.SubPages.addWidget(self.pageWorkShop)
        self.pageMember = QWidget()
        self.pageMember.setObjectName(u"pageMember")
        sizePolicy.setHeightForWidth(self.pageMember.sizePolicy().hasHeightForWidth())
        self.pageMember.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QVBoxLayout(self.pageMember)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.VLMember = QVBoxLayout()
        self.VLMember.setObjectName(u"VLMember")
        self.listView = QListView(self.pageMember)
        self.listView.setObjectName(u"listView")

        self.VLMember.addWidget(self.listView)


        self.verticalLayout_11.addLayout(self.VLMember)

        self.SubPages.addWidget(self.pageMember)

        self.horizontalLayout_32.addWidget(self.SubPages)


        self.VLRoom.addLayout(self.horizontalLayout_32)


        self.verticalLayout_8.addLayout(self.VLRoom)

        self.MainPages.addWidget(self.pageRoom)

        self.forStretchVerticalLayout.addWidget(self.MainPages)


        self.verticalLayout.addLayout(self.forStretchVerticalLayout)


        self.retranslateUi(Form)

        self.MainPages.setCurrentIndex(1)
        self.SubPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Username :", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Password : ", None))
        self.loginRegisterBtn.setText(QCoreApplication.translate("Form", u"Register", None))
        self.loginConfirmBtn.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Register", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Username :", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Gmail :", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Phone Number :", None))
        self.registerGmail.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Password : ", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Confirm Password :", None))
        self.registerLoginBtn.setText(QCoreApplication.translate("Form", u"Login", None))
        self.registerConfirmBtn.setText(QCoreApplication.translate("Form", u"Confirm", None))
        self.homeUserName.setText(QCoreApplication.translate("Form", u"Name Surname", None))
        self.homeLogoutBtn.setText(QCoreApplication.translate("Form", u"logout", None))
        self.homeAddRoomBtn.setText(QCoreApplication.translate("Form", u"Add", None))
        self.homeCreateRoomBtn.setText(QCoreApplication.translate("Form", u"Create", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Create Room", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Room Name :", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Description :", None))
        self.createRoomCancleBtn.setText(QCoreApplication.translate("Form", u"Cancle", None))
        self.createRoomConfirmBtn.setText(QCoreApplication.translate("Form", u"Create", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Join Room", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Room Code:", None))
        self.joinRoomCancleBtn.setText(QCoreApplication.translate("Form", u"Cancle", None))
        self.joinRoomConfirm.setText(QCoreApplication.translate("Form", u"Confirm", None))
        self.roomHomeBtn.setText(QCoreApplication.translate("Form", u"Home", None))
        self.roomCode.setText(QCoreApplication.translate("Form", u"Code : ", None))
        self.roomName.setText(QCoreApplication.translate("Form", u"Place Holder", None))
        self.roomChatBtn.setText(QCoreApplication.translate("Form", u"Chat", None))
        self.roomCallBtn.setText(QCoreApplication.translate("Form", u"Call", None))
        self.roomWorkshopBtn.setText(QCoreApplication.translate("Form", u"Workshop", None))
        self.roomMemberBtn.setText(QCoreApplication.translate("Form", u"Members", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Chat", None))
        self.chatSendTextConfirmBtn.setText(QCoreApplication.translate("Form", u"<", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"WorkSpace", None))
        self.workshopRunBtn.setText(QCoreApplication.translate("Form", u"Run", None))
        self.workshopImportBtn.setText(QCoreApplication.translate("Form", u"Import", None))
        self.workshopExportBtn.setText(QCoreApplication.translate("Form", u"Export", None))
    # retranslateUi