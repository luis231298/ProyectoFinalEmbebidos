# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_app.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pgb_cocina = QtWidgets.QProgressBar(self.centralwidget)
        self.pgb_cocina.setGeometry(QtCore.QRect(10, 90, 118, 23))
        self.pgb_cocina.setProperty("value", 100)
        self.pgb_cocina.setObjectName("pgb_cocina")
        self.pgb_garage = QtWidgets.QProgressBar(self.centralwidget)
        self.pgb_garage.setGeometry(QtCore.QRect(210, 90, 118, 23))
        self.pgb_garage.setProperty("value", 100)
        self.pgb_garage.setObjectName("pgb_garage")
        self.pgb_pasillo = QtWidgets.QProgressBar(self.centralwidget)
        self.pgb_pasillo.setGeometry(QtCore.QRect(410, 90, 118, 23))
        self.pgb_pasillo.setProperty("value", 100)
        self.pgb_pasillo.setObjectName("pgb_pasillo")
        self.LE_Cocina = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_Cocina.setGeometry(QtCore.QRect(10, 60, 113, 22))
        self.LE_Cocina.setObjectName("LE_Cocina")
        self.LE_Garage = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_Garage.setGeometry(QtCore.QRect(210, 60, 113, 22))
        self.LE_Garage.setObjectName("LE_Garage")
        self.LE_Pasillo = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_Pasillo.setGeometry(QtCore.QRect(410, 60, 113, 22))
        self.LE_Pasillo.setObjectName("LE_Pasillo")
        self.LE_Luces = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_Luces.setGeometry(QtCore.QRect(10, 20, 113, 22))
        self.LE_Luces.setObjectName("LE_Luces")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 120, 171, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/cocina.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 120, 161, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("assets/garage.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 120, 171, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("assets/pasillo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 290, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LE_Cocina.setText(_translate("MainWindow", "Cocina"))
        self.LE_Garage.setText(_translate("MainWindow", "Garage"))
        self.LE_Pasillo.setText(_translate("MainWindow", "Pasillo"))
        self.LE_Luces.setText(_translate("MainWindow", "Luces"))
        self.lineEdit.setText(_translate("MainWindow", "Camaras"))

