from src.views.botones.configuraciones.avanzada.inside.agregar.boton_agregar import Boton_agregar
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

    def InsideEliminar(self):
        pass

    def InsideEnviar(self):
        pass

    def InsideCapacidad(self):
        self.configuracion_capacidad_text.setVisible(True)
        self.ingresar_capacidad.setVisible(True)
        self.configuracion_capacidad.setVisible(False)
        self.new_admin_username.setVisible(False)
        self.new_admin_password.setVisible(False)
        self.new_admin.setVisible(False)
        self.agregar_eliminar_admin_boton.setVisible(False)
        self.cambiar_password_admin_boton.setVisible(False)
        self.enviar_datos_servidor.setVisible(False)


    def InsideCambiar(self):
        pass
