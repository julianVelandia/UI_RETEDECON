from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#locals
from .funciones_ingresar import Funcion_ingresar
from src.controler.QLineClick import QLineEditClick
from screeninfo import get_monitors


class Boton_ingresar(Funcion_ingresar):
    width = get_monitors()[0].width
    height = get_monitors()[0].height

    def texto_ingresar_nombre(self, widget):
        self.ingresar_nombre = QLineEditClick(widget)
        self.ingresar_nombre.setPlaceholderText("NOMBRE")
        self.ingresar_nombre.setObjectName("input")  # nombre de enlace a css
        self.ingresar_nombre.setClearButtonEnabled(False)
        self.ingresar_nombre.setGeometry(self.width/3.6, self.height/2.7, 
                                        self.width/4.2, self.height/12)
        self.ingresar_nombre.setMaxLength(40)
        self.ingresar_nombre.clicked.connect(self.Ingresar_desplegar_teclado)

    def texto_ingresar_cedula(self, widget):
        self.ingresar_cedula = QLineEditClick(widget)
        self.ingresar_cedula.setPlaceholderText("CEDULA")
        self.ingresar_cedula.setObjectName("input") #nombre de enlace a css
        self.ingresar_cedula.setClearButtonEnabled(False)
        self.ingresar_cedula.setGeometry(self.width/3.6, (self.height/2.7)+self.height/8.5, 
                                        self.width/7, self.height/12)
        self.ingresar_cedula.setMaxLength(15)
        self.ingresar_cedula.clicked.connect(self.Ingresar_desplegar_teclado_numerico_cedula)

    def texto_ingresar_temp(self, widget):
        self.ingresar_temp = QLineEditClick(widget)
        self.ingresar_temp.setPlaceholderText("TEMP")
        self.ingresar_temp.setObjectName("input") #nombre de enlace a css
        self.ingresar_temp.setClearButtonEnabled(False)
        self.ingresar_temp.setGeometry((self.width/3.6) + (self.width/6), (self.height/2.7)+self.height/8.5, 
                                        self.width/14, self.height/12)
        self.ingresar_temp.setMaxLength(5)
        self.ingresar_temp.clicked.connect(self.Ingresar_desplegar_teclado_numerico_temp)

    def boton_ingresar_ingresar(self, widget):
        self.ingresar_ingresar = QToolButton(widget)
        self.ingresar_ingresar.setText('INGRESAR')
        self.ingresar_ingresar.setObjectName("button") #nombre de enlace a css
        self.ingresar_ingresar.setIcon(QIcon('src/views/static/icons/icono_entrar')) #icono
        self.ingresar_ingresar.setIconSize(QSize(40,40))
        self.ingresar_ingresar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ingresar_ingresar.clicked.connect(self.IngresarIngresar)
        self.ingresar_ingresar.setGeometry(self.width/1.8, self.height/2.7, 
                                        self.width/6, self.height/4.9)
        self.ingresar_nombre.setVisible(False)
        self.ingresar_cedula.setVisible(False)
        self.ingresar_temp.setVisible(False)
        self.ingresar_ingresar.setVisible(False)