from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#locals
from .funciones_eliminar import Funcion_eliminar
from src.controler.QLineClick import QLineEditClick

class Boton_eliminar(Funcion_eliminar):
    def boton_eliminar_username(self, widget):
        self.eliminar_username = QLineEditClick(widget)
        self.eliminar_username.setPlaceholderText("USUARIO")
        self.eliminar_username.setObjectName("input")  # nombre de enlace a css
        self.eliminar_username.setClearButtonEnabled(True)
        self.eliminar_username.setGeometry(164,237,290,70)
        self.eliminar_username.setMaxLength(40)
        self.eliminar_username.setVisible(False)

    def boton_eliminar_pass(self, widget):
        self.eliminar_pass = QLineEditClick(widget)
        self.eliminar_pass.setPlaceholderText("CONTRASEÑA")
        self.eliminar_pass.setObjectName("input")  # nombre de enlace a css
        self.eliminar_pass.setClearButtonEnabled(True)
        self.eliminar_pass.setGeometry(164, 341, 290, 70)
        self.eliminar_pass.setMaxLength(15)
        self.eliminar_pass.setVisible(False)
        self.eliminar_pass.setEchoMode(QLineEdit.Password)

    def boton_eliminar_eliminar(self, widget):
        self.eliminar_eliminar = QToolButton(widget)
        self.eliminar_eliminar.setText('ELIMINAR')
        self.eliminar_eliminar.setObjectName("button") #nombre de enlace a css
        self.eliminar_eliminar.setIcon(QIcon('src/views/static/icons/icono_entrar')) #icono
        self.eliminar_eliminar.setIconSize(QSize(60,60))
        self.eliminar_eliminar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.eliminar_eliminar.setGeometry(570, 230, 290, 180)
        self.eliminar_eliminar.clicked.connect(self.EliminarEliminar)
        self.eliminar_eliminar.setVisible(False)
