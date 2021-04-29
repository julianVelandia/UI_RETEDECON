from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#locals
from .funciones_agregar import Funcion_agregar
from src.controler.QLineClick import QLineEditClick

class Boton_agregar(Funcion_agregar):
    def boton_agregar_username(self, widget):
        self.agregar_username = QLineEditClick(widget)
        self.agregar_username.setPlaceholderText("USUARIO")
        self.agregar_username.setObjectName("input")  # nombre de enlace a css
        self.agregar_username.setClearButtonEnabled(True)
        self.agregar_username.setGeometry(164,237,290,70)
        self.agregar_username.setMaxLength(40)
        self.agregar_username.setVisible(False)
        self.agregar_username.clicked.connect(self.AgregarUsername)


    def boton_agregar_pass(self, widget):
        self.agregar_pass = QLineEditClick(widget)
        self.agregar_pass.setPlaceholderText("CONTRASEÑA")
        self.agregar_pass.setObjectName("input")  # nombre de enlace a css
        self.agregar_pass.setClearButtonEnabled(True)
        self.agregar_pass.setGeometry(164, 341, 290, 70)
        self.agregar_pass.setMaxLength(15)
        self.agregar_pass.setVisible(False)
        self.agregar_pass.setEchoMode(QLineEdit.Password)
        self.agregar_pass.clicked.connect(self.AgregarPass)


    def boton_agregar_agregar(self, widget):
        self.agregar_agregar = QToolButton(widget)
        self.agregar_agregar.setText('REGISTRAR')
        self.agregar_agregar.setObjectName("button") #nombre de enlace a css
        self.agregar_agregar.setIcon(QIcon('src/views/static/icons/icono_entrar')) #icono
        self.agregar_agregar.setIconSize(QSize(60,60))
        self.agregar_agregar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.agregar_agregar.setGeometry(570, 230, 290, 180)
        self.agregar_agregar.clicked.connect(self.AgregarAgregar)
        self.agregar_agregar.setVisible(False)