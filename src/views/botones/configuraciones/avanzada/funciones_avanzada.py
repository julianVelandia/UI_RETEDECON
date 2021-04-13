from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import hashlib

from src.views.teclado.teclado_letras import *
from src.views.teclado.teclado_numeros import *

class Funcion_avanzada:
    def AvanzadaUserTeclado(self):
        MOV = -100
        #movimiento botones
        self.avanzada_user.setGeometry(164.2,237+MOV,290,70)
        self.avanzada_pass.setGeometry(164.2,341+MOV,290,70)
        self.avanzada_ingresar.setGeometry(570, 237+MOV, 290, 176.3)
        self.Teclado()
        self.NotTecladoNumerico()
        self.campo = 'AdConf-User'

    def AvanzadaPassTeclado(self):
        MOV = -100
        #movimiento botones
        self.avanzada_user.setGeometry(164.2,237+MOV,290,70)
        self.avanzada_pass.setGeometry(164.2,341+MOV,290,70)
        self.avanzada_ingresar.setGeometry(570, 237+MOV, 290, 176.3)
        self.NotTeclado()
        self.TecladoNumerico()
        self.campo = 'AdConf-Pass'

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
            if str(h.digest()) in passwords_values:
                correct_password = True
                indP = passwords_values.index(str(h.digest()))
            else:
                correct_password = False
            # Checking other conditions and connecting functions
            if self.avanzada_user.text()!="" and self.avanzada_pass.text()!="" :  #lógica para leer si los campos están vacíos
                if not self.avanzada_user.text().isdigit() and not self.avanzada_pass.text().isalpha():  #detecta si numeros donde no deben
                    if correct_user and correct_password and indU==indP:
                        self.dialogo_mensaje = "Bienvenido: +"+self.avanzada_user.text()+" \n "
                        self.dialogo.setInformativeText(self.dialogo_mensaje)
                        self.dialogo.show()
                        

                        self.ConfiguracionAvanzadaInside()

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
            
            
