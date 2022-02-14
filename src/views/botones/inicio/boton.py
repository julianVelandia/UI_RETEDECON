from src.views.botones.estudiantes.botonEstudiantes import BotonEstudiantes
from src.views.botones.informacion.boton_informacion import Boton_informacion
from src.views.botones.configuraciones.boton_configuraciones import Boton_configuraciones
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.views.botones.inicio.funciones import Funciones
from src.views.botones.ingresar.boton_ingresar import Boton_ingresar
from src.views.botones.salida.boton_salida import Boton_salida
from src.views.botones.configuraciones.boton_configuraciones import Boton_configuraciones
from src.views.botones.informacion.boton_informacion import Boton_informacion
from src.views.botones.estadisticas.boton_estadisticas import Boton_estadisticas

class Boton(Funciones, BotonEstudiantes, Boton_ingresar,Boton_salida,Boton_configuraciones,Boton_informacion, Boton_estadisticas):
    '''
    Botones Pantalla inicio
    '''
    def boton_home(self, widget):
        self.label_img_esquina = QToolButton(widget)
        self.label_img_esquina.setIcon(QIcon('src/views/static/icons/logo_lateral.png'))

        self.label_img_esquina.setIconSize(QSize(self.width/3,self.height/3))

        self.label_img_esquina.setGeometry(self.width/28, self.height/30, 
                                            self.width/4, self.height/11)        
        self.label_img_esquina.setObjectName("button_home") #nombre de enlace a css
        self.label_img_esquina.clicked.connect(self.HomeWindow)
        self.label_img_esquina.setVisible(False)

        self.atras = QToolButton(widget)
        self.atras.setGeometry(self.width-(self.width/6), self.height/30,
                                self.height/10,self.height/10)        
        self.atras.setObjectName("NotButton") #nombre de enlace a css
        self.atras.setIcon(QIcon('src/views/static/icons/icono_atras')) #icono
        self.atras.setIconSize(QSize(self.height/20,self.height/20))
        self.atras.clicked.connect(self.Atras)
        self.atras.setVisible(False)

    def boton_inicio_ingresar(self, widget):
        self.ingresar = QToolButton(widget)
        self.ingresar.setText('INGRESO MANUAL')
        self.ingresar.setObjectName("button") #nombre de enlace a css
        self.ingresar.setIcon(QIcon('src/views/static/icons/icono_entrar')) #icono
        self.ingresar.setIconSize(QSize(self.height/11,self.height/11))
        self.ingresar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ingresar.clicked.connect(self.Ingresar)
        self.ingresar.setGeometry(self.width/23, self.height/7, 
                                    self.width/3.6, self.height/3.3)
        self.ingresar.setVisible(False)

    def boton_inicio_estadisticas(self,widget):
        self.estadisticas = QToolButton(widget)
        self.estadisticas.setText('ESTADISTICAS')
        self.estadisticas.setObjectName("button")
        self.estadisticas.setIcon(QIcon('src/views/static/icons/icono_estadisticas'))
        self.estadisticas.setIconSize(QSize(self.height/11,self.height/11))
        self.estadisticas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.estadisticas.clicked.connect(self.Estadisticas)
        self.estadisticas.setGeometry(self.width/2.8, self.height/7, 
                                    self.width/3.6, self.height/3.3)
        self.estadisticas.setVisible(False)
        
    def boton_inicio_detener_alarma(self,widget):
        self.detener_alarma = QToolButton(widget)
        self.detener_alarma.setText('DETENER ALARMA')
        self.detener_alarma.setObjectName("button")
        self.detener_alarma.setIcon(QIcon('src/views/static/icons/icono_campana'))
        self.detener_alarma.setIconSize(QSize(self.height/11,self.height/11))
        self.detener_alarma.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.detener_alarma.clicked.connect(self.DetenerAlarma)
        self.detener_alarma.setGeometry(self.width/1.5, self.height/7, 
                                    self.width/3.6, self.height/3.3)
        self.detener_alarma.setVisible(False)

    def boton_inicio_salida_manual(self,widget):
        self.salida_manual = QToolButton(widget)
        self.salida_manual.setText('SALIDA MANUAL')
        self.salida_manual.setObjectName("button")
        self.salida_manual.setIcon(QIcon('src/views/static/icons/icono_salir'))
        self.salida_manual.setIconSize(QSize(self.height/11,self.height/11))
        self.salida_manual.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.salida_manual.clicked.connect(self.Salida_manual)
        self.salida_manual.setGeometry(self.width/23, self.height/1.9, 
                                    self.width/3.6, self.height/3.3)
        self.salida_manual.setVisible(False)

    def boton_inicio_configuracion(self,widget):
        self.configuracion = QToolButton(widget)
        self.configuracion.setText('CONFIGURACIÓN')
        self.configuracion.setObjectName("button")
        self.configuracion.setIcon(QIcon('src/views/static/icons/icono_configuraciones'))
        self.configuracion.setIconSize(QSize(self.height/11,self.height/11))
        self.configuracion.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuracion.clicked.connect(self.Configuracion)
        self.configuracion.setGeometry(self.width/2.8, self.height/1.9, 
                                    self.width/3.6, self.height/3.3)
        self.configuracion.setVisible(False)

    def boton_inicio_informacion(self,widget):
        self.informacion = QToolButton(widget)
        self.informacion.setText('INFORMACIÓN')
        self.informacion.setObjectName("button")
        self.informacion.setIcon(QIcon('src/views/static/icons/icono_info'))
        self.informacion.setIconSize(QSize(self.height/11,self.height/11))
        self.informacion.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.informacion.clicked.connect(self.Informacion)        
        self.informacion.setGeometry(self.width/1.5, self.height/1.9, 
                                    self.width/3.6, self.height/3.3)
        self.informacion.setVisible(False)
        print(self.height/10)