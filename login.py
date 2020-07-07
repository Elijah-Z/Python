# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login_Dialog(object):
    def setupUi(self, Login_Dialog):
        Login_Dialog.setObjectName("Login_Dialog")
        Login_Dialog.resize(535, 338)
        Login_Dialog.setMinimumSize(QtCore.QSize(535, 338))
        Login_Dialog.setMaximumSize(QtCore.QSize(535, 338))
        self.label = QtWidgets.QLabel(Login_Dialog)
        self.label.setGeometry(QtCore.QRect(130, 70, 61, 41))
        self.label.setObjectName("label")
        self.userName_lineEdit = QtWidgets.QLineEdit(Login_Dialog)
        self.userName_lineEdit.setGeometry(QtCore.QRect(190, 80, 161, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.userName_lineEdit.setFont(font)
        self.userName_lineEdit.setObjectName("userName_lineEdit")
        self.label_2 = QtWidgets.QLabel(Login_Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 120, 61, 41))
        self.label_2.setObjectName("label_2")
        self.passsWord_lineEdit = QtWidgets.QLineEdit(Login_Dialog)
        self.passsWord_lineEdit.setGeometry(QtCore.QRect(190, 130, 161, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.passsWord_lineEdit.setFont(font)
        self.passsWord_lineEdit.setObjectName("passsWord_lineEdit")
        self.login_PushButton = QtWidgets.QPushButton(Login_Dialog)
        self.login_PushButton.setGeometry(QtCore.QRect(130, 210, 75, 23))
        self.login_PushButton.setObjectName("login_PushButton")
        self.registrer_PushButton = QtWidgets.QPushButton(Login_Dialog)
        self.registrer_PushButton.setGeometry(QtCore.QRect(280, 210, 75, 23))
        self.registrer_PushButton.setObjectName("registrer_PushButton")

        self.retranslateUi(Login_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Login_Dialog)

    def retranslateUi(self, Login_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "Login"))
        self.label.setText(_translate("Login_Dialog", "用户名"))
        self.label_2.setText(_translate("Login_Dialog", "密  码"))
        self.login_PushButton.setText(_translate("Login_Dialog", "登录"))
        self.registrer_PushButton.setText(_translate("Login_Dialog", "注册"))
