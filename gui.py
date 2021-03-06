# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'un.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 500, 300))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("img/bg.jpg"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.bt_exit = QtWidgets.QPushButton(self.centralwidget)
        self.bt_exit.setGeometry(QtCore.QRect(380, 230, 90, 30))
        self.bt_exit.setStyleSheet("QPushButton#bt_exit {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton#bt_exit:hover {\n"
"    background-color: rgb(159, 9, 47);\n"
"}\n"
"")
        self.bt_exit.setObjectName("bt_exit")
        self.bt_svernut = QtWidgets.QPushButton(self.centralwidget)
        self.bt_svernut.setGeometry(QtCore.QRect(260, 230, 90, 30))
        self.bt_svernut.setStyleSheet("QPushButton#bt_svernut {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton#bt_svernut:hover {\n"
"    background-color: rgb(159, 9, 47);\n"
"}\n"
"")
        self.bt_svernut.setObjectName("bt_svernut")
        self.bt_cs16 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_cs16.setGeometry(QtCore.QRect(260, 80, 90, 30))
        self.bt_cs16.setStyleSheet("QPushButton#bt_cs16 {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton#bt_cs16:hover {\n"
"    background-color: rgb(159, 9, 47);\n"
"}\n"
"")
        self.bt_cs16.setObjectName("bt_cs16")
        self.bt_css = QtWidgets.QPushButton(self.centralwidget)
        self.bt_css.setGeometry(QtCore.QRect(380, 80, 90, 30))
        self.bt_css.setStyleSheet("QPushButton#bt_css {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton#bt_css:hover {\n"
"    background-color: rgb(159, 9, 47);\n"
"}\n"
"")
        self.bt_css.setObjectName("bt_css")
        self.bt_csgo = QtWidgets.QPushButton(self.centralwidget)
        self.bt_csgo.setGeometry(QtCore.QRect(260, 130, 90, 30))
        self.bt_csgo.setStyleSheet("QPushButton#bt_csgo {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton#bt_csgo:hover {\n"
"    background-color: rgb(159, 9, 47);\n"
"}\n"
"")
        self.bt_csgo.setObjectName("bt_csgo")
        self.bt_dota2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_dota2.setGeometry(QtCore.QRect(380, 130, 90, 30))
        self.bt_dota2.setStyleSheet("QPushButton#bt_dota2 {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton#bt_dota2:hover {\n"
"    background-color: rgb(159, 9, 47);\n"
"}\n"
"")
        self.bt_dota2.setObjectName("bt_dota2")
        self.bt_readme = QtWidgets.QPushButton(self.centralwidget)
        self.bt_readme.setGeometry(QtCore.QRect(380, 180, 90, 30))
        self.bt_readme.setStyleSheet("QPushButton#bt_readme {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton#bt_readme:hover {\n"
"    background-color: rgb(159, 9, 47);\n"
"}\n"
"")
        self.bt_readme.setObjectName("bt_readme")
        self.bt_options = QtWidgets.QPushButton(self.centralwidget)
        self.bt_options.setGeometry(QtCore.QRect(260, 180, 90, 30))
        self.bt_options.setStyleSheet("QPushButton#bt_options {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton#bt_options:hover {\n"
"    background-color: rgb(159, 9, 47);\n"
"}\n"
"")
        self.bt_options.setObjectName("bt_options")
        self.my_tg = QtWidgets.QTextBrowser(self.centralwidget)
        self.my_tg.setGeometry(QtCore.QRect(0, 270, 101, 31))
        self.my_tg.setObjectName("my_tg")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_exit.setText(_translate("MainWindow", "??????????"))
        self.bt_svernut.setText(_translate("MainWindow", "????????????????"))
        self.bt_cs16.setText(_translate("MainWindow", "CS 1.6"))
        self.bt_css.setText(_translate("MainWindow", "CSS"))
        self.bt_csgo.setText(_translate("MainWindow", "CS GO"))
        self.bt_dota2.setText(_translate("MainWindow", "Dota2"))
        self.bt_readme.setText(_translate("MainWindow", "????????????????????"))
        self.bt_options.setText(_translate("MainWindow", "??????????????????"))
        self.my_tg.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[TG] @t_o_ma_s</p></body></html>"))
