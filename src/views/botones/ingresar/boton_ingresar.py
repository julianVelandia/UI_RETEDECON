from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#locals
from .funciones_ingresar import Funcion_ingresar
from src.controler.QLineClick import QLineEditClick


class Boton_ingresar(Funcion_ingresar):
    def texto_ingresar_nombre(self, widget):
        self.ingresar_nombre = QLineEditClick(widget)
        self.ingresar_nombre.setPlaceholderText("NOMBRE")
        self.ingresar_nombre.setObjectName("input")  # nombre de enlace a css
        self.ingresar_nombre.setClearButtonEnabled(True)
        self.ingresar_nombre.setGeometry(164, 230, 290, 65)
        self.ingresar_nombre.setMaxLength(40)

    def texto_ingresar_cedula(self, widget):
        self.ingresar_cedula = QLineEditClick(widget)
        self.ingresar_cedula.setPlaceholderText("CEDULA")
        self.ingresar_cedula.setObjectName("input") #nombre de enlace a css
        self.ingresar_cedula.setClearButtonEnabled(True)
        self.ingresar_cedula.setGeometry(164,313,290,65)
        self.ingresar_cedula.setMaxLength(15)

    def texto_ingresar_temp(self, widget):
        self.ingresar_temp = QLineEditClick(widget)
        self.ingresar_temp.setPlaceholderText("TEMP")
        self.ingresar_temp.setObjectName("input") #nombre de enlace a css
        self.ingresar_temp.setClearButtonEnabled(True)
        self.ingresar_temp.setGeometry(164,396,290,65)
        self.ingresar_temp.setMaxLength(5)

    def boton_ingresar_ingresar(self, widget):
        self.ingresar_ingresar = QToolButton(widget)
        self.ingresar_ingresar.setText('INGRESAR')
        self.ingresar_ingresar.setObjectName("button") #nombre de enlace a css
        self.ingresar_ingresar.setIcon(QIcon('src/views/static/icons/icono_entrar')) #icono
        self.ingresar_ingresar.setIconSize(QSize(60,60))
        self.ingresar_ingresar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        #self.ingresar_ingresar.clicked.connect(self.Escribir)
        self.ingresar_ingresar.setGeometry(570, 230, 290, 231)

        self.ingresar_nombre.setVisible(False)
        self.ingresar_cedula.setVisible(False)
        self.ingresar_temp.setVisible(False)
        self.ingresar_ingresar.setVisible(False)