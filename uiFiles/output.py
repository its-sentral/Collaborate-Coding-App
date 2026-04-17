# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prototype4.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListView,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(600, 480))
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.forStretchVerticalLayout = QVBoxLayout()
        self.forStretchVerticalLayout.setSpacing(0)
        self.forStretchVerticalLayout.setObjectName(u"forStretchVerticalLayout")
        self.MainPages = QStackedWidget(Form)
        self.MainPages.setObjectName(u"MainPages")
        sizePolicy.setHeightForWidth(self.MainPages.sizePolicy().hasHeightForWidth())
        self.MainPages.setSizePolicy(sizePolicy)
        self.MainPages.setStyleSheet(u"")
        self.pageLogin = QWidget()
        self.pageLogin.setObjectName(u"pageLogin")
        sizePolicy.setHeightForWidth(self.pageLogin.sizePolicy().hasHeightForWidth())
        self.pageLogin.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.pageLogin)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.VLLogin = QVBoxLayout()
        self.VLLogin.setSpacing(0)
        self.VLLogin.setObjectName(u"VLLogin")
        self.VLLogin.setContentsMargins(-1, 0, -1, 0)
        self.FrameLogin = QFrame(self.pageLogin)
        self.FrameLogin.setObjectName(u"FrameLogin")
        self.FrameLogin.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameLogin.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.FrameLogin)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer_25 = QSpacerItem(32, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_25)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, -1, -1, -1)
        self.verticalSpacer_13 = QSpacerItem(20, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_23.addItem(self.verticalSpacer_13)

        self.FrameLoginImage = QFrame(self.FrameLogin)
        self.FrameLoginImage.setObjectName(u"FrameLoginImage")
        self.FrameLoginImage.setMinimumSize(QSize(50, 0))
        self.FrameLoginImage.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameLoginImage.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.FrameLoginImage)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.VLImageContainer = QVBoxLayout()
        self.VLImageContainer.setSpacing(0)
        self.VLImageContainer.setObjectName(u"VLImageContainer")
        self.loginImage = QLabel(self.FrameLoginImage)
        self.loginImage.setObjectName(u"loginImage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.loginImage.sizePolicy().hasHeightForWidth())
        self.loginImage.setSizePolicy(sizePolicy1)
        self.loginImage.setMinimumSize(QSize(100, 75))
        self.loginImage.setMaximumSize(QSize(1350, 900))

        self.VLImageContainer.addWidget(self.loginImage)


        self.verticalLayout_22.addLayout(self.VLImageContainer)


        self.verticalLayout_23.addWidget(self.FrameLoginImage)

        self.verticalSpacer_14 = QSpacerItem(20, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_23.addItem(self.verticalSpacer_14)


        self.horizontalLayout_6.addLayout(self.verticalLayout_23)

        self.horizontalSpacer_35 = QSpacerItem(32, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_35)

        self.VLLoginWindow = QVBoxLayout()
        self.VLLoginWindow.setSpacing(0)
        self.VLLoginWindow.setObjectName(u"VLLoginWindow")
        self.VLLoginWindow.setContentsMargins(-1, -1, -1, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLLoginWindow.addItem(self.verticalSpacer_6)

        self.FrameLoginArea = QFrame(self.FrameLogin)
        self.FrameLoginArea.setObjectName(u"FrameLoginArea")
        sizePolicy1.setHeightForWidth(self.FrameLoginArea.sizePolicy().hasHeightForWidth())
        self.FrameLoginArea.setSizePolicy(sizePolicy1)
        self.FrameLoginArea.setMinimumSize(QSize(240, 0))
        self.FrameLoginArea.setMaximumSize(QSize(333, 16777215))
        self.FrameLoginArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameLoginArea.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.FrameLoginArea)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 10)
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_25.addItem(self.verticalSpacer_15)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_28 = QSpacerItem(80, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_28)

        self.label_2 = QLabel(self.FrameLoginArea)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout_23.addWidget(self.label_2)

        self.horizontalSpacer_29 = QSpacerItem(80, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_29)


        self.verticalLayout_24.addLayout(self.horizontalLayout_23)

        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_24.addItem(self.verticalSpacer_11)


        self.verticalLayout_25.addLayout(self.verticalLayout_24)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_27 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_27)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_9 = QLabel(self.FrameLoginArea)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_9.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_9)

        self.loginUsername = QTextEdit(self.FrameLoginArea)
        self.loginUsername.setObjectName(u"loginUsername")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.loginUsername.sizePolicy().hasHeightForWidth())
        self.loginUsername.setSizePolicy(sizePolicy3)
        self.loginUsername.setMinimumSize(QSize(0, 20))
        self.loginUsername.setMaximumSize(QSize(16777215, 40))
        self.loginUsername.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.loginUsername.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.loginUsername.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.verticalLayout_13.addWidget(self.loginUsername)


        self.horizontalLayout_22.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_26 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_26)


        self.verticalLayout_25.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_10 = QLabel(self.FrameLoginArea)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setMaximumSize(QSize(16777215, 60))
        self.label_10.setFont(font1)

        self.verticalLayout_14.addWidget(self.label_10)

        self.loginPassword = QTextEdit(self.FrameLoginArea)
        self.loginPassword.setObjectName(u"loginPassword")
        sizePolicy3.setHeightForWidth(self.loginPassword.sizePolicy().hasHeightForWidth())
        self.loginPassword.setSizePolicy(sizePolicy3)
        self.loginPassword.setMinimumSize(QSize(0, 20))
        self.loginPassword.setMaximumSize(QSize(16777215, 40))
        self.loginPassword.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.loginPassword.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.loginPassword.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.verticalLayout_14.addWidget(self.loginPassword)


        self.horizontalLayout_3.addLayout(self.verticalLayout_14)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_25.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacer_10)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 10, -1, 10)
        self.horizontalSpacer_30 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_30)

        self.loginRegisterBtn = QPushButton(self.FrameLoginArea)
        self.loginRegisterBtn.setObjectName(u"loginRegisterBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.loginRegisterBtn.sizePolicy().hasHeightForWidth())
        self.loginRegisterBtn.setSizePolicy(sizePolicy4)
        self.loginRegisterBtn.setMinimumSize(QSize(70, 0))
        self.loginRegisterBtn.setMaximumSize(QSize(16777215, 60))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.loginRegisterBtn.setFont(font2)

        self.horizontalLayout_18.addWidget(self.loginRegisterBtn)

        self.horizontalSpacer_31 = QSpacerItem(20, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_31)

        self.loginConfirmBtn = QPushButton(self.FrameLoginArea)
        self.loginConfirmBtn.setObjectName(u"loginConfirmBtn")
        sizePolicy4.setHeightForWidth(self.loginConfirmBtn.sizePolicy().hasHeightForWidth())
        self.loginConfirmBtn.setSizePolicy(sizePolicy4)
        self.loginConfirmBtn.setMinimumSize(QSize(70, 0))
        self.loginConfirmBtn.setMaximumSize(QSize(16777215, 60))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.loginConfirmBtn.setFont(font3)

        self.horizontalLayout_18.addWidget(self.loginConfirmBtn)

        self.horizontalSpacer_21 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_21)


        self.verticalLayout_25.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_25.addItem(self.verticalSpacer_16)


        self.VLLoginWindow.addWidget(self.FrameLoginArea)

        self.verticalSpacer_5 = QSpacerItem(20, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLLoginWindow.addItem(self.verticalSpacer_5)


        self.horizontalLayout_6.addLayout(self.VLLoginWindow)

        self.horizontalSpacer_40 = QSpacerItem(32, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_40)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)


        self.VLLogin.addWidget(self.FrameLogin)


        self.verticalLayout_6.addLayout(self.VLLogin)

        self.MainPages.addWidget(self.pageLogin)
        self.pageRegister = QWidget()
        self.pageRegister.setObjectName(u"pageRegister")
        sizePolicy.setHeightForWidth(self.pageRegister.sizePolicy().hasHeightForWidth())
        self.pageRegister.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.pageRegister)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.VLRegister = QVBoxLayout()
        self.VLRegister.setSpacing(0)
        self.VLRegister.setObjectName(u"VLRegister")
        self.VLRegister.setContentsMargins(-1, 0, -1, 0)
        self.FrameRegister = QFrame(self.pageRegister)
        self.FrameRegister.setObjectName(u"FrameRegister")
        self.FrameRegister.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameRegister.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.FrameRegister)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalSpacer_46 = QSpacerItem(32, 32, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_46)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalSpacer_19 = QSpacerItem(20, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_26.addItem(self.verticalSpacer_19)

        self.FrameRegisterImageContainer = QFrame(self.FrameRegister)
        self.FrameRegisterImageContainer.setObjectName(u"FrameRegisterImageContainer")
        self.FrameRegisterImageContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameRegisterImageContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.FrameRegisterImageContainer)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, 0, -1, -1)
        self.registerImage = QLabel(self.FrameRegisterImageContainer)
        self.registerImage.setObjectName(u"registerImage")
        self.registerImage.setMinimumSize(QSize(100, 75))
        self.registerImage.setMaximumSize(QSize(1350, 900))

        self.verticalLayout_30.addWidget(self.registerImage)


        self.verticalLayout_31.addLayout(self.verticalLayout_30)


        self.verticalLayout_26.addWidget(self.FrameRegisterImageContainer)

        self.verticalSpacer_18 = QSpacerItem(20, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_26.addItem(self.verticalSpacer_18)


        self.horizontalLayout_4.addLayout(self.verticalLayout_26)

        self.horizontalSpacer_47 = QSpacerItem(32, 32, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_47)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(-1, 0, -1, 0)
        self.verticalSpacer_20 = QSpacerItem(20, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_27.addItem(self.verticalSpacer_20)

        self.FrameRegisterArea = QFrame(self.FrameRegister)
        self.FrameRegisterArea.setObjectName(u"FrameRegisterArea")
        self.FrameRegisterArea.setMinimumSize(QSize(240, 0))
        self.FrameRegisterArea.setMaximumSize(QSize(333, 16777215))
        self.FrameRegisterArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameRegisterArea.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.FrameRegisterArea)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, -1, -1, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_28.addItem(self.verticalSpacer_7)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_33)

        self.label_3 = QLabel(self.FrameRegisterArea)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setFont(font)

        self.horizontalLayout_31.addWidget(self.label_3)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_34)


        self.verticalLayout_28.addLayout(self.horizontalLayout_31)

        self.verticalSpacer_22 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_28.addItem(self.verticalSpacer_22)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_32 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_32)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.label_17 = QLabel(self.FrameRegisterArea)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 60))
        self.label_17.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_17)

        self.registerGmail = QTextEdit(self.FrameRegisterArea)
        self.registerGmail.setObjectName(u"registerGmail")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.registerGmail.sizePolicy().hasHeightForWidth())
        self.registerGmail.setSizePolicy(sizePolicy5)
        self.registerGmail.setMaximumSize(QSize(16777215, 40))
        self.registerGmail.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.registerGmail.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.registerGmail.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.verticalLayout_15.addWidget(self.registerGmail)


        self.horizontalLayout_30.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_36 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_36)


        self.verticalLayout_28.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_35.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_51 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_51)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, -1, -1, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.label_11 = QLabel(self.FrameRegisterArea)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 60))
        self.label_11.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_11)

        self.horizontalSpacer_23 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_23)

        self.label_14 = QLabel(self.FrameRegisterArea)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 60))
        self.label_14.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_14)


        self.verticalLayout_16.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, -1, -1, -1)
        self.registerUsername = QTextEdit(self.FrameRegisterArea)
        self.registerUsername.setObjectName(u"registerUsername")
        sizePolicy3.setHeightForWidth(self.registerUsername.sizePolicy().hasHeightForWidth())
        self.registerUsername.setSizePolicy(sizePolicy3)
        self.registerUsername.setMaximumSize(QSize(16777215, 40))
        self.registerUsername.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.registerUsername.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.registerUsername.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.horizontalLayout_19.addWidget(self.registerUsername)

        self.horizontalSpacer_24 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_24)

        self.registerPhoneNumber = QTextEdit(self.FrameRegisterArea)
        self.registerPhoneNumber.setObjectName(u"registerPhoneNumber")
        sizePolicy5.setHeightForWidth(self.registerPhoneNumber.sizePolicy().hasHeightForWidth())
        self.registerPhoneNumber.setSizePolicy(sizePolicy5)
        self.registerPhoneNumber.setMaximumSize(QSize(16777215, 40))
        self.registerPhoneNumber.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.registerPhoneNumber.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.registerPhoneNumber.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.horizontalLayout_19.addWidget(self.registerPhoneNumber)


        self.verticalLayout_16.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_35.addLayout(self.verticalLayout_16)

        self.horizontalSpacer_54 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_54)


        self.verticalLayout_28.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_37 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_37)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_12 = QLabel(self.FrameRegisterArea)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 60))
        self.label_12.setFont(font1)

        self.verticalLayout_17.addWidget(self.label_12)

        self.registerPassword = QTextEdit(self.FrameRegisterArea)
        self.registerPassword.setObjectName(u"registerPassword")
        sizePolicy3.setHeightForWidth(self.registerPassword.sizePolicy().hasHeightForWidth())
        self.registerPassword.setSizePolicy(sizePolicy3)
        self.registerPassword.setMaximumSize(QSize(16777215, 40))
        self.registerPassword.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.registerPassword.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.registerPassword.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.verticalLayout_17.addWidget(self.registerPassword)


        self.horizontalLayout_28.addLayout(self.verticalLayout_17)

        self.horizontalSpacer_38 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_38)


        self.verticalLayout_28.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_44 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_44)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_13 = QLabel(self.FrameRegisterArea)
        self.label_13.setObjectName(u"label_13")
        sizePolicy5.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy5)
        self.label_13.setMaximumSize(QSize(16777215, 60))
        self.label_13.setFont(font1)

        self.verticalLayout_18.addWidget(self.label_13)

        self.registerConfirmPassword = QTextEdit(self.FrameRegisterArea)
        self.registerConfirmPassword.setObjectName(u"registerConfirmPassword")
        sizePolicy3.setHeightForWidth(self.registerConfirmPassword.sizePolicy().hasHeightForWidth())
        self.registerConfirmPassword.setSizePolicy(sizePolicy3)
        self.registerConfirmPassword.setMaximumSize(QSize(16777215, 40))
        self.registerConfirmPassword.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.registerConfirmPassword.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.registerConfirmPassword.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.verticalLayout_18.addWidget(self.registerConfirmPassword)


        self.horizontalLayout_26.addLayout(self.verticalLayout_18)

        self.horizontalSpacer_41 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_41)


        self.verticalLayout_28.addLayout(self.horizontalLayout_26)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_28.addItem(self.verticalSpacer_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 0, -1, 5)
        self.horizontalSpacer_42 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_42)

        self.registerLoginBtn = QPushButton(self.FrameRegisterArea)
        self.registerLoginBtn.setObjectName(u"registerLoginBtn")
        sizePolicy1.setHeightForWidth(self.registerLoginBtn.sizePolicy().hasHeightForWidth())
        self.registerLoginBtn.setSizePolicy(sizePolicy1)
        self.registerLoginBtn.setMinimumSize(QSize(70, 0))
        self.registerLoginBtn.setMaximumSize(QSize(16777215, 60))
        self.registerLoginBtn.setFont(font3)

        self.horizontalLayout_24.addWidget(self.registerLoginBtn)

        self.horizontalSpacer_22 = QSpacerItem(20, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_22)

        self.registerConfirmBtn = QPushButton(self.FrameRegisterArea)
        self.registerConfirmBtn.setObjectName(u"registerConfirmBtn")
        sizePolicy1.setHeightForWidth(self.registerConfirmBtn.sizePolicy().hasHeightForWidth())
        self.registerConfirmBtn.setSizePolicy(sizePolicy1)
        self.registerConfirmBtn.setMinimumSize(QSize(70, 0))
        self.registerConfirmBtn.setMaximumSize(QSize(16777215, 60))
        self.registerConfirmBtn.setFont(font3)

        self.horizontalLayout_24.addWidget(self.registerConfirmBtn)

        self.horizontalSpacer_39 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_39)


        self.verticalLayout_28.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_28.addItem(self.verticalSpacer_8)


        self.verticalLayout_29.addLayout(self.verticalLayout_28)


        self.verticalLayout_27.addWidget(self.FrameRegisterArea)

        self.verticalSpacer_21 = QSpacerItem(20, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_27.addItem(self.verticalSpacer_21)


        self.horizontalLayout_4.addLayout(self.verticalLayout_27)

        self.horizontalSpacer_45 = QSpacerItem(32, 32, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_45)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.VLRegister.addWidget(self.FrameRegister)


        self.verticalLayout_7.addLayout(self.VLRegister)

        self.MainPages.addWidget(self.pageRegister)
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        sizePolicy.setHeightForWidth(self.pageHome.sizePolicy().hasHeightForWidth())
        self.pageHome.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.pageHome)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.VLHome = QVBoxLayout()
        self.VLHome.setSpacing(0)
        self.VLHome.setObjectName(u"VLHome")
        self.VLHome.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.VLHome.setContentsMargins(-1, 0, -1, -1)
        self.FrameHome = QFrame(self.pageHome)
        self.FrameHome.setObjectName(u"FrameHome")
        self.FrameHome.setMinimumSize(QSize(0, 0))
        self.FrameHome.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameHome.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.FrameHome)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.FrameHomeSearchBar = QFrame(self.FrameHome)
        self.FrameHomeSearchBar.setObjectName(u"FrameHomeSearchBar")
        self.FrameHomeSearchBar.setMinimumSize(QSize(0, 20))
        self.FrameHomeSearchBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameHomeSearchBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.FrameHomeSearchBar)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.homeUserName = QLabel(self.FrameHomeSearchBar)
        self.homeUserName.setObjectName(u"homeUserName")
        self.homeUserName.setMinimumSize(QSize(40, 32))
        self.homeUserName.setMaximumSize(QSize(120, 16777215))
        self.homeUserName.setFont(font3)

        self.horizontalLayout.addWidget(self.homeUserName)

        self.horizontalSpacer_14 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_14)

        self.homeSearchBar = QLineEdit(self.FrameHomeSearchBar)
        self.homeSearchBar.setObjectName(u"homeSearchBar")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.homeSearchBar.sizePolicy().hasHeightForWidth())
        self.homeSearchBar.setSizePolicy(sizePolicy6)
        self.homeSearchBar.setMinimumSize(QSize(0, 32))
        self.homeSearchBar.setFont(font1)

        self.horizontalLayout.addWidget(self.homeSearchBar)

        self.horizontalSpacer_13 = QSpacerItem(10, 50, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_13)

        self.homeLogoutBtn = QPushButton(self.FrameHomeSearchBar)
        self.homeLogoutBtn.setObjectName(u"homeLogoutBtn")
        sizePolicy6.setHeightForWidth(self.homeLogoutBtn.sizePolicy().hasHeightForWidth())
        self.homeLogoutBtn.setSizePolicy(sizePolicy6)
        self.homeLogoutBtn.setMinimumSize(QSize(33, 32))
        self.homeLogoutBtn.setMaximumSize(QSize(120, 16777215))
        font4 = QFont()
        font4.setBold(True)
        self.homeLogoutBtn.setFont(font4)

        self.horizontalLayout.addWidget(self.homeLogoutBtn)

        self.homeAddRoomBtn = QPushButton(self.FrameHomeSearchBar)
        self.homeAddRoomBtn.setObjectName(u"homeAddRoomBtn")
        sizePolicy6.setHeightForWidth(self.homeAddRoomBtn.sizePolicy().hasHeightForWidth())
        self.homeAddRoomBtn.setSizePolicy(sizePolicy6)
        self.homeAddRoomBtn.setMinimumSize(QSize(33, 32))
        self.homeAddRoomBtn.setMaximumSize(QSize(120, 16777215))
        self.homeAddRoomBtn.setFont(font4)

        self.horizontalLayout.addWidget(self.homeAddRoomBtn)

        self.homeCreateRoomBtn = QPushButton(self.FrameHomeSearchBar)
        self.homeCreateRoomBtn.setObjectName(u"homeCreateRoomBtn")
        sizePolicy6.setHeightForWidth(self.homeCreateRoomBtn.sizePolicy().hasHeightForWidth())
        self.homeCreateRoomBtn.setSizePolicy(sizePolicy6)
        self.homeCreateRoomBtn.setMinimumSize(QSize(33, 32))
        self.homeCreateRoomBtn.setMaximumSize(QSize(120, 16777215))
        self.homeCreateRoomBtn.setFont(font4)

        self.horizontalLayout.addWidget(self.homeCreateRoomBtn)


        self.horizontalLayout_9.addLayout(self.horizontalLayout)


        self.verticalLayout_35.addWidget(self.FrameHomeSearchBar)

        self.FrameHomeRoomList = QFrame(self.FrameHome)
        self.FrameHomeRoomList.setObjectName(u"FrameHomeRoomList")
        self.FrameHomeRoomList.setMinimumSize(QSize(0, 0))
        self.FrameHomeRoomList.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameHomeRoomList.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.FrameHomeRoomList)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.scrollArea = QScrollArea(self.FrameHomeRoomList)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy7)
        self.scrollArea.setSizeIncrement(QSize(1, 1))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidget.setObjectName(u"scrollAreaWidget")
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 586, 412))
        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.verticalLayout_36.addWidget(self.scrollArea)


        self.verticalLayout_37.addLayout(self.verticalLayout_36)


        self.verticalLayout_35.addWidget(self.FrameHomeRoomList)


        self.VLHome.addWidget(self.FrameHome)


        self.verticalLayout_4.addLayout(self.VLHome)

        self.MainPages.addWidget(self.pageHome)
        self.pageCreateRoom = QWidget()
        self.pageCreateRoom.setObjectName(u"pageCreateRoom")
        sizePolicy.setHeightForWidth(self.pageCreateRoom.sizePolicy().hasHeightForWidth())
        self.pageCreateRoom.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.pageCreateRoom)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.FrameCreateRoom = QFrame(self.pageCreateRoom)
        self.FrameCreateRoom.setObjectName(u"FrameCreateRoom")
        self.FrameCreateRoom.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameCreateRoom.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.FrameCreateRoom)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_16, 1, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_17, 1, 2, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_28, 2, 1, 1, 1)

        self.FrameCreateRoomArea = QFrame(self.FrameCreateRoom)
        self.FrameCreateRoomArea.setObjectName(u"FrameCreateRoomArea")
        sizePolicy1.setHeightForWidth(self.FrameCreateRoomArea.sizePolicy().hasHeightForWidth())
        self.FrameCreateRoomArea.setSizePolicy(sizePolicy1)
        self.FrameCreateRoomArea.setMinimumSize(QSize(450, 300))
        self.FrameCreateRoomArea.setAutoFillBackground(False)
        self.FrameCreateRoomArea.setStyleSheet(u"")
        self.FrameCreateRoomArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameCreateRoomArea.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.FrameCreateRoomArea)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setSpacing(10)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_33.setContentsMargins(40, 40, 40, 40)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.FrameCreateRoomArea)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_33.addLayout(self.horizontalLayout_2)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_7 = QLabel(self.FrameCreateRoomArea)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 60))
        self.label_7.setFont(font1)

        self.verticalLayout_19.addWidget(self.label_7)

        self.createRoomName = QTextEdit(self.FrameCreateRoomArea)
        self.createRoomName.setObjectName(u"createRoomName")
        self.createRoomName.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.createRoomName.sizePolicy().hasHeightForWidth())
        self.createRoomName.setSizePolicy(sizePolicy1)
        self.createRoomName.setMinimumSize(QSize(0, 10))
        self.createRoomName.setMaximumSize(QSize(16777215, 30))
        self.createRoomName.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.createRoomName.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.createRoomName.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.verticalLayout_19.addWidget(self.createRoomName)


        self.verticalLayout_33.addLayout(self.verticalLayout_19)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_8 = QLabel(self.FrameCreateRoomArea)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 60))
        self.label_8.setFont(font1)

        self.verticalLayout_20.addWidget(self.label_8)

        self.createRoomDescription = QTextEdit(self.FrameCreateRoomArea)
        self.createRoomDescription.setObjectName(u"createRoomDescription")
        sizePolicy1.setHeightForWidth(self.createRoomDescription.sizePolicy().hasHeightForWidth())
        self.createRoomDescription.setSizePolicy(sizePolicy1)
        self.createRoomDescription.setMinimumSize(QSize(0, 10))
        self.createRoomDescription.setMaximumSize(QSize(16777215, 30))
        self.createRoomDescription.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.createRoomDescription.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.createRoomDescription.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.verticalLayout_20.addWidget(self.createRoomDescription)


        self.verticalLayout_33.addLayout(self.verticalLayout_20)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.createRoomCancelBtn = QPushButton(self.FrameCreateRoomArea)
        self.createRoomCancelBtn.setObjectName(u"createRoomCancelBtn")
        sizePolicy1.setHeightForWidth(self.createRoomCancelBtn.sizePolicy().hasHeightForWidth())
        self.createRoomCancelBtn.setSizePolicy(sizePolicy1)
        self.createRoomCancelBtn.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_10.addWidget(self.createRoomCancelBtn)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)

        self.createRoomConfirmBtn = QPushButton(self.FrameCreateRoomArea)
        self.createRoomConfirmBtn.setObjectName(u"createRoomConfirmBtn")
        sizePolicy1.setHeightForWidth(self.createRoomConfirmBtn.sizePolicy().hasHeightForWidth())
        self.createRoomConfirmBtn.setSizePolicy(sizePolicy1)
        self.createRoomConfirmBtn.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_10.addWidget(self.createRoomConfirmBtn)


        self.verticalLayout_33.addLayout(self.horizontalLayout_10)


        self.verticalLayout_34.addLayout(self.verticalLayout_33)


        self.gridLayout_2.addWidget(self.FrameCreateRoomArea, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.FrameCreateRoom)

        self.MainPages.addWidget(self.pageCreateRoom)
        self.pageJoinRoom = QWidget()
        self.pageJoinRoom.setObjectName(u"pageJoinRoom")
        sizePolicy.setHeightForWidth(self.pageJoinRoom.sizePolicy().hasHeightForWidth())
        self.pageJoinRoom.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.pageJoinRoom)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.FrameJoinRoom = QFrame(self.pageJoinRoom)
        self.FrameJoinRoom.setObjectName(u"FrameJoinRoom")
        self.FrameJoinRoom.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameJoinRoom.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.FrameJoinRoom)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_52, 1, 0, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_24, 0, 1, 1, 1)

        self.FrameJoinRoomArea = QFrame(self.FrameJoinRoom)
        self.FrameJoinRoomArea.setObjectName(u"FrameJoinRoomArea")
        self.FrameJoinRoomArea.setMinimumSize(QSize(450, 300))
        self.FrameJoinRoomArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameJoinRoomArea.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.FrameJoinRoomArea)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(20)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_21.setContentsMargins(40, 40, 40, 40)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_12)

        self.label_15 = QLabel(self.FrameJoinRoomArea)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_15)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_15)


        self.verticalLayout_21.addLayout(self.horizontalLayout_16)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(-1, 0, -1, -1)
        self.label_16 = QLabel(self.FrameJoinRoomArea)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setFont(font1)

        self.verticalLayout_42.addWidget(self.label_16)

        self.joinRoomCode = QTextEdit(self.FrameJoinRoomArea)
        self.joinRoomCode.setObjectName(u"joinRoomCode")
        sizePolicy5.setHeightForWidth(self.joinRoomCode.sizePolicy().hasHeightForWidth())
        self.joinRoomCode.setSizePolicy(sizePolicy5)
        self.joinRoomCode.setMinimumSize(QSize(0, 20))
        self.joinRoomCode.setMaximumSize(QSize(16777215, 30))
        self.joinRoomCode.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.joinRoomCode.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.joinRoomCode.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.verticalLayout_42.addWidget(self.joinRoomCode)


        self.verticalLayout_21.addLayout(self.verticalLayout_42)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.joinRoomCancelBtn = QPushButton(self.FrameJoinRoomArea)
        self.joinRoomCancelBtn.setObjectName(u"joinRoomCancelBtn")
        sizePolicy1.setHeightForWidth(self.joinRoomCancelBtn.sizePolicy().hasHeightForWidth())
        self.joinRoomCancelBtn.setSizePolicy(sizePolicy1)
        self.joinRoomCancelBtn.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_15.addWidget(self.joinRoomCancelBtn)

        self.horizontalSpacer_20 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_20)

        self.joinRoomConfirm = QPushButton(self.FrameJoinRoomArea)
        self.joinRoomConfirm.setObjectName(u"joinRoomConfirm")
        sizePolicy1.setHeightForWidth(self.joinRoomConfirm.sizePolicy().hasHeightForWidth())
        self.joinRoomConfirm.setSizePolicy(sizePolicy1)
        self.joinRoomConfirm.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_15.addWidget(self.joinRoomConfirm)


        self.verticalLayout_21.addLayout(self.horizontalLayout_15)


        self.verticalLayout_32.addLayout(self.verticalLayout_21)


        self.gridLayout.addWidget(self.FrameJoinRoomArea, 1, 1, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_27, 2, 1, 1, 1)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_53, 1, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.FrameJoinRoom)

        self.MainPages.addWidget(self.pageJoinRoom)
        self.pageRoom = QWidget()
        self.pageRoom.setObjectName(u"pageRoom")
        sizePolicy.setHeightForWidth(self.pageRoom.sizePolicy().hasHeightForWidth())
        self.pageRoom.setSizePolicy(sizePolicy)
        self.verticalLayout_8 = QVBoxLayout(self.pageRoom)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.FrameRoom = QFrame(self.pageRoom)
        self.FrameRoom.setObjectName(u"FrameRoom")
        self.FrameRoom.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameRoom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.FrameRoom)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.VLRoom = QVBoxLayout()
        self.VLRoom.setSpacing(0)
        self.VLRoom.setObjectName(u"VLRoom")
        self.VLRoom.setContentsMargins(-1, 0, -1, 0)
        self.FrameRoomTopBar = QFrame(self.FrameRoom)
        self.FrameRoomTopBar.setObjectName(u"FrameRoomTopBar")
        self.FrameRoomTopBar.setMinimumSize(QSize(0, 50))
        self.FrameRoomTopBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameRoomTopBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.FrameRoomTopBar)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(8)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(5, -1, -1, -1)
        self.roomHomeBtn = QPushButton(self.FrameRoomTopBar)
        self.roomHomeBtn.setObjectName(u"roomHomeBtn")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.roomHomeBtn.sizePolicy().hasHeightForWidth())
        self.roomHomeBtn.setSizePolicy(sizePolicy8)
        self.roomHomeBtn.setMinimumSize(QSize(80, 32))
        self.roomHomeBtn.setFont(font2)

        self.horizontalLayout_34.addWidget(self.roomHomeBtn)

        self.horizontalSpacer_49 = QSpacerItem(10, 50, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_49)

        self.roomCode = QLabel(self.FrameRoomTopBar)
        self.roomCode.setObjectName(u"roomCode")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.roomCode.sizePolicy().hasHeightForWidth())
        self.roomCode.setSizePolicy(sizePolicy9)
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        self.roomCode.setFont(font5)

        self.horizontalLayout_34.addWidget(self.roomCode)

        self.horizontalSpacer_43 = QSpacerItem(8, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_43)

        self.roomName = QLabel(self.FrameRoomTopBar)
        self.roomName.setObjectName(u"roomName")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.roomName.sizePolicy().hasHeightForWidth())
        self.roomName.setSizePolicy(sizePolicy10)
        self.roomName.setFont(font5)

        self.horizontalLayout_34.addWidget(self.roomName)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_34)


        self.VLRoom.addWidget(self.FrameRoomTopBar)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, -1, 0, -1)
        self.FrameRoomSectionBtnArea = QFrame(self.FrameRoom)
        self.FrameRoomSectionBtnArea.setObjectName(u"FrameRoomSectionBtnArea")
        self.FrameRoomSectionBtnArea.setMinimumSize(QSize(50, 0))
        self.FrameRoomSectionBtnArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameRoomSectionBtnArea.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.FrameRoomSectionBtnArea)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 20, 5, 20)
        self.roomChatBtn = QPushButton(self.FrameRoomSectionBtnArea)
        self.roomChatBtn.setObjectName(u"roomChatBtn")
        sizePolicy10.setHeightForWidth(self.roomChatBtn.sizePolicy().hasHeightForWidth())
        self.roomChatBtn.setSizePolicy(sizePolicy10)
        self.roomChatBtn.setMaximumSize(QSize(80, 80))

        self.verticalLayout_2.addWidget(self.roomChatBtn)

        self.roomCallBtn = QPushButton(self.FrameRoomSectionBtnArea)
        self.roomCallBtn.setObjectName(u"roomCallBtn")
        sizePolicy10.setHeightForWidth(self.roomCallBtn.sizePolicy().hasHeightForWidth())
        self.roomCallBtn.setSizePolicy(sizePolicy10)
        self.roomCallBtn.setMaximumSize(QSize(80, 80))

        self.verticalLayout_2.addWidget(self.roomCallBtn)

        self.roomWorkshopBtn = QPushButton(self.FrameRoomSectionBtnArea)
        self.roomWorkshopBtn.setObjectName(u"roomWorkshopBtn")
        sizePolicy10.setHeightForWidth(self.roomWorkshopBtn.sizePolicy().hasHeightForWidth())
        self.roomWorkshopBtn.setSizePolicy(sizePolicy10)
        self.roomWorkshopBtn.setMaximumSize(QSize(80, 80))

        self.verticalLayout_2.addWidget(self.roomWorkshopBtn)

        self.roomMemberBtn = QPushButton(self.FrameRoomSectionBtnArea)
        self.roomMemberBtn.setObjectName(u"roomMemberBtn")
        sizePolicy10.setHeightForWidth(self.roomMemberBtn.sizePolicy().hasHeightForWidth())
        self.roomMemberBtn.setSizePolicy(sizePolicy10)
        self.roomMemberBtn.setMaximumSize(QSize(80, 80))

        self.verticalLayout_2.addWidget(self.roomMemberBtn)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_17)

        self.roomLeaveBtn = QPushButton(self.FrameRoomSectionBtnArea)
        self.roomLeaveBtn.setObjectName(u"roomLeaveBtn")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setWeight(QFont.ExtraBold)
        self.roomLeaveBtn.setFont(font6)
        self.roomLeaveBtn.setStyleSheet(u"background-color: #941010 ")

        self.verticalLayout_2.addWidget(self.roomLeaveBtn)


        self.verticalLayout_40.addLayout(self.verticalLayout_2)


        self.horizontalLayout_32.addWidget(self.FrameRoomSectionBtnArea)

        self.FrameRoomSectionDisplayArea = QFrame(self.FrameRoom)
        self.FrameRoomSectionDisplayArea.setObjectName(u"FrameRoomSectionDisplayArea")
        self.FrameRoomSectionDisplayArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.FrameRoomSectionDisplayArea.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.FrameRoomSectionDisplayArea)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.SubPages = QStackedWidget(self.FrameRoomSectionDisplayArea)
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
        self.chatHistoryArea = QScrollArea(self.pageChat)
        self.chatHistoryArea.setObjectName(u"chatHistoryArea")
        self.chatHistoryArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 481, 315))
        self.chatHistoryArea.setWidget(self.scrollAreaWidgetContents_2)

        self.VLChat.addWidget(self.chatHistoryArea)

        self.verticalSpacer_9 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLChat.addItem(self.verticalSpacer_9)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(-1, 0, 0, -1)
        self.chatSendTextEdit = QTextEdit(self.pageChat)
        self.chatSendTextEdit.setObjectName(u"chatSendTextEdit")
        sizePolicy4.setHeightForWidth(self.chatSendTextEdit.sizePolicy().hasHeightForWidth())
        self.chatSendTextEdit.setSizePolicy(sizePolicy4)
        self.chatSendTextEdit.setMaximumSize(QSize(16777215, 60))
        self.chatSendTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.chatSendTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.horizontalLayout_37.addWidget(self.chatSendTextEdit)

        self.chatSendTextConfirmBtn = QPushButton(self.pageChat)
        self.chatSendTextConfirmBtn.setObjectName(u"chatSendTextConfirmBtn")
        sizePolicy10.setHeightForWidth(self.chatSendTextConfirmBtn.sizePolicy().hasHeightForWidth())
        self.chatSendTextConfirmBtn.setSizePolicy(sizePolicy10)
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
        # self.enterOrLeaveCall = QPushButton(self.pageCall)
        # self.enterOrLeaveCall.setObjectName(u"enterOrLeaveCall")
        # sizePolicy1.setHeightForWidth(self.enterOrLeaveCall.sizePolicy().hasHeightForWidth())
        # self.enterOrLeaveCall.setSizePolicy(sizePolicy1)

        # self.VLCall.addWidget(self.enterOrLeaveCall)
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
        self.horizontalLayout_38.setSpacing(4)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.workshopRunBtn = QPushButton(self.pageWorkShop)
        self.workshopRunBtn.setObjectName(u"workshopRunBtn")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.workshopRunBtn.sizePolicy().hasHeightForWidth())
        self.workshopRunBtn.setSizePolicy(sizePolicy11)
        self.workshopRunBtn.setMinimumSize(QSize(0, 32))
        self.workshopRunBtn.setFont(font3)

        self.horizontalLayout_38.addWidget(self.workshopRunBtn)

        self.horizontalSpacer_48 = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_48)

        self.workshopImportBtn = QPushButton(self.pageWorkShop)
        self.workshopImportBtn.setObjectName(u"workshopImportBtn")
        sizePolicy11.setHeightForWidth(self.workshopImportBtn.sizePolicy().hasHeightForWidth())
        self.workshopImportBtn.setSizePolicy(sizePolicy11)
        self.workshopImportBtn.setMinimumSize(QSize(0, 32))
        self.workshopImportBtn.setFont(font3)

        self.horizontalLayout_38.addWidget(self.workshopImportBtn)

        self.workshopExportBtn = QPushButton(self.pageWorkShop)
        self.workshopExportBtn.setObjectName(u"workshopExportBtn")
        sizePolicy11.setHeightForWidth(self.workshopExportBtn.sizePolicy().hasHeightForWidth())
        self.workshopExportBtn.setSizePolicy(sizePolicy11)
        self.workshopExportBtn.setMinimumSize(QSize(0, 32))
        self.workshopExportBtn.setFont(font3)

        self.horizontalLayout_38.addWidget(self.workshopExportBtn)


        self.VLWorkShop.addLayout(self.horizontalLayout_38)


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

        self.verticalLayout_41.addWidget(self.SubPages)


        self.horizontalLayout_32.addWidget(self.FrameRoomSectionDisplayArea)


        self.VLRoom.addLayout(self.horizontalLayout_32)


        self.verticalLayout_39.addLayout(self.VLRoom)


        self.verticalLayout_8.addWidget(self.FrameRoom)

        self.MainPages.addWidget(self.pageRoom)

        self.forStretchVerticalLayout.addWidget(self.MainPages)


        self.verticalLayout.addLayout(self.forStretchVerticalLayout)


        self.retranslateUi(Form)

        self.MainPages.setCurrentIndex(5)
        self.SubPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.loginImage.setText(QCoreApplication.translate("Form", u"IMG", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Username :", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Password : ", None))
        self.loginRegisterBtn.setText(QCoreApplication.translate("Form", u"Register", None))
        self.loginConfirmBtn.setText(QCoreApplication.translate("Form", u"Login", None))
        self.registerImage.setText(QCoreApplication.translate("Form", u"IMG", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Register", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Gmail :", None))
        self.registerGmail.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Username :", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Phone :", None))
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
        self.createRoomCancelBtn.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.createRoomConfirmBtn.setText(QCoreApplication.translate("Form", u"Create", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Join Room", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Room Code:", None))
        self.joinRoomCancelBtn.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.joinRoomConfirm.setText(QCoreApplication.translate("Form", u"Confirm", None))
        self.roomHomeBtn.setText(QCoreApplication.translate("Form", u"Home", None))
        self.roomCode.setText(QCoreApplication.translate("Form", u"Code : ", None))
        self.roomName.setText(QCoreApplication.translate("Form", u"Place Holder", None))
        self.roomChatBtn.setText(QCoreApplication.translate("Form", u"Chat", None))
        self.roomCallBtn.setText(QCoreApplication.translate("Form", u"Call", None))
        self.roomWorkshopBtn.setText(QCoreApplication.translate("Form", u"Workshop", None))
        self.roomMemberBtn.setText(QCoreApplication.translate("Form", u"Members", None))
        self.roomLeaveBtn.setText(QCoreApplication.translate("Form", u"Leave", None))
        self.chatSendTextConfirmBtn.setText(QCoreApplication.translate("Form", u"<", None))
        # self.enterOrLeaveCall.setText(QCoreApplication.translate("Form", u"Enter Call", None))
        self.workshopRunBtn.setText(QCoreApplication.translate("Form", u"Run", None))
        self.workshopImportBtn.setText(QCoreApplication.translate("Form", u"Import", None))
        self.workshopExportBtn.setText(QCoreApplication.translate("Form", u"Export", None))
    # retranslateUi

