from gui_design import *
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtCore import QIODevice

class MyApp(QtWidgets.QMainWindow, Ui_COM_S):
# Se define le contructor con todos los atributos necesarios y asociacion de metodos
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.serial = QSerialPort()

        # Eventos
        self.BTN_CONECTAR.clicked.connect(self.Conectar)
        self.BTN_DESCONECTAR.clicked.connect(self.Desconectar)

        self.serial.setBaudRate(9600)
        self.serial.setPortName('COM4')




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyApp()
    window.show()
    app.exec_()