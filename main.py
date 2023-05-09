from gui_design import *
from PyQt5.QtSerialPort import QSerialPort

class MyApp(QtWidgets.QMainWindow, Ui_COM_S):
# Se define le contructor con todos los atributos necesarios y asociacion de metodos
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyApp()
    window.show()
    app.exec_()