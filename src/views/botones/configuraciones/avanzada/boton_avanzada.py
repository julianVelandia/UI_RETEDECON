from src.views.botones.configuraciones.avanzada.inside.boton_inside import Boton_inside
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#locals
from .funciones_avanzada import Funcion_avanzada
from .inside.boton_inside import Boton_inside
from src.controler.QLineClick import QLineEditClick

class Boton_avanzada(Funcion_avanzada, Boton_inside):
    def texto_avanzada_user(self, widget):
        self.avanzada_user = QLineEditClick(widget)
        self.avanzada_user.setPlaceholderText("USUARIO")
        self.avanzada_user.setObjectName("input") #nombre de enlace a css
        self.avanzada_user.setClearButtonEnabled(True)
        self.avanzada_user.setGeometry(self.width/3.6, self.height/2.7, 
                                        self.width/4.2, self.height/12)
               
        self.avanzada_user.setMaxLength(40)
        self.avanzada_user.setVisible(False)
        self.avanzada_user.clicked.connect(self.AvanzadaUserTeclado)

    def texto_avanzada_pass(self, widget):
        self.avanzada_pass = QLineEditClick(widget)
        self.avanzada_pass.setPlaceholderText("CONTRASEÑA")
        self.avanzada_pass.setObjectName("input")  # nombre de enlace a css
        self.avanzada_pass.setClearButtonEnabled(True)
        self.avanzada_pass.setGeometry(self.width/3.6, (self.height/2.7)+self.height/8.5, 
                                        self.width/4.2, self.height/12)
        self.avanzada_pass.setMaxLength(15)
        self.avanzada_pass.setVisible(False)
        self.avanzada_pass.setEchoMode(QLineEdit.Password)
        self.avanzada_pass.clicked.connect(self.AvanzadaPassTeclado)

    def boton_avanzada_ingresar(self, widget):
        self.avanzada_ingresar = QToolButton(widget)
        self.avanzada_ingresar.setText('ACCEDER')
        self.avanzada_ingresar.setObjectName("button")  # nombre de enlace a css
        self.avanzada_ingresar.setIcon(QIcon('src/views/static/icons/icono_entrar'))  # icono
        self.avanzada_ingresar.setIconSize(QSize(60, 60))
        self.avanzada_ingresar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.avanzada_ingresar.clicked.connect(self.AvanzadaIngresar)
        self.avanzada_ingresar.setGeometry(self.width/1.8, self.height/2.7, 
                                        self.width/6, self.height/4.9)
        self.avanzada_ingresar.setVisible(False)