from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


from .funcionesEstudiantes import FuncionesEstudiantes

from screeninfo import get_monitors


class BotonEstudiantes(FuncionesEstudiantes):



    def textosEstado(self, widget):
       
        width = get_monitors()[0].width
        print(width)
        height = get_monitors()[0].height

        self.textoIngreso = QToolButton(widget)
        self.textoIngreso.setText('El usuario fue ingresado \n con éxito')
        self.textoIngreso.setObjectName("button")  # nombre de enlace a css
        self.textoIngreso.setGeometry((width/2)-(310/2), 300, 310, 100)
        self.textoIngreso.setVisible(False)



        self.usuarioExiste = QToolButton(widget)
        self.usuarioExiste.setObjectName("button")  # nombre de enlace a css
        self.usuarioExiste.setText("El usuario ya está adentro")
        self.usuarioExiste.setVisible(False)
        self.usuarioExiste.setGeometry((width/2)-(310/2), 300, 310, 100)


        self.usuarioRetirado = QLabel(widget)
        self.usuarioRetirado.setObjectName("FabInfo")  # nombre de enlace a css
        self.usuarioRetirado.setText("Se ha retirado correctamente")
        self.usuarioRetirado.setVisible(False)
        self.usuarioRetirado.setGeometry((width/2)-(310/2), 300, 310, 100)


        self.usuarioNoEncontrado = QLabel(widget)
        self.usuarioNoEncontrado.setObjectName("FabInfo")  # nombre de enlace a css
        self.usuarioNoEncontrado.setText("Error, no se encontró a ese usuario")
        self.usuarioNoEncontrado.setVisible(False)
        self.usuarioNoEncontrado.setGeometry((width/2)-(310/2), 300, 310, 100)



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

    