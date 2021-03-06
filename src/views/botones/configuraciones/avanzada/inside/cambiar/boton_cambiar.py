from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#locals
from .funciones_cambiar import Funcion_cambiar
from src.controler.QLineClick import QLineEditClick

class Boton_cambiar(Funcion_cambiar):
    def text_cambiar_pass(self, widget):
        self.cambiar_user = QLineEditClick(widget)
        self.cambiar_user.setPlaceholderText("USUARIO")
        self.cambiar_user.setObjectName("input")  # nombre de enlace a css
        self.cambiar_user.setClearButtonEnabled(True)
        self.cambiar_user.setGeometry(self.width/4.5, self.height/2.7 , 
                                        self.width/6.1, self.height/12)
        
        
        
        

        self.cambiar_user.setMaxLength(15)
        self.cambiar_user.setVisible(False)
        self.cambiar_user.clicked.connect(self.CambiarUser)


        self.cambiar_pass = QLineEditClick(widget)
        self.cambiar_pass.setPlaceholderText("PASSWORD ANTERIOR")
        self.cambiar_pass.setObjectName("input")  # nombre de enlace a css
        self.cambiar_pass.setClearButtonEnabled(True)
        self.cambiar_pass.setGeometry(self.width/2.5, self.height/2.7  , 
                                        self.width/6.1, self.height/12)
        self.cambiar_pass.setMaxLength(40)
        self.cambiar_pass.setVisible(False)
        self.cambiar_pass.setEchoMode(QLineEdit.Password)
        self.cambiar_pass.clicked.connect(self.CambiarPass)


    def text_pass_new(self, widget):
        self.pass_new_0 = QLineEditClick(widget)
        self.pass_new_0.setPlaceholderText("CONTRASEÑA NUEVA")
        self.pass_new_0.setObjectName("input")  # nombre de enlace a css
        self.pass_new_0.setClearButtonEnabled(True)
        self.pass_new_0.setGeometry(self.width/4.5, self.height/2.7 +self.height/8.5, 
                                        self.width/6.1, self.height/12)
        self.pass_new_0.setMaxLength(15)
        self.pass_new_0.setVisible(False)
        self.pass_new_0.setEchoMode(QLineEdit.Password)
        self.pass_new_0.clicked.connect(self.PassNew0)


        self.pass_new_1 = QLineEditClick(widget)
        self.pass_new_1.setPlaceholderText("CONTRASEÑA NUEVA")
        self.pass_new_1.setObjectName("input")  # nombre de enlace a css
        self.pass_new_1.setClearButtonEnabled(True)
        self.pass_new_1.setGeometry(self.width/2.5, self.height/2.7 +self.height/8.5, 
                                        self.width/6.1, self.height/12)
        self.pass_new_1.setMaxLength(15)
        self.pass_new_1.setVisible(False)
        self.pass_new_1.setEchoMode(QLineEdit.Password)
        self.pass_new_1.clicked.connect(self.PassNew1)


    def boton_cambiar_cambiar(self, widget):
        self.cambiar_cambiar = QToolButton(widget)
        self.cambiar_cambiar.setText('CAMBIAR')
        self.cambiar_cambiar.setObjectName("button") #nombre de enlace a css
        self.cambiar_cambiar.setIcon(QIcon('src/views/static/icons/icono_password')) #icono
        self.cambiar_cambiar.setIconSize(QSize(self.height/20,self.height/20))
        self.cambiar_cambiar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.cambiar_cambiar.setGeometry(self.width/1.7, self.height/2.7, 
                                        self.width/6, self.height/4.9)
        self.cambiar_cambiar.clicked.connect(self.CambiarCambiar)
        self.cambiar_cambiar.setVisible(False)
