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
        
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setObjectName("window")    #nombre que enlaza en css 
        
        '''
        botón temporal para la transición
        '''
        self.button = QPushButton('home',self.centralWidget) 
        self.button.setGeometry(100,100,100,100)
        self.button.clicked.connect(self.HomeWindow)


        self.ingresar = QPushButton('INGRESO MANUAL', self.centralWidget)
        self.ingresar.setGeometry(0, 0, 0, 0)
        self.ingresar.setObjectName("button")

        self.estadisticas = QPushButton('ESTADISTICAS',self.centralWidget)
        self.estadisticas.setGeometry(0,0, 0, 0)
        self.estadisticas.setObjectName("button")

        self.detener_alarma = QPushButton('DETENER ALARMA',self.centralWidget)
        self.detener_alarma.setGeometry(0, 0, 0, 0)
        self.detener_alarma.setObjectName("button")

        self.salida_manual = QPushButton('SALIDA MANUAL',self.centralWidget)
        self.salida_manual.setGeometry(0, 0, 0, 0)
        self.salida_manual.setObjectName("button")

        self.configuracion = QPushButton('CONFIGURACIÓN',self.centralWidget)
        self.configuracion.setGeometry(0, 0, 0, 0)
        self.configuracion.setObjectName("button")

        self.informacion = QPushButton('INFRMACIÓN',self.centralWidget)
        self.informacion.setGeometry(0, 0, 0, 0)
        self.informacion.setObjectName("button")

    def HomeWindow(self):
        '''
        Esta función crea la pantalla de home, que contiene 6 botones
        y un logo pequeño
        '''
        
        self.ingresar.setGeometry(44.7, 112.5, 290, 180)
      
        self.estadisticas.setGeometry(367, 112.5, 290, 180)

        self.detener_alarma.setGeometry(689.3, 112.5, 290, 180)

        self.salida_manual.setGeometry(44.7, 348.9, 290, 180)

        self.configuracion.setGeometry(367, 348.9, 290, 180)

        self.informacion.setGeometry(689.3, 348.9, 290, 180)

if __name__=='__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()