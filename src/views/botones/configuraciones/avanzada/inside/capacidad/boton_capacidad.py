from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#locals
from .funciones_capacidad import Funcion_capacidad
from src.controler.QLineClick import QLineEditClick

class Boton_capacidad(Funcion_capacidad):
    def text_capacidad_newcapacidad(self, widget):
        self.capacidad_newcapacidad = QLineEditClick(widget)
        self.capacidad_newcapacidad.setPlaceholderText("CAPACIDAD")
        self.capacidad_newcapacidad.setObjectName("input") #nombre de enlace a css
        self.capacidad_newcapacidad.setClearButtonEnabled(True)
        self.capacidad_newcapacidad.setGeometry(164,237,290,70)
        self.capacidad_newcapacidad.setMaxLength(5)
        self.capacidad_newcapacidad.setVisible(False)

    def boton_capacidad_setnew(self, widget):
        self.capacidad_setnew = QToolButton(self.centralWidget)
        self.capacidad_setnew.setText('CAMBIAR CAPACIDAD\nMÁXIMA')
        self.capacidad_setnew.setObjectName("button")  # nombre de enlace a css
        self.capacidad_setnew.setIcon(QIcon('src/views/static/icons/icono_capacidad'))  # icono
        self.capacidad_setnew.setIconSize(QSize(60, 60))
        self.capacidad_setnew.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.capacidad_setnew.clicked.connect(self.CapacidadSetnew)
        self.capacidad_setnew.setGeometry(570, 230, 290, 231)
        self.capacidad_setnew.setVisible(False)