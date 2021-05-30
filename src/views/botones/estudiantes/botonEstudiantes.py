from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


from .funcionesEstudiantes import FuncionesEstudiantes

from screeninfo import get_monitors


class BotonEstudiantes(FuncionesEstudiantes):



    def textosEstado(self, widget):
       
        self.width = get_monitors()[0].width
        self.height = get_monitors()[0].height
        self.widthGif = 400
        self.heightGif = 400

        self.texto_informativo = QToolButton(widget)

        self.texto_informativo.setIcon(QIcon('src/views/static/icons/icono_info'))
        self.texto_informativo.setIconSize(QSize(60,60))
        self.texto_informativo.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.texto_informativo.setText('')
        self.texto_informativo.setObjectName("Texto")  # nombre de enlace a css
        self.texto_informativo.setGeometry((self.width/4.5), (self.height/2), 
                                            self.widthGif, self.heightGif)
        self.texto_informativo.setVisible(False)


        

    def botonesPrueba(self, widget):

        width = get_monitors()[0].width

        self.botonPrueba1 = QToolButton(widget)
        self.botonPrueba1.setText('Si')
        self.botonPrueba1.setObjectName("small")  # nombre de enlace a css
        self.botonPrueba1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.botonPrueba1.clicked.connect(self.si)
        self.botonPrueba1.setGeometry((width/2)-90, 190, 60, 60)
        self.botonPrueba1.setVisible(False)

        self.botonPrueba2 = QToolButton(widget)
        self.botonPrueba2.setText('No')
        self.botonPrueba2.setObjectName("small")  # nombre de enlace a css
        self.botonPrueba2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.botonPrueba2.clicked.connect(self.no)
        self.botonPrueba2.setGeometry((width/2)+30, 190, 60, 60)
        self.botonPrueba2.setVisible(False)

    
    def giftEstudiantes(self, widget):
        self.widthGif = 400
        self.heightGif = 400

        self.giflabel = QLabel(widget)
        self.movie0 = QMovie('src/views/static/gif/s0.gif')  # Gif paso 1
        self.giflabel.setGeometry((self.width/1.5),(self.height/2),
                                    self.widthGif, self.heightGif)
        self.giflabel.setMovie(self.movie0)
        self.giflabel.setVisible(False)



    def labelEsquina(self, widget):
        self.label_img_esquina = QToolButton(widget)
        self.label_img_esquina.setGeometry(30,5,250,60)        
        self.label_img_esquina.setObjectName("button_home") #nombre de enlace a css
        #self.label_img_esquina.clicked.connect(self.HomeWindow)
        self.label_img_esquina.setVisible(True)