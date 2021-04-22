from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#locals
from src.views.teclado.teclado_letras import *
from src.views.teclado.teclado_numeros import *
#from .agregar.boton_agregar import Boton_agregar

class Funcion_inside:#(Boton_agregar):

    def InsideAgregar(self):
        self.inside_agregar.setVisible(False)
        self.inside_eliminar.setVisible(False)
        self.inside_enviar.setVisible(False)
        self.inside_capacidad.setVisible(False)
        self.inside_cambiar.setVisible(False)
        self.agregar_username.setVisible(True)
        self.agregar_pass.setVisible(True)
        self.agregar_agregar.setVisible(True)
        self.enviar_newenviar.setVisible(False)
        self.enviar_setnew.setVisible(False)

    def InsideEliminar(self):
        self.inside_agregar.setVisible(False)
        self.inside_eliminar.setVisible(False)
        self.inside_enviar.setVisible(False)
        self.inside_capacidad.setVisible(False)
        self.inside_cambiar.setVisible(False)
        self.eliminar_username.setVisible(True)
        self.eliminar_pass.setVisible(True)
        self.eliminar_eliminar.setVisible(True)
        self.enviar_newenviar.setVisible(False)
        self.enviar_setnew.setVisible(False)

    def InsideEnviar(self):
        self.inside_agregar.setVisible(False)
        self.inside_eliminar.setVisible(False)
        self.inside_enviar.setVisible(False)
        self.inside_capacidad.setVisible(False)
        self.inside_cambiar.setVisible(False)
        self.capacidad_newcapacidad.setVisible(False)
        self.capacidad_setnew.setVisible(False)
        self.enviar_newenviar.setVisible(True)
        self.enviar_setnew.setVisible(True)


    def InsideCapacidad(self):
        self.inside_agregar.setVisible(False)
        self.inside_eliminar.setVisible(False)
        self.inside_enviar.setVisible(False)
        self.inside_capacidad.setVisible(False)
        self.inside_cambiar.setVisible(False)
        self.capacidad_newcapacidad.setVisible(True)
        self.capacidad_setnew.setVisible(True)
        self.enviar_newenviar.setVisible(False)
        self.enviar_setnew.setVisible(False)

    def InsideCambiar(self):
        pass