# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_COM_S(object):
    def setupUi(self, COM_S):
        COM_S.setObjectName("COM_S")
        COM_S.resize(942, 611)
        self.centralwidget = QtWidgets.QWidget(COM_S)
        self.centralwidget.setObjectName("centralwidget")
        self.LABEL_TEXT = QtWidgets.QLabel(self.centralwidget)
        self.LABEL_TEXT.setGeometry(QtCore.QRect(310, 150, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LABEL_TEXT.setFont(font)
        self.LABEL_TEXT.setText("")
        self.LABEL_TEXT.setAlignment(QtCore.Qt.AlignCenter)
        self.LABEL_TEXT.setObjectName("LABEL_TEXT")
        self.BTN_CONECTAR = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_CONECTAR.setGeometry(QtCore.QRect(290, 330, 93, 28))
        self.BTN_CONECTAR.setObjectName("BTN_CONECTAR")
        self.BTN_DESCONECTAR = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_DESCONECTAR.setGeometry(QtCore.QRect(530, 330, 93, 28))
        self.BTN_DESCONECTAR.setObjectName("BTN_DESCONECTAR")
        COM_S.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(COM_S)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 26))
        self.menubar.setObjectName("menubar")
        COM_S.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(COM_S)
        self.statusbar.setObjectName("statusbar")
        COM_S.setStatusBar(self.statusbar)

        self.retranslateUi(COM_S)
        QtCore.QMetaObject.connectSlotsByName(COM_S)

    def retranslateUi(self, COM_S):
        _translate = QtCore.QCoreApplication.translate
        COM_S.setWindowTitle(_translate("COM_S", "MainWindow"))
        self.BTN_CONECTAR.setText(_translate("COM_S", "Conectar"))
        self.BTN_DESCONECTAR.setText(_translate("COM_S", "Desconectar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    COM_S = QtWidgets.QMainWindow()
    ui = Ui_COM_S()
    ui.setupUi(COM_S)
    COM_S.show()
    sys.exit(app.exec_())