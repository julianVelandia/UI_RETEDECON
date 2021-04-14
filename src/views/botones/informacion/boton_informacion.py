from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#locals
from .funciones_informacion import Funcion_informacion
from src.views.botones.inicio.funciones import *

class Boton_informacion(Funcion_informacion):
    def boton_informacion_manual(self, widget):
        self.informacion_manual = QToolButton(widget)
        self.informacion_manual.setText('Manual de Usuario')
        self.informacion_manual.setObjectName("button")  # nombre de enlace a css
        self.informacion_manual.setIcon(QIcon('src/views/static/icons/icono_manual_usuario'))  # icono
        self.informacion_manual.setIconSize(QSize(65, 65))
        self.informacion_manual.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.informacion_manual.setGeometry(200, 210, 290, 180)
        self.informacion_manual.clicked.connect(self.InformacionManual)
        self.informacion_manual.setVisible(False)

    def boton_informacion_fabricante(self, widget):
        self.informacion_fabricante = QToolButton(widget)
        self.informacion_fabricante.setText('Información del\nFabricante')
        self.informacion_fabricante.setObjectName("button")  # nombre de enlace a css
        self.informacion_fabricante.setIcon(QIcon('src/views/static/icons/favicon3'))  # icono
        self.informacion_fabricante.setIconSize(QSize(60, 60))
        self.informacion_fabricante.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.informacion_fabricante.clicked.connect(self.InformacionFabricante)
        self.informacion_fabricante.setGeometry(534, 210, 290, 180)
        self.informacion_fabricante.setVisible(False)

    def qr_informacion_qr(self, widget):
        self.informacion_qr = QToolButton(widget)
        self.informacion_qr.setObjectName("button_trasnparente")  # nombre de enlace a css
        self.informacion_qr.setIcon(QIcon('src/views/static/icons/QRDRIVE.png'))  # icono
        self.informacion_qr.setIconSize(QSize(300, 300))
        self.informacion_qr.setGeometry(self.width/3.5, self.height/5, 400, 400)
        self.informacion_qr.setVisible(False)

    def label_informacion_label(self, widget):
        self.informacion_label = QLabel(widget)
        self.informacion_label.setObjectName("FabInfo")  # nombre de enlace a css
        self.informacion_label.setText("                                  GRACIAS POR USAR RETEDECON\n"
                           "\n"
                           "RETEDECON es fabricado por:\n"
                           " - Julián C. Velandia\n"
                           " - Sebastian Cubides\n"
                           " - Jhon B. Muñoz\n"
                           "Con la coolaboración de: \n"
                           " - Diego A. Tibaduiza\n"
                           "Bajo la supervición y sustento de la Unidad De Gestion De La Innovación,\n"
                           "Facultad De Ingeniería (Ingnova), de La Universidad Nacional De Colombia.\n\n"
                           "Si desea contactarse con nosotros puede hacerlo a través de los siguientes medios:\n"
                           " - Celular/Whatsapp: +57 313 8244012\n"
                           " - E-Mail: scubidest@unal.edu.co\n\n"
                           "Versión del Software: 1.0")
        self.informacion_label.setVisible(False)
        
        self.label_img_esquina_2 = QToolButton(widget)
        self.label_img_esquina_2.setGeometry(30, 5, 250, 60)
        self.label_img_esquina_2.setObjectName("button_home")  # nombre de enlace a css
        self.label_img_esquina_2.setVisible(False)
        self.label_img_esquina_2.clicked.connect(self.HomeWindow)
        