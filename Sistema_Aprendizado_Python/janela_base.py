# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_janela_base(object):
    def setupUi(self, janela_base):
        janela_base.setObjectName("janela_base")
        janela_base.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(janela_base)
        self.centralwidget.setObjectName("centralwidget")
        janela_base.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(janela_base)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        janela_base.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(janela_base)
        self.statusbar.setObjectName("statusbar")
        janela_base.setStatusBar(self.statusbar)

        self.retranslateUi(janela_base)
        QtCore.QMetaObject.connectSlotsByName(janela_base)

    def retranslateUi(self, janela_base):
        _translate = QtCore.QCoreApplication.translate
        janela_base.setWindowTitle(_translate("janela_base", "MainWindow"))