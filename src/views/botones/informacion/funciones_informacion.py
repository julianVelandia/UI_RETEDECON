from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Funcion_informacion:
    def InformacionManual(self):
        self.pantalla = 'manual'
        self.informacion_qr.setVisible(True)
        self.atras.setVisible(True)
        self.informacion_fabricante.setVisible(False)
        self.informacion_manual.setVisible(False)
    
    def InformacionFabricante(self):
        self.pantalla = 'fabricante'
        self.atras.setVisible(True)
        self.informacion_label.setVisible(True)
        #self.label_img_esquina_2.setVisible(True)
        self.informacion_fabricante.setVisible(False)
        self.informacion_manual.setVisible(False)