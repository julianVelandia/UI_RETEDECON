from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from .funciones import Funciones

class Boton(Funciones):
    def boton_ingresar(self, widget):
        self.ingresar = QToolButton(widget)
        self.ingresar.setText('INGRESO MANUAL')
        self.ingresar.setObjectName("button") #nombre de enlace a css
        self.ingresar.setIcon(QIcon('../../static/icons/icono_entrar')) #icono
        self.ingresar.setIconSize(QSize(60,60))
        self.ingresar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ingresar.clicked.connect(self.Ingresar)
        self.ingresar.setVisible(False)



    def boton_home(self, widget):
        self.label_img_esquina = QToolButton(widget)
        self.label_img_esquina.setGeometry(30,5,250,60)        
        self.label_img_esquina.setObjectName("button_home") #nombre de enlace a css
        self.label_img_esquina.clicked.connect(self.HomeWindow)