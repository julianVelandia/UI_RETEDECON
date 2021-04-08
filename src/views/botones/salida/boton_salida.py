from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#locals
from .funciones_salida import Funcion_salida
from src.controler.QLineClick import QLineEditClick


class Boton_salida(Funcion_salida):
    def texto_salida_nombre_out(self, widget):
        self.salida_nombre = QLineEditClick(widget)
        self.salida_nombre.setPlaceholderText("NOMBRE")
        self.salida_nombre.setObjectName("input")  # nombre de enlace a css
        self.salida_nombre.setClearButtonEnabled(True)
        self.salida_nombre.setGeometry(164, 237, 290, 70)
        self.salida_nombre.setMaxLength(40)

    def texto_salida_cedula_out(self, widget):

        self.salida_cedula = QLineEditClick(widget)
        self.salida_cedula.setPlaceholderText("CEDULA")
        self.salida_cedula.setObjectName("input")  # nombre de enlace a css
        self.salida_cedula.setClearButtonEnabled(True)
        self.salida_cedula.setGeometry(164, 341, 290, 70)
        self.salida_cedula.setMaxLength(15)

    def boton_salida_salida(self,widget):
        self.salida_salida = QToolButton(widget)
        self.salida_salida.setText('RETIRAR')
        self.salida_salida.setObjectName("button") #nombre de enlace a css
        self.salida_salida.setIcon(QIcon('src/views/static/icons/icono_salir')) #icono
        self.salida_salida.setIconSize(QSize(60,60))
        self.salida_salida.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.salida_salida.clicked.connect(self.SalidaSalida)
        self.salida_salida.setGeometry(570, 237, 290, 176.3)

        self.salida_nombre.setVisible(False)
        self.salida_cedula.setVisible(False)
        self.salida_salida.setVisible(False)