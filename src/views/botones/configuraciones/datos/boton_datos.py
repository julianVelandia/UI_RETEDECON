from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#locals
from .funciones_datos import Funcion_datos
from src.controler.QLineClick import QLineEditClick

class Boton_datos(Funcion_datos):
    def boton_datos_barras(self, widget):
        self.datos_barras = QToolButton(widget)
        self.datos_barras.setText('GRÁFICO DE BARRAS')
        self.datos_barras.setObjectName("button")  # nombre de enlace a css
        self.datos_barras.setIcon(QIcon('src/views/static/icons/icono_barras'))  # icono
        self.datos_barras.setIconSize(QSize(60, 60))
        self.datos_barras.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.datos_barras.clicked.connect(self.DatosBarras)
        self.datos_barras.setGeometry(534,230, 290, 180)
        self.datos_barras.setVisible(False)
        self.datos_barras.setStyleSheet("background-color: #A2A2A2;")

    def boton_datos_pie(self, widget):
        self.datos_pie = QToolButton(widget)
        self.datos_pie.setText('GRÁFICO DE TORTA')
        self.datos_pie.setObjectName("button")  # nombre de enlace a css
        self.datos_pie.setIcon(QIcon('src/views/static/icons/icono_pie'))  # icono
        self.datos_pie.setIconSize(QSize(60, 60))
        self.datos_pie.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.datos_pie.clicked.connect(self.DatosPie)
        self.datos_pie.setGeometry(200, 230, 290, 180)
        self.datos_pie.setVisible(False)
        self.datos_pie.setStyleSheet("background-color: none;")