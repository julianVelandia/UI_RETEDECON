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
        self.eliminar_username.setGeometry(self.width/3.6, self.height/2.7, 
                                        self.width/4.2, self.height/12)
        self.eliminar_username.setMaxLength(40)
        self.eliminar_username.setVisible(False)
        self.eliminar_username.clicked.connect(self.EliminarUsername)


    def boton_eliminar_pass(self, widget):
        self.eliminar_pass = QLineEditClick(widget)
        self.eliminar_pass.setPlaceholderText("CONTRASEÑA")
        self.eliminar_pass.setObjectName("input")  # nombre de enlace a css
        self.eliminar_pass.setClearButtonEnabled(True)
        self.eliminar_pass.setGeometry(self.width/3.6, (self.height/2.7)+self.height/8.5, 
                                        self.width/4.2, self.height/12)
        self.eliminar_pass.setMaxLength(15)
        self.eliminar_pass.setVisible(False)
        self.eliminar_pass.setEchoMode(QLineEdit.Password)
        self.eliminar_pass.clicked.connect(self.EliminarPass)


    def boton_eliminar_eliminar(self, widget):
        self.eliminar_eliminar = QToolButton(widget)
        self.eliminar_eliminar.setText('ELIMINAR')
        self.eliminar_eliminar.setObjectName("button") #nombre de enlace a css
        self.eliminar_eliminar.setIcon(QIcon('src/views/static/icons/icono_entrar')) #icono
        self.eliminar_eliminar.setIconSize(QSize(self.height/20,self.height/20))
        self.eliminar_eliminar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.eliminar_eliminar.setGeometry(self.width/1.8, self.height/2.7, 
                                        self.width/6, self.height/4.9)
        self.eliminar_eliminar.clicked.connect(self.EliminarEliminar)
        self.eliminar_eliminar.setVisible(False)
