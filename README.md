## Primera Interfaz de Usuario con PyQt5
#### Paso 1:
Crear un nuevo proyecto

#### Paso 2:
Diseñar la interfaz en Qt Designer
- Seleccionamos la plantilla main window
- Se colocan los widgets necesarios
- Definir los IDs de los widgets
- Guardamos el diseño dentro de nuestro proyecto

###### STYLE SHEET (QT DESIGNER)

```c++
QFrame{
}

QPushButton{
}

QPushButton:hover{
}

QLabel{
}

QLineEdit{
}

QTableWidget{
}

QSlider::handle:horizontal{
}

QSlider::add-page:horizontal{
}

QSlider::groove:horizontal{
}
```
```c++
background-color: rgb(130,187,62);
border-top-left-radius:20px;
border-bottom-left-radius:20px;
border-top-right-radius:5px;
border-bottom-right-radius:5px;
color:rgb(0,0,0);
font: 77 14pt "Arial";
gridline-color:rgb(130,187,62);
border: 1px solid rgb(0,0,0);
font-size:12pt;
width:28px;
height:28px;
left:11px;
right:11px;
margin:-12px;
border-radius:14px;
```

COLORS
https://htmlcolorcodes.com/es/

#### Paso 3:
Instalar el modulo de PyQt5 desde la terminal
```bash
pip install PyQt5
pip install pyqtgraph
```

#### Paso 4:
Correr el siguiente comando para convertir el archivo .ui a .py
```bash
pyuic5 -x 'name'.ui -o 'name'.py
pyuic5 -x GUI.ui -o gui_design.py
```

#### Paso 5:
Crear un archivo .py que llame a la clase de la interfaz
```python
class {NAMECLASS}(QtWidgets.QMainWindow, Ui_MainWindow):
    # Se define le contructor con todos los atributos necesarios y asociacion de metodos
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = {NAMECLASS}()
    window.show()
    app.exec_()
```
Asi queda en mi codigo:
```python
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
# Se define le contructor con todos los atributos necesarios y asociacion de metodos
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyApp()
    window.show()
    app.exec_()
```
#### Paso 6:
Definir los eventos de la interfaz

#### Paso 7:
Definir los metodos