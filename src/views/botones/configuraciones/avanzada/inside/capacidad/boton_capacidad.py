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
        self.capacidad_newcapacidad.setGeometry(self.width/3.6, self.height/2.7, 
                                        self.width/4.2, self.height/12)

        self.capacidad_newcapacidad.setMaxLength(5)
        self.capacidad_newcapacidad.setVisible(False)
        self.capacidad_newcapacidad.clicked.connect(self.CapacidadNewCapacidad)


    def boton_capacidad_setnew(self, widget):
        self.capacidad_setnew = QToolButton(widget)
        self.capacidad_setnew.setText('CAMBIAR CAPACIDAD\nMÁXIMA')
        self.capacidad_setnew.setObjectName("button")  # nombre de enlace a css
        self.capacidad_setnew.setIcon(QIcon('src/views/static/icons/icono_capacidad'))  # icono
        self.capacidad_setnew.setIconSize(QSize(self.height/11, self.height/11))
        self.capacidad_setnew.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.capacidad_setnew.clicked.connect(self.CapacidadSetnew)
        self.capacidad_setnew.setGeometry(self.width/1.8, self.height/2.7, 
                                        self.width/6, self.height/4.9)
        self.capacidad_setnew.setVisible(False)
