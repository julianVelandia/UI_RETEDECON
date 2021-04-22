from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#locals
from .funciones_enviar import Funcion_enviar
from src.controler.QLineClick import QLineEditClick

class Boton_enviar(Funcion_enviar):
    def text_enviar(self, widget):
        self.enviar_newenviar = QLineEditClick(widget)
        self.enviar_newenviar.setPlaceholderText("Correo:")
        self.enviar_newenviar.setObjectName("input") #nombre de enlace a css
        self.enviar_newenviar.setClearButtonEnabled(True)
        self.enviar_newenviar.setGeometry(164,237,290,70)
        # self.enviar_newenviar.setMaxLength(5)
        self.enviar_newenviar.setVisible(False)

    def boton_enviar_setnew(self, widget):
        self.enviar_setnew = QToolButton(widget)
        self.enviar_setnew.setText('ENVIAR DATOS')
        self.enviar_setnew.setObjectName("button")  # nombre de enlace a css
        self.enviar_setnew.setIcon(QIcon('src/views/static/icons/icono_config_datos'))  # icono
        self.enviar_setnew.setIconSize(QSize(60, 60))
        self.enviar_setnew.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.enviar_setnew.clicked.connect(self.EnviarSetnew)
        self.enviar_setnew.setGeometry(570, 230, 290, 231)
        self.enviar_setnew.setVisible(False)