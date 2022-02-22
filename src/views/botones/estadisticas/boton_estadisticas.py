from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# locals
from src.views.botones.estadisticas.funciones_estadisticas import Funcion_estadisticas
from src.views.botones.estadisticas.graficas import *


from screeninfo import get_monitors

class Boton_estadisticas(Funcion_estadisticas):

    width = get_monitors()[0].width
    height = get_monitors()[0].height

    def boton_estadisticas_ocupacion(self, widget):
        self.estadisticas_ocupacion = QToolButton(widget)
        self.estadisticas_ocupacion.setObjectName("NotButton")  # nombre de enlace a css
        self.estadisticas_ocupacion.setStyleSheet('font-size: 20px;font-family: Helvetica; color: white; ')
        self.estadisticas_ocupacion.setIcon(QIcon('src/views/static/icons/icono_capacidad'))  # icono
        self.estadisticas_ocupacion.setIconSize(QSize(self.height/11, self.height/11))
        self.estadisticas_ocupacion.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.estadisticas_ocupacion.setGeometry(self.width/20, self.height/7, 
                                                self.width/8, self.height/6)
        self.estadisticas_ocupacion.setVisible(False)
        self.EstadisticasOcupacion()

    def boton_estadisticas_duracion(self, widget):
        self.estadisticas_duracion = QToolButton(widget)
        self.estadisticas_duracion.setObjectName("NotButton")  # nombre de enlace a css
        self.estadisticas_duracion.setStyleSheet('font-size: 20px;font-family: Helvetica; color: white; ')
        self.estadisticas_duracion.setIcon(QIcon('src/views/static/icons/icono_tiempo'))  # icono
        self.estadisticas_duracion.setIconSize(QSize(self.height/11, self.height/11))
        self.estadisticas_duracion.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.estadisticas_duracion.setGeometry(self.width/20, self.height/2.5,
                                                self.width/6, self.height/5.3)
        self.estadisticas_duracion.setVisible(False)
        self.EstadisticasDuracion()

    def boton_estadisticas_personasDia(self, widget):
        self.estadisticas_personasDia = QToolButton(widget)
        self.estadisticas_personasDia.setObjectName("NotButton")  # nombre de enlace a css
        self.estadisticas_personasDia.setStyleSheet('font-size: 20px;font-family: Helvetica; color: white; ')
        self.estadisticas_personasDia.setIcon(QIcon('src/views/static/icons/icono_capacidad'))  # icono
        self.estadisticas_personasDia.setIconSize(QSize(self.height/11, self.height/11))
        self.estadisticas_personasDia.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.estadisticas_personasDia.setGeometry(self.width/20, self.height/1.5, 
                                                self.width/6.5, self.height/4.5)
        self.estadisticas_personasDia.setVisible(False)
        self.EstadisticasPersonasDia()

    def boton_estadisticas_cambiar_semana(self, widget):
        # semana adelante
        self.estadisticas_cambiar_semana_adelante = QToolButton(widget)
        self.estadisticas_cambiar_semana_adelante.setObjectName("button")  # nombre de enlace a css
        self.estadisticas_cambiar_semana_adelante.setStyleSheet('border-radius:4px;')
        self.estadisticas_cambiar_semana_adelante.setGeometry(self.width/4, self.height/1.4, 
                                                                self.width/30, self.height/25)
        self.estadisticas_cambiar_semana_adelante.setVisible(False)
        self.estadisticas_cambiar_semana_adelante.setText('<')
        self.estadisticas_cambiar_semana_adelante.clicked.connect(self.EstadisticasCambiarSemanaAdelante)

        # semana atras
        self.estadisticas_cambiar_semana_atras = QToolButton(widget)
        self.estadisticas_cambiar_semana_atras.setObjectName("button")  # nombre de enlace a css
        self.estadisticas_cambiar_semana_atras.setStyleSheet('border-radius:4px;')
        self.estadisticas_cambiar_semana_atras.setGeometry(self.width/1.4, self.height/1.4, 
                                                                self.width/30, self.height/25)
        self.estadisticas_cambiar_semana_atras.setVisible(False)
        self.estadisticas_cambiar_semana_atras.setText('>')
        self.estadisticas_cambiar_semana_atras.clicked.connect(self.EstadisticasCambiarSemanaAtras)

    def graficas_estadisticas(self):
        info = self.EstadisticasGetInfo()
        # Barras
        self.estadisticas_bar_chart = PlotCanvas(self, width=self.width/195, height=self.height/190)
        self.estadisticas_bar_chart.move(self.width/4, self.height/8)
        self.estadisticas_bar_chart.bara(info, False)
        self.estadisticas_bar_chart.setVisible(False)