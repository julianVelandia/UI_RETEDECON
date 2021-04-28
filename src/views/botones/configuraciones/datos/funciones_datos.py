from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

#locals

class Funcion_datos:
    SiBarrasNoPie = True

    def DatosBarras(self):
        self.datos_barras.setStyleSheet("background-color: #A2A2A2;")
        self.datos_pie.setStyleSheet("background-color: none;")
        self.SiBarrasNoPie = True
        print(self.SiBarrasNoPie)

    def DatosPie(self):
        self.datos_pie.setStyleSheet("background-color:#A2A2A2;")
        self.datos_barras.setStyleSheet("background-color: none; ")
        self.SiBarrasNoPie = False
        print(self.SiBarrasNoPie)