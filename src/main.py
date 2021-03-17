from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow): #Ventana principal
    def __init__(self, parent=None, *args):
        super(MainWindow,self).__init__(parent = parent)
        with open("style.css") as f:
            self.setStyleSheet(f.read())
        'constants'
        self.title = 'RETEDECON'
        self.width = 1024
        self.height = 600

        self.setMinimumSize(self.width,self.height)    #tamaño mínimo
        self.setMaximumSize(self.width,self.height)  #tamaño máximo
        self.setWindowTitle(self.title)   #titulo
        self.setWindowIcon(QIcon("static/favicon3.png"))   #Favicon

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setObjectName("window") #nombre que enlaza en css
        '''
        Imagen central 
        '''
        self.label_img_central = QLabel(self)
        self.label_img_central.setGeometry(289,-10,1024,600)
        self.pixmap = QPixmap('static/Logo_central.png')   #Imagen central
        self.label_img_central.setPixmap(self.pixmap)

        '''
        Botones de home y logo esquina
        '''
        self.label_img_esquina = QLabel(self)
        self.label_img_esquina.setGeometry(0,0,0,0)
        self.pixmap = QPixmap('static/icons/logo_lateral.png')   #Imagen esquina
        self.label_img_esquina.setPixmap(self.pixmap)

        #Botones
        self.ingresar = QToolButton(self.centralWidget)
        self.ingresar.setText('INGRESO MANUAL')
        self.ingresar.setGeometry(0, 0, 0, 0) #Se define el vector en 0 para que no aparesca al inicio
        self.ingresar.setObjectName("button") #nombre de enlace a css
        self.ingresar.setIcon(QIcon('static/icons/icono_entrar')) #icono
        self.ingresar.setIconSize(QSize(60,60))
        self.ingresar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ingresar.clicked.connect(self.Ingresar)

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
        
        'timer'
        self.timer = QTimer()
        self.timer.setInterval(2500)
        self.timer.setSingleShot(True)
        self.timer.start()
        self.timer.timeout.connect(self.HomeWindow) #función a ejecutar pasados los 3 seg

    def HomeWindow(self):
        '''
        Esta función le da tamaños a los elementos de la pantalla de home, 
        que contiene 6 botones y un logo pequeño,
        También hace 0 el vector de geometría de los elementos de la otra pantalla
        '''
        #self.label_img_central.setWindowOpacity(op)
        self.label_img_central.setGeometry(0,0,0,0) #oculta la imagen
        self.label_img_esquina.setGeometry(15,5,500,100)
        self.ingresar.setGeometry(44.7, 112.5, 290, 180)
        self.estadisticas.setGeometry(367, 112.5, 290, 180)
        self.detener_alarma.setGeometry(689.3, 112.5, 290, 180)
        self.salida_manual.setGeometry(44.7, 348.9, 290, 180)
        self.configuracion.setGeometry(367, 348.9, 290, 180)
        self.informacion.setGeometry(689.3, 348.9, 290, 180)

    def Ingresar(self):
        print(1)
        self.label_img_central.setVisible(False)  # oculta la imagen
        self.label_img_esquina.setGeometry(15, 5, 500, 100)
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)

    def Ingresar(self):
        print(1)
        self.label_img_central.setVisible(False)  # oculta la imagen
        self.label_img_esquina.setGeometry(15, 5, 500, 100)
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)


if __name__=='__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()