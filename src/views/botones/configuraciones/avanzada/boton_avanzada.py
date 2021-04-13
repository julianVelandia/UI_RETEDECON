from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#locals
from .funciones_avanzada import Funcion_avanzada
from src.controler.QLineClick import QLineEditClick


class Boton_avanzada(Funcion_avanzada):
    def texto_avanzada_user(self, widget):

        self.avanzada_user = QLineEditClick(widget)
        self.avanzada_user.setPlaceholderText("USUARIO")
        self.avanzada_user.setObjectName("input") #nombre de enlace a css
        self.avanzada_user.setClearButtonEnabled(True)
        self.avanzada_user.setGeometry(164,237,290,70)
        self.avanzada_user.setMaxLength(40)
        self.avanzada_user.setVisible(False)
        self.avanzada_user.clicked.connect(self.AvanzadaUserTeclado)


    def texto_avanzada_pass(self, widget):
        self.avanzada_pass = QLineEditClick(widget)
        self.avanzada_pass.setPlaceholderText("CONTRASEÑA")
        self.avanzada_pass.setObjectName("input")  # nombre de enlace a css
        self.avanzada_pass.setClearButtonEnabled(True)
        self.avanzada_pass.setGeometry(164, 341, 290, 70)
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
        self.avanzada_ingresar.setGeometry(570, 230, 290, 180)

        self.avanzada_ingresar.setVisible(False)
        self.avanzada_user.setVisible(False)
        self.avanzada_pass.setVisible(False)