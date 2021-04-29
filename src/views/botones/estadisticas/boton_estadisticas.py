from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# locals
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
        self.estadisticas_ocupacion.setGeometry(80, 130, 280, 120)
        self.estadisticas_ocupacion.setVisible(False)
        self.EstadisticasOcupacion()

    def boton_estadisticas_duracion(self, widget):
        self.estadisticas_duracion = QToolButton(widget)
        self.estadisticas_duracion.setObjectName("NotButton")  # nombre de enlace a css
        self.estadisticas_duracion.setStyleSheet('font-size: 20px;font-family: Helvetica; color: white; ')
        self.estadisticas_duracion.setIcon(QIcon('src/views/static/icons/icono_tiempo'))  # icono
        self.estadisticas_duracion.setIconSize(QSize(50, 50))
        self.estadisticas_duracion.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.estadisticas_duracion.setGeometry(80, 240, 280, 120)
        self.estadisticas_duracion.setVisible(False)
        self.EstadisticasDuracion()

    def boton_estadisticas_personasDia(self, widget):
        self.estadisticas_personasDia = QToolButton(widget)
        self.estadisticas_personasDia.setObjectName("NotButton")  # nombre de enlace a css
        self.estadisticas_personasDia.setStyleSheet('font-size: 20px;font-family: Helvetica; color: white; ')
        self.estadisticas_personasDia.setIcon(QIcon('src/views/static/icons/icono_capacidad'))  # icono
        self.estadisticas_personasDia.setIconSize(QSize(50, 50))
        self.estadisticas_personasDia.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.estadisticas_personasDia.setGeometry(80, 375, 280, 120)
        self.estadisticas_personasDia.setVisible(False)
        self.EstadisticasPersonasDia()

    def boton_estadisticas_cambiar_semana(self, widget):
        # semana adelante
        self.estadisticas_cambiar_semana_adelante = QToolButton(widget)
        self.estadisticas_cambiar_semana_adelante.setObjectName("button")  # nombre de enlace a css
        self.estadisticas_cambiar_semana_adelante.setStyleSheet('border-radius:4px;')
        self.estadisticas_cambiar_semana_adelante.setGeometry(470, 530, 50, 30)
        self.estadisticas_cambiar_semana_adelante.setVisible(False)
        self.estadisticas_cambiar_semana_adelante.setText('<')
        self.estadisticas_cambiar_semana_adelante.clicked.connect(self.EstadisticasCambiarSemanaAdelante)

        # semana atras
        self.estadisticas_cambiar_semana_atras = QToolButton(widget)
        self.estadisticas_cambiar_semana_atras.setObjectName("button")  # nombre de enlace a css
        self.estadisticas_cambiar_semana_atras.setStyleSheet('border-radius:4px;')
        self.estadisticas_cambiar_semana_atras.setGeometry(870, 530, 50, 30)
        self.estadisticas_cambiar_semana_atras.setVisible(False)
        self.estadisticas_cambiar_semana_atras.setText('>')
        self.estadisticas_cambiar_semana_atras.clicked.connect(self.EstadisticasCambiarSemanaAtras)

    def boton_barras(self, widget):
        self.estadisticas_barras = QToolButton(widget)
        # self.estadisticas_barras.setText('GRÁFICO DE BARRAS')
        self.estadisticas_barras.setObjectName("small")  # nombre de enlace a css
        self.estadisticas_barras.setIcon(QIcon('src/views/static/icons/icono_barras'))  # icono
        self.estadisticas_barras.setIconSize(QSize(20, 20))
        self.estadisticas_barras.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.estadisticas_barras.clicked.connect(self.barras)
        self.estadisticas_barras.clicked.connect(self.Estadisticas)
        self.estadisticas_barras.setGeometry(610, 527, 36, 36)
        self.estadisticas_barras.setVisible(False)
        self.estadisticas_barras.setStyleSheet("background-color: #A2A2A2;")

    def boton_torta(self, widget):
        self.estadisticas_torta = QToolButton(widget)
        self.estadisticas_torta.setObjectName("small")  # nombre de enlace a css
        self.estadisticas_torta.setIcon(QIcon('src/views/static/icons/icono_pie'))  # icono
        self.estadisticas_torta.setIconSize(QSize(20, 20))
        self.estadisticas_torta.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.estadisticas_torta.clicked.connect(self.torta)
        self.estadisticas_torta.clicked.connect(self.Estadisticas)
        self.estadisticas_torta.setGeometry(740, 527, 36, 36)
        self.estadisticas_torta.setVisible(False)
        # self.estadisticas_torta.setStyleSheet("background-color: #A2A2A2;")

    def graficas_estadisticas(self):
        info = self.EstadisticasGetInfo()
        # Barras
        self.estadisticas_bar_chart = PlotCanvas(self, width=5, height=4)
        self.estadisticas_bar_chart.move(450, 120)
        self.estadisticas_bar_chart.bara(info, False)
        self.estadisticas_bar_chart.setVisible(False)
        # Pie
        self.estadisticas_pie_chart = PlotCanvasP(self, width=5, height=4)
        self.estadisticas_pie_chart.move(450, 120)
        self.estadisticas_pie_chart.pies(info, False)
        self.estadisticas_pie_chart.setVisible(False)
