from src.views.botones.ingresar.boton_ingresar import Boton_ingresar
from src.views.botones.configuraciones.avanzada.inside.funciones_inside import Funcion_inside
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import hashlib
from src.views.teclado.teclado_letras import *
from src.views.teclado.teclado_numeros import *



class Funcion_avanzada():
    def AvanzadaUserTeclado(self):
        MOV = -100
        #movimiento botones
        self.avanzada_user.setGeometry(self.width/3.6, self.height/2.7+MOV, 
                                        self.width/4.2, self.height/12)
        self.avanzada_pass.setGeometry(self.width/3.6, (self.height/2.7)+(self.height/8.5)+MOV, 
                                        self.width/4.2, self.height/12)
        self.avanzada_ingresar.setGeometry(self.width/1.8, (self.height/2.7)+MOV, 
                                        self.width/6, self.height/4.9)
        self.Teclado()
        self.NotTecladoNumerico()
        self.campo = 'AdConf-User'

    def AvanzadaPassTeclado(self):
        MOV = -100
        #movimiento botones
        self.avanzada_user.setGeometry(self.width/3.6, self.height/2.7+MOV, 
                                        self.width/4.2, self.height/12)
        self.avanzada_pass.setGeometry(self.width/3.6, (self.height/2.7)+(self.height/8.5)+MOV, 
                                        self.width/4.2, self.height/12)
        self.avanzada_ingresar.setGeometry(self.width/1.8, (self.height/2.7)+MOV, 
                                        self.width/6, self.height/4.9)
        self.NotTeclado()
        self.TecladoNumerico()
        self.campo = 'AdConf-Pass'

    def Ad_Conf_guardar_teclado(self):
        self.avanzada_user.setGeometry(self.width/3.6, self.height/2.7, 
                                        self.width/4.2, self.height/12)
        self.avanzada_pass.setGeometry(self.width/3.6, (self.height/2.7)+(self.height/8.5), 
                                        self.width/4.2, self.height/12)
        self.avanzada_ingresar.setGeometry(self.width/1.8, (self.height/2.7), 
                                        self.width/6, self.height/4.9)
        self.NotTeclado()

    def AvanzadaIngresar(self):
        try:
            #Reading the config.ini file
            self.config.read('config.ini')
            users = list(self.config['users'])
            passwords = list(self.config['passwords'])
            users_values = []
            passwords_values = []
            #Use the cycle to append values to the list from the document
            for key in users:
                users_values.append(self.config.get('users', str(key)))
            # Check if user is in the list
            if self.avanzada_user.text() in users_values:
                correct_user = True
                indU = users_values.index(self.avanzada_user.text())
            else:
                correct_user = False
            # Use the cycle to append values to the list from the document
            for key in passwords:
                p1=self.config.get('passwords', str(key))
                passwords_values.append(p1)
            # Check if password is in the list
            p = self.avanzada_pass.text()
            h = hashlib.new("sha1", p.encode())
            # Verifications
            if str(h.digest()) == passwords_values[indU]:
                correct_password = True
                indP=indU
            else:
                correct_password = False
            # Checking other conditions and connecting functions
            if self.avanzada_user.text()!="" and self.avanzada_pass.text()!="" :  #lógica para leer si los campos están vacíos
                if not self.avanzada_user.text().isdigit() and not self.avanzada_pass.text().isalpha():  #detecta si numeros donde no deben
                    if correct_user and correct_password and indU==indP:
                        self.dialogo_mensaje = "Bienvenido: "+self.avanzada_user.text()+" \n "
                        self.dialogo.setInformativeText(self.dialogo_mensaje)
                        self.dialogo.show()
                        #funcion inside
                        self.AvanzadaInsideInside()
                    else:
                        self.dialogo_mensaje = "Error, verifique los datos ingresados  \nSi el error persiste comuniquese con el fabricante"
                        self.dialogo.setInformativeText(self.dialogo_mensaje)
                        self.dialogo.show()
                else:
                    self.dialogo_mensaje = "Error, verifique los datos ingresados     \n"
                    self.dialogo.setInformativeText(self.dialogo_mensaje)
                    self.dialogo.show()
            else:
                self.dialogo_mensaje = "Debe llenar todos los campos\nantes de continuar"
                self.dialogo.setInformativeText(self.dialogo_mensaje)
                self.dialogo.show()
        except:
            self.dialogo_mensaje = "Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante"
            self.dialogo.setInformativeText(self.dialogo_mensaje)
            self.dialogo.show()

    def AvanzadaInsideInside(self):
        self.pantalla = 'inside'
        self.inside_agregar.setVisible(True)
        self.inside_enviar.setVisible(True)
        self.inside_cambiar.setVisible(True)
        self.inside_capacidad.setVisible(True)
        self.inside_eliminar.setVisible(True)
        self.avanzada_ingresar.setVisible(False)
        self.avanzada_user.setVisible(False)
        self.avanzada_pass.setVisible(False)


        self.atras.setVisible(True)
        
        self.Ad_Conf_guardar_teclado()
        self.NotTecladoNumerico()