from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#locals
from .funciones_estadisticas import Funcion_estadisticas
from .graficas import *


class Boton_estadisticas(Funcion_estadisticas):
    def boton_estadisticas_ocupacion(self, widget):
        self.estadisticas_ocupacion = QToolButton(widget)
        self.estadisticas_ocupacion.setObjectName("NotButton")  # nombre de enlace a css
        self.estadisticas_ocupacion.setStyleSheet('font-size: 20px;font-family: Helvetica; color: white; ')
        self.estadisticas_ocupacion.setIcon(QIcon('src/views/static/icons/icono_capacidad'))  # icono
        self.estadisticas_ocupacion.setIconSize(QSize(50, 50))
        self.estadisticas_ocupacion.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.estadisticas_ocupacion.setGeometry(80, 100, 280, 120)
        self.estadisticas_ocupacion.setVisible(False)
        self.EstadisticasOcupacion()

    def boton_estadisticas_duracion(self, widget):
        self.estadisticas_duracion = QToolButton(widget)
        self.estadisticas_duracion.setObjectName("NotButton")  # nombre de enlace a css
        self.estadisticas_duracion.setStyleSheet('font-size: 20px;font-family: Helvetica; color: white; ')
        self.estadisticas_duracion.setIcon(QIcon('src/views/static/icons/icono_capacidad'))  # icono
        self.estadisticas_duracion.setIconSize(QSize(50, 50))
        self.estadisticas_duracion.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.estadisticas_duracion.setGeometry(80, 220, 280, 120)
        self.estadisticas_duracion.setVisible(False)
        self.EstadisticasDuracion()

    def boton_estadisticas_personasDia(self, widget):
        self.estadisticas_personasDia = QToolButton(widget)
        self.estadisticas_personasDia.setObjectName("NotButton")  # nombre de enlace a css
        self.estadisticas_personasDia.setStyleSheet('font-size: 20px;font-family: Helvetica; color: white; ')
        self.estadisticas_personasDia.setIcon(QIcon('src/views/static/icons/icono_capacidad'))  # icono
        self.estadisticas_personasDia.setIconSize(QSize(50, 50))
        self.estadisticas_personasDia.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.estadisticas_personasDia.setGeometry(80, 340, 280, 120)
        self.estadisticas_personasDia.setVisible(False)
        self.EstadisticasPersonasDia()

    def boton_estadisticas_cambiar_semana(self, widget):
        #semana adelante
        self.estadisticas_cambiar_semana_adelante = QToolButton(widget)
        self.estadisticas_cambiar_semana_adelante.setObjectName("button")  # nombre de enlace a css
        self.estadisticas_cambiar_semana_adelante.setStyleSheet('border-radius:4px;')
        self.estadisticas_cambiar_semana_adelante.setGeometry(470, 530,50, 30)
        self.estadisticas_cambiar_semana_adelante.setVisible(False)
        self.estadisticas_cambiar_semana_adelante.setText('<')
        self.estadisticas_cambiar_semana_adelante.clicked.connect(self.EstadisticasCambiarSemanaAdelante)

        #semana atras
        self.estadisticas_cambiar_semana_atras = QToolButton(widget)
        self.estadisticas_cambiar_semana_atras.setObjectName("button")  # nombre de enlace a css
        self.estadisticas_cambiar_semana_atras.setStyleSheet('border-radius:4px;')
        self.estadisticas_cambiar_semana_atras.setGeometry(870, 530,50, 30)
        self.estadisticas_cambiar_semana_atras.setVisible(False)
        self.estadisticas_cambiar_semana_atras.setText('>')
        self.estadisticas_cambiar_semana_atras.clicked.connect(self.EstadisticasCambiarSemanaAtras)

    def graficas_estadisticas(self):
        
        info = self.EstadisticasGetInfo()
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

    