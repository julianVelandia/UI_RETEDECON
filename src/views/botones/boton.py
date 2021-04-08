from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from .botones.funciones import Funciones

class Boton(Funciones):
    def boton_ingresar(self, widget, funcion):
        self.ingresar = QToolButton(widget)
        self.ingresar.setText('INGRESO MANUAL')
        self.ingresar.setObjectName("button") #nombre de enlace a css
        self.ingresar.setIcon(QIcon('../../static/icons/icono_entrar')) #icono
        self.ingresar.setIconSize(QSize(60,60))
        self.ingresar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ingresar.clicked.connect(funcion)


    def boton_home(self, widget, funcion):
        self.label_img_esquina = QToolButton(widget)
        self.label_img_esquina.setGeometry(30,5,250,60)        
        self.label_img_esquina.setObjectName("button_home") #nombre de enlace a css
        self.label_img_esquina.clicked.connect(funcion)