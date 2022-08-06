from src.views.botones.configuraciones.avanzada.boton_avanzada import Boton_avanzada
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# locals
from .funciones_configuraciones import Funcion_configuraciones
from .avanzada.boton_avanzada import Boton_avanzada
from .datos.boton_datos import Boton_datos

from screeninfo import get_monitors


class Boton_configuraciones(Funcion_configuraciones, Boton_avanzada, Boton_datos):
    width = get_monitors()[0].width
    height = get_monitors()[0].height

    #def boton_configuraciones_ajustes(self, widget):
        #self.configuraciones_ajustes = QToolButton(widget)
        #self.configuraciones_ajustes.setText('Ajustes de Pantallas')
        #self.configuraciones_ajustes.setObjectName("button")  # nombre de enlace a css
        #self.configuraciones_ajustes.setIcon(QIcon('src/views/static/icons/icono_config_pantalla'))  # icono
        #self.configuraciones_ajustes.setIconSize(QSize(self.height/11,self.height/11))
        #self.configuraciones_ajustes.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        #self.configuraciones_ajustes.clicked.connect(self.ConfiguracionesAjustes)
        #self.configuraciones_ajustes.setGeometry(self.width/5.7, self.height/7, self.width/3.6, self.height/3.3)
        #self.configuraciones_ajustes.setVisible(False)

    def boton_configuraciones_avanzada(self, widget):
        self.configuraciones_avanzada = QToolButton(widget)
        self.configuraciones_avanzada.setText('Configuración Avanzada\n(Administrador)')
        self.configuraciones_avanzada.setObjectName("button")  # nombre de enlace a css
        self.configuraciones_avanzada.setIcon(QIcon('src/views/static/icons/icono_config_avanzada'))  # icono
        self.configuraciones_avanzada.setIconSize(QSize(self.height/11,self.height/11))
        self.configuraciones_avanzada.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuraciones_avanzada.setGeometry(self.width/1.9, self.height/7, 
                                                self.width/3.6, self.height/3.3) 
        self.configuraciones_avanzada.clicked.connect(self.ConfiguracionesAvanzada)
        self.configuraciones_avanzada.setVisible(False)

    def boton_configuraciones_apagar(self, widget):
        self.configuraciones_apagar = QToolButton(widget)
        self.configuraciones_apagar.setText('Apagar')
        self.configuraciones_apagar.setObjectName("button")  # nombre de enlace a css
        self.configuraciones_apagar.setIcon(QIcon('src/views/static/icons/icono_apagar'))  # icono
        self.configuraciones_apagar.setIconSize(QSize(self.height/11,self.height/11))
        self.configuraciones_apagar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuraciones_apagar.clicked.connect(self.ConfiguracionesApagar)
        self.configuraciones_apagar.setGeometry(self.width/5, self.height/1.9,
                                                self.width/3.6, self.height/3.3) 
        self.configuraciones_apagar.setVisible(False)

    def boton_configuraciones_datos(self, widget):
        self.configuraciones_datos = QToolButton(widget)
        self.configuraciones_datos.setText('Otros ajustes')
        self.configuraciones_datos.setObjectName("button")  # nombre de enlace a css
        self.configuraciones_datos.setIcon(QIcon('src/views/static/icons/icono_estadisticas'))  # icono
        self.configuraciones_datos.setIconSize(QSize(self.height/11,self.height/11))
        self.configuraciones_datos.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # self.configuraciones_datos.clicked.connect(self.ConfiguracionesDatos)
        self.configuraciones_datos.setGeometry(self.width/5.7, self.height/7,
                                                self.width/3.6, self.height/3.3)
        self.configuraciones_datos.setVisible(False)
