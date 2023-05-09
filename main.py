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

        ######################################
        ########## EVENTO ESPECIAL ###########
        self.serial.readyRead.connect(self.read_data)
        ######################################
        ######################################

        ## configuramos la comunicacion
        self.serial.setBaudRate(9600)
        self.serial.setPortName('COM4')


# Metodos:
    def Conectar(self):
        self.serial.open(QIODevice.ReadWrite)  ## Abre el puerto

    def Desconectar(self):
        self.serial.close()

    def read_data(self):
        rx = self.serial.readLine()  ## Leyendo el puerto
        datos = str(rx, 'utf-8') ## Convertimos de byte a str
        self.LABEL_TEXT.setText(datos)  ## Mandando al Label



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyApp()
    window.show()
    app.exec_()