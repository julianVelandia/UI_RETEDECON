from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow): #Ventana principal
    '''
    Esta clase crea la ventana padre, la cual contiene un 
    logo grande en el centro y cambia pasados n segundos 
    a la vista HomeWindow
    '''
    def __init__(self, parent=None, *args):
        super(MainWindow,self).__init__(parent = parent)
        
        with open("style.css") as f:
            self.setStyleSheet(f.read())

        self.setMinimumSize(1024,600)    #tamaño mínimo
        self.setMaximumSize(1024,600)  #tamaño máximo
        self.setWindowTitle('RETEDECON')   #titulo
        self.setObjectName("window")    #nombre que enlaza en css


class HomeWindow(QWidget):
    '''
    Esta clase crea la pantalla de home, que contiene 6 botones
    y un logo pequeño
    '''

    def __init__(self, parent=None, *args):
        super(HomeWindow,self).__init__(parent = parent)

        self.ingresar = QPushButton('ingreso')
        self.ingresar.setGeometry(44.7, 112.5, 290, 180)
        self.ingresar.setObjectName("bingresar")

        self.estatus = QPushButton('status')
        self.estatus.setGeometry(367, 112.5, 290, 180)
        self.estatus.setObjectName("bestatus")


        self.estatus = QPushButton('estatus')
        self.estatus.setGeometry(689.3, 112.5, 290, 180)
        self.estatus.setObjectName("bestatus")

        self.estatus = QPushButton('estatus')
        self.estatus.setGeometry(44.7, 348.9, 290, 180)
        self.estatus.setObjectName("bestatus")

        self.estatus = QPushButton('estatus')
        self.estatus.setGeometry(367, 348.9, 290, 180)
        self.estatus.setObjectName("bestatus")

        self.estatus = QPushButton('estatus')
        self.estatus.setGeometry(689.3, 348.9, 290, 180)
        self.estatus.setObjectName("bestatus")

if __name__=='__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()