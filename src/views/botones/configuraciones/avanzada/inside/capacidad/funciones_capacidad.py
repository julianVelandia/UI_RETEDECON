from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#locals
from src.views.teclado.teclado_letras import *
from src.views.teclado.teclado_numeros import *

class Funcion_capacidad:
    def CapacidadNewCapacidad(self):
        MOV = -100
        #movimiento botones
        self.capacidad_newcapacidad.setGeometry(164,237+MOV,290,70)
        self.capacidad_setnew.setGeometry(570, 230+MOV, 290, 231)
        self.NotTeclado()
        self.TecladoNumerico()
        self.campo = 'New-Capacidad'
    
    def Capacidad_guardar_teclado(self):
        self.capacidad_newcapacidad.setGeometry(164,237,290,70)
        self.capacidad_setnew.setGeometry(570, 230, 290, 231)
        self.NotTeclado()
    

    
    def CapacidadSetnew(self):
        # Reading the config.ini file
        try:
            self.config.read('config.ini')            
            capacidad_vieja = self.config.getint('capacity','key1')
            self.config.set('capacity', 'key1', self.capacidad_newcapacidad.text())
            with open('config.ini', 'w') as f:
                self.config.write(f)
                f.close()
            ####
            self.dialogo_mensaje = "Se ha cambiado la capacidad máxima\n\n Capacidad antigua:  "+str(capacidad_vieja)+ '\n Capacidad actual: '+str(self.config.getint('capacity','key1'))
            self.dialogo.setInformativeText(self.dialogo_mensaje)
            self.dialogo.show()


            self.pantalla = 'inside'
            #capacidad
            self.capacidad_newcapacidad.setVisible(False)
            self.capacidad_setnew.setVisible(False)
            self.AvanzadaInsideInside()
        except:
            self.dialogo_mensaje = "Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante"
            self.dialogo.setInformativeText(self.dialogo_mensaje)
            self.dialogo.show()