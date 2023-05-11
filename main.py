from gui_design import *
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtCore import QIODevice
import pyqtgraph as pg
import numpy as np

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

        ## Los vectores que son ejes de la grafica
        self.x = list(np.linspace(0, 100, 100))
        self.y = list(np.linspace(0, 0, 100))

        ## configurar la grafica
        pg.setConfigOption('background', '#86e277')
        pg.setConfigOption('foreground', '#000000')
        self.plt = pg.PlotWidget(title='Comunicacion Serial')
        self.GRPH_1.addWidget(self.plt)


# Metodos:
    def Conectar(self):
        self.serial.open(QIODevice.ReadWrite)  ## Abre el puerto

    def Desconectar(self):
        self.serial.close()

    def read_data(self):
        if not self.serial.canReadLine(): return
        rx = self.serial.readLine() ## Leyendo el puerto
        datos = str(rx, 'utf-8').strip() ## Convertimos de byte a str
        ## self.LABEL_TEXT.setText(datos)  ## Mandando al Label
        self.y = self.y[1:]  ## en este momento la lista tiene 99 elementos
        self.y.append(int(datos)) ## Apendizamos el valor leido en la comunicacion serial
        self.plt.clear()   ## Limpiamos la grafica para poder actualizarla
        self.plt.plot(self.x, self.y, pen=pg.mkPen('#000000', width=2)) ## Mandamos la lista actualizada


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyApp()
    window.show()
    app.exec_()