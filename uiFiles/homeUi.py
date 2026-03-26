w# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hw3.ui'
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
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(680, 480)
        Form.setMinimumSize(QSize(680, 480))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 581, 461))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.userName = QLabel(self.verticalLayoutWidget)
        self.userName.setObjectName(u"userName")

        self.horizontalLayout.addWidget(self.userName)

        self.searchBar = QLineEdit(self.verticalLayoutWidget)
        self.searchBar.setObjectName(u"searchBar")

        self.horizontalLayout.addWidget(self.searchBar)

        self.logoutBtn = QPushButton(self.verticalLayoutWidget)
        self.logoutBtn.setObjectName(u"logoutBtn")

        self.horizontalLayout.addWidget(self.logoutBtn)

        self.editBtn = QPushButton(self.verticalLayoutWidget)
        self.editBtn.setObjectName(u"editBtn")

        self.horizontalLayout.addWidget(self.editBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setSizeIncrement(QSize(1, 1))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidget.setObjectName(u"scrollAreaWidget")
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 577, 406))
        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 9)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.userName.setText(QCoreApplication.translate("Form", u"Name Surname", None))
        self.logoutBtn.setText(QCoreApplication.translate("Form", u"logout", None))
        self.editBtn.setText(QCoreApplication.translate("Form", u"Edit", None))
    # retranslateUi

