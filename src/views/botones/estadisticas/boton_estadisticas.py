from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#locals
from .funciones_estadisticas import Funcion_estadisticas
from .graficas import *


class Boton_estadisticas(Funcion_estadisticas):
    def boton_estadisticas_ocupacion(self, widget):
        self.estadisticas_ocupacion = QToolButton(widget)
        self.estadisticas_ocupacion.setObjectName("button")  # nombre de enlace a css
        self.estadisticas_ocupacion.setIcon(QIcon('src/views/static/icons/icono_capacidad'))  # icono
        self.estadisticas_ocupacion.setIconSize(QSize(60, 60))
        self.estadisticas_ocupacion.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.estadisticas_ocupacion.setGeometry(120, 120, 290, 140)
        self.estadisticas_ocupacion.setVisible(False)

    def graficas_estadisticas(self):
        
        info = self.get_info()
        #Barras
        self.estadisticas_bar_chart = PlotCanvas(self, width=5, height=4)
        self.estadisticas_bar_chart.move(450, 120)
        self.estadisticas_bar_chart.bar(info)
        self.estadisticas_bar_chart.setVisible(False)
        #Pie
        self.estadisticas_pie_chart = PlotCanvasP(self, width=5, height=4)
        self.estadisticas_pie_chart.move(450, 120)
        self.estadisticas_pie_chart.pie(info)
        self.estadisticas_pie_chart.setVisible(False)

    