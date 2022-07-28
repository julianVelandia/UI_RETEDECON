from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from .funcionesEstudiantes import FuncionesEstudiantes

from screeninfo import get_monitors


class BotonEstudiantes(FuncionesEstudiantes):
    width = get_monitors()[1].width
    height = get_monitors()[1].height
    widthGif = width / 5
    heightGif = width / 5

    def textosEstado(self, widget):
        # self.width = get_monitors()[0].width
        # self.height = get_monitors()[0].height

        self.texto_informativo = QToolButton(widget)

        self.texto_informativo.setIcon(QIcon('src/views/static/icons/icono_info'))
        self.texto_informativo.setIconSize(QSize(60, 60))
        self.texto_informativo.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.texto_informativo.setText('')
        self.texto_informativo.setObjectName("Texto")  # nombre de enlace a css
        self.texto_informativo.setGeometry((self.width / 4), (self.height / 1.5),
                                           self.width / 2, self.height / 3)
        self.texto_informativo.setVisible(False)

        self.texto_temporal = QToolButton(widget)

        self.texto_temporal.setIcon(QIcon('src/views/static/icons/icono_info'))
        self.texto_temporal.setIconSize(QSize(60, 60))
        self.texto_temporal.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.texto_temporal.setText('')
        self.texto_temporal.setObjectName("Texto")  # nombre de enlace a css
        self.texto_temporal.setGeometry((self.width / 4), (self.height / 1.5),
                                        self.width / 2, self.height / 3)
        self.texto_temporal.setVisible(False)

    def botonesPrueba(self, widget):
        self.botonPrueba1 = QToolButton(widget)
        self.botonPrueba1.setText('Si')
        self.botonPrueba1.setObjectName("small")  # nombre de enlace a css
        self.botonPrueba1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.botonPrueba1.clicked.connect(self.si)
        self.botonPrueba1.setGeometry((self.width / 2) - self.width / 10, self.height / 10,
                                      self.height / 8, self.height / 8)
        self.botonPrueba1.setVisible(False)

        self.botonPrueba2 = QToolButton(widget)
        self.botonPrueba2.setText('No')
        self.botonPrueba2.setObjectName("small")  # nombre de enlace a css
        self.botonPrueba2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.botonPrueba2.clicked.connect(self.no)
        self.botonPrueba2.setGeometry((self.width / 2) + self.width / 10, self.height / 10,
                                      self.height / 8, self.height / 8)
        self.botonPrueba2.setVisible(False)

    def giftEstudiantes(self, widget):
        self.giflabel = QLabel(widget)
        self.movie0 = QMovie('src/views/static/gif/s0.gif')  # Gif paso 1
        self.giflabel.setGeometry((self.width / 4), (self.height / 4),
                                  self.widthGif, self.heightGif)
        self.giflabel.setMovie(self.movie0)
        self.giflabel.setVisible(False)

    def labelEsquina(self, widget):
        self.label_img_esquina = QToolButton(widget)
        self.label_img_esquina.setGeometry(self.width / 28, self.height / 30,
                                           self.width / 6, self.height / 10)
        self.label_img_esquina.setObjectName("button_home")  # nombre de enlace a css
        self.label_img_esquina.setVisible(True)

    def labelsCamara(self, widget):
        self.labelMatrix = []
        for i in range(32):
            row = []
            for j in range(32):
                label = QLabel(widget)
                label.setStyleSheet("background-color: rgb(28, 76, 150)")
                label.setGeometry(self.width/4+10*i, 250+10*j, 10, 10)
                label.setVisible(False)
                row.append(label)
            self.labelMatrix.append(row)