from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time


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

        '''
        Configuraciones básicas
        '''
        self.setMinimumSize(1024,600)    #tamaño mínimo
        self.setMaximumSize(1024,600)  #tamaño máximo
        self.setWindowTitle('RETEDECON')   #titulo
        self.setWindowIcon(QIcon("static/favicon.png"))   #Favicon
        
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setObjectName("window") #nombre que enlaza en css 
        
        self.label_img_central = QLabel(self)
        self.label_img_central.setGeometry(288.9,-10,1024,600)
        self.pixmap = QPixmap('static/Logo_central.png')   #Imagen central
        self.label_img_central.setPixmap(self.pixmap)
        

        self.label_img_esquina = QLabel(self)
        self.label_img_esquina.setGeometry(0,0,0,0)
        self.pixmap = QPixmap('static/icons/logo_lateral.png')   #Imagen esquina
        self.label_img_esquina.setPixmap(self.pixmap)

        '''
        Botones de home
        '''
        self.ingresar = QToolButton(self.centralWidget)
        self.ingresar.setText('INGRESO MANUAL')
        self.ingresar.setGeometry(0, 0, 0, 0)
        self.ingresar.setObjectName("button")
        self.ingresar.setIcon(QIcon('static/icons/icono_entrar'))
        self.ingresar.setIconSize(QSize(60,60))
        self.ingresar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.estadisticas = QToolButton(self.centralWidget)
        self.estadisticas.setText('ESTADISTICAS')
        self.estadisticas.setGeometry(0, 0, 0, 0)
        self.estadisticas.setObjectName("button")
        self.estadisticas.setIcon(QIcon('static/icons/icono_estadisticas'))
        self.estadisticas.setIconSize(QSize(60,60))
        self.estadisticas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.detener_alarma = QToolButton(self.centralWidget)
        self.detener_alarma.setText('DETENER ALARMA')
        self.detener_alarma.setGeometry(0, 0, 0, 0)
        self.detener_alarma.setObjectName("button")
        self.detener_alarma.setIcon(QIcon('static/icons/icono_campana'))
        self.detener_alarma.setIconSize(QSize(60,60))
        self.detener_alarma.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.salida_manual = QToolButton(self.centralWidget)
        self.salida_manual.setText('SALIDA MANUAL')
        self.salida_manual.setGeometry(0, 0, 0, 0)
        self.salida_manual.setObjectName("button")
        self.salida_manual.setIcon(QIcon('static/icons/icono_salir'))
        self.salida_manual.setIconSize(QSize(60,60))
        self.salida_manual.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.configuracion = QToolButton(self.centralWidget)
        self.configuracion.setText('CONFIGURACIÓN')
        self.configuracion.setGeometry(0, 0, 0, 0)
        self.configuracion.setObjectName("button")
        self.configuracion.setIcon(QIcon('static/icons/icono_configuraciones'))
        self.configuracion.setIconSize(QSize(60,60))
        self.configuracion.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.informacion = QToolButton(self.centralWidget)
        self.informacion.setText('INFORMACIÓN')
        self.informacion.setGeometry(0, 0, 0, 0)
        self.informacion.setObjectName("button")
        self.informacion.setIcon(QIcon('static/icons/icono_campana'))
        self.informacion.setIconSize(QSize(60,60))
        self.informacion.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.HomeWindow)
        #self.HomeWindow()
    
    def HomeWindow(self):
        '''
        Esta función crea la pantalla de home, que contiene 6 botones
        y un logo pequeño
        '''
        
        self.label_img_central.setGeometry(0,0,0,0) #oculta la imagen

        self.label_img_esquina.setGeometry(15,5,500,100)


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