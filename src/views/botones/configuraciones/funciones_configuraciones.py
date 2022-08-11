from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
#locals
from .avanzada.boton_avanzada import Boton_avanzada

class Funcion_configuraciones:


    def ConfiguracionesAvanzada(self):
        self.configuraciones_apagar.setVisible(False)
        #self.configuraciones_ajustes.setVisible(False)
        self.configuraciones_datos.setVisible(False)
        self.configuraciones_avanzada.setVisible(False)

        #self.label_img_central.setVisible(False)
        #self.label_img_esquina.setVisible(True)
        #self.ingresar.setVisible(False)
        #self.estadisticas.setVisible(False)
        #self.detener_alarma.setVisible(False)
        #self.salida_manual.setVisible(False)
        #self.configuracion.setVisible(False)
        #self.informacion.setVisible(False)

        self.avanzada_user.setVisible(True)
        self.avanzada_user.clear()

        self.avanzada_pass.setVisible(True)
        self.avanzada_pass.clear()

        self.avanzada_ingresar.setVisible(True)

        #self.Ad_Conf_guardar_teclado()

    def ConfiguracionesDatos(self):
        self.pantalla = 'datos'
        self.configuraciones_apagar.setVisible(False)
        self.configuraciones_ajustes.setVisible(False)
        self.configuraciones_datos.setVisible(False)
        self.configuraciones_avanzada.setVisible(False)
        self.datos_barras.setVisible(True)
        self.datos_pie.setVisible(True)
        self.atras.setVisible(True)

    def ConfiguracionesApagar(self):
        sys.exit()