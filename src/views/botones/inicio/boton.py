from src.views.botones.configuraciones.boton_configuraciones import Boton_configuraciones
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from .funciones import Funciones
from src.views.botones.ingresar.boton_ingresar import Boton_ingresar
from src.views.botones.salida.boton_salida import Boton_salida
from src.views.botones.configuraciones.boton_configuraciones import Boton_configuraciones


class Boton(Funciones,Boton_ingresar,Boton_salida,Boton_configuraciones):

    '''
    Botones Pantalla inicio
    '''
    def boton_home(self, widget):
        self.label_img_esquina = QToolButton(widget)
        self.label_img_esquina.setGeometry(30,5,250,60)        
        self.label_img_esquina.setObjectName("button_home") #nombre de enlace a css
        self.label_img_esquina.clicked.connect(self.HomeWindow)
        self.label_img_esquina.setVisible(False)

    def boton_inicio_ingresar(self, widget):
        self.ingresar = QToolButton(widget)
        self.ingresar.setText('INGRESO MANUAL')
        self.ingresar.setObjectName("button") #nombre de enlace a css
        self.ingresar.setIcon(QIcon('src/views/static/icons/icono_entrar')) #icono
        self.ingresar.setIconSize(QSize(60,60))
        self.ingresar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ingresar.clicked.connect(self.Ingresar)
        self.ingresar.setGeometry(44.7, 112.5, 290, 180)
        self.ingresar.setVisible(False)

    def boton_inicio_estadisticas(self,widget):
        self.estadisticas = QToolButton(widget)
        self.estadisticas.setText('ESTADISTICAS')
        self.estadisticas.setObjectName("button")
        self.estadisticas.setIcon(QIcon('src/views/static/icons/icono_estadisticas'))
        self.estadisticas.setIconSize(QSize(60,60))
        self.estadisticas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.estadisticas.clicked.connect(self.Estadisticas)
        self.estadisticas.setGeometry(367, 112.5, 290, 180)
        self.estadisticas.setVisible(False)
        
    def boton_inicio_detener_alarma(self,widget):
        self.detener_alarma = QToolButton(widget)
        self.detener_alarma.setText('DETENER ALARMA')
        self.detener_alarma.setObjectName("button")
        self.detener_alarma.setIcon(QIcon('src/views/static/icons/icono_campana'))
        self.detener_alarma.setIconSize(QSize(60,60))
        self.detener_alarma.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.detener_alarma.clicked.connect(self.DetenerAlarma)
        self.detener_alarma.setGeometry(689.3, 112.5, 290, 180)
        self.detener_alarma.setVisible(False)

    def boton_inicio_salida_manual(self,widget):
        self.salida_manual = QToolButton(widget)
        self.salida_manual.setText('SALIDA MANUAL')
        self.salida_manual.setObjectName("button")
        self.salida_manual.setIcon(QIcon('src/views/static/icons/icono_salir'))
        self.salida_manual.setIconSize(QSize(60,60))
        self.salida_manual.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.salida_manual.clicked.connect(self.Salida_manual)
        self.salida_manual.setGeometry(44.7, 348.9, 290, 180)
        self.salida_manual.setVisible(False)


    def boton_inicio_configuracion(self,widget):
        self.configuracion = QToolButton(widget)
        self.configuracion.setText('CONFIGURACIÓN')
        self.configuracion.setObjectName("button")
        self.configuracion.setIcon(QIcon('src/views/static/icons/icono_configuraciones'))
        self.configuracion.setIconSize(QSize(70,70))
        self.configuracion.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuracion.clicked.connect(self.Configuracion)
        self.configuracion.setGeometry(367, 348.9, 290, 180)
        self.configuracion.setVisible(False)


    def boton_inicio_informacion(self,widget):
        self.informacion = QToolButton(widget)
        self.informacion.setText('INFORMACIÓN')
        self.informacion.setObjectName("button")
        self.informacion.setIcon(QIcon('src/views/static/icons/icono_info'))
        self.informacion.setIconSize(QSize(50,50))
        self.informacion.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.informacion.clicked.connect(self.Informacion)        
        self.informacion.setGeometry(689.3, 348.9, 290, 180)
        self.informacion.setVisible(False)
