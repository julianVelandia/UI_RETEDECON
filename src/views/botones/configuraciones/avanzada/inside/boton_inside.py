from src.views.botones.configuraciones.avanzada.inside.capacidad.boton_capacidad import Boton_capacidad
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#locals
from .funciones_inside import Funcion_inside
from .agregar.boton_agregar import Boton_agregar
from .eliminar.boton_eliminar import Boton_eliminar
from .capacidad.boton_capacidad import Boton_capacidad
from .cambiar.boton_cambiar import Boton_cambiar
from screeninfo import get_monitors

class Boton_inside(Funcion_inside, Boton_agregar, Boton_eliminar, Boton_capacidad, Boton_cambiar):
    
    
    width = get_monitors()[0].width
    height = get_monitors()[0].height

    def boton_inside_agregar(self, widget):
        self.inside_agregar = QToolButton(widget)
        self.inside_agregar.setText('Agregar Administrador')
        self.inside_agregar.setObjectName("button")  # nombre de enlace a css
        self.inside_agregar.setIcon(QIcon('src/views/static/icons/icono_add_delete_admin'))  # icono
        self.inside_agregar.setIconSize(QSize(self.height/11,self.height/11))
        self.inside_agregar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.inside_agregar.clicked.connect(self.InsideAgregar)
        self.inside_agregar.setGeometry(self.width/23, self.height/7, 
                                    self.width/3.6, self.height/3.3)

        self.inside_agregar.setVisible(False)

    def boton_inside_eliminar(self, widget):
        self.inside_eliminar = QToolButton(widget)
        self.inside_eliminar.setText('Eliminar Administrador')
        self.inside_eliminar.setObjectName("button")  # nombre de enlace a css
        self.inside_eliminar.setIcon(QIcon('src/views/static/icons/icono_add_delete_admin'))  # icono
        self.inside_eliminar.setIconSize(QSize(self.height/11,self.height/11))
        self.inside_eliminar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.inside_eliminar.clicked.connect(self.InsideEliminar)
        self.inside_eliminar.setGeometry(self.width/2.8, self.height/7, 
                                    self.width/3.6, self.height/3.3)
        self.inside_eliminar.setVisible(False)

    def boton_inside_enviar(self, widget):
        self.inside_enviar = QToolButton(widget)
        self.inside_enviar.setText('Enviar Datos Al Servidor')
        self.inside_enviar.setObjectName("button")  # nombre de enlace a css
        self.inside_enviar.setIcon(QIcon('src/views/static/icons/icono_config_datos'))  # icono
        self.inside_enviar.setIconSize(QSize(self.height/11,self.height/11))
        self.inside_enviar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.inside_enviar.clicked.connect(self.InsideEnviar)
        self.inside_enviar.setGeometry(self.width/1.5, self.height/7, 
                                    self.width/3.6, self.height/3.3)
        self.inside_enviar.setVisible(False)

    def boton_inside_capacidad(self, widget):
        self.inside_capacidad = QToolButton(widget)
        self.inside_capacidad.setText('Capacidad Máxima')
        self.inside_capacidad.setObjectName("button")  # nombre de enlace a css
        self.inside_capacidad.setIcon(QIcon('src/views/static/icons/icono_capacidad'))  # icono
        self.inside_capacidad.setIconSize(QSize(self.height/11,self.height/11))
        self.inside_capacidad.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.inside_capacidad.clicked.connect(self.InsideCapacidad)#Capacidad
        self.inside_capacidad.setGeometry(self.width/5, self.height/1.9, 
                                    self.width/3.6, self.height/3.3)

        self.inside_capacidad.setVisible(False)

    def boton_inside_cambiar(self, widget):
        self.inside_cambiar = QToolButton(widget)
        self.inside_cambiar.setText('Cambiar Contraseña')
        self.inside_cambiar.setObjectName("button")  # nombre de enlace a css
        self.inside_cambiar.setIcon(QIcon('src/views/static/icons/icono_password'))  # icono
        self.inside_cambiar.setIconSize(QSize(self.height/11,self.height/11))
        self.inside_cambiar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.inside_cambiar.clicked.connect(self.InsideCambiar)
        self.inside_cambiar.setGeometry(self.width/1.9, self.height/1.9, 
                                    self.width/3.6, self.height/3.3)
        self.inside_cambiar.setVisible(False)