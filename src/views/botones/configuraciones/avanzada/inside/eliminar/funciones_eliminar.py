from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import hashlib

#locals
from src.views.teclado.teclado_letras import *
from src.views.teclado.teclado_numeros import *

class Funcion_eliminar:
    def EliminarEliminar(self):
        try:
            self.config.read('config.ini')
            users = list(self.config['users'])
            passwords = list(self.config['passwords'])
            users_values = []
            passwords_values = []
            if self.eliminar_username.text() != "" and self.eliminar_pass.text() != "":  # lógica para leer si los campos están vacíos
                if not self.eliminar_username.text().isdigit() and not self.eliminar_pass.text().isalpha():  # detecta si numeros o letras donde no deben
                    # Use the cycle to append values to the list from the document
                    for key in users:
                        users_values.append(self.config.get('users', str(key)))
                    # Check if user is in the list
                    if self.eliminar_username.text() in users_values:
                        correct_user = True
                        indU = users_values.index(self.eliminar_username.text())
                    else:
                        correct_user = False
                    # Use the cycle to append values to the list from the document
                    for key in passwords:
                        p1 = self.config.get('passwords', str(key))
                        passwords_values.append(p1)
                    # Check if password is in the list
                    p = self.eliminar_pass.text()
                    h = hashlib.new("sha1", p.encode())
                    # Verifications
                    if str(h.digest()) in passwords_values:
                        correct_password = True
                        indP = passwords_values.index(str(h.digest()))
                    else:
                        correct_password = False
                    # Existance verification
                    if correct_user and correct_password and indP==indU:
                        self.dialogo_mensaje = "Se ha eliminado correctamente   \n"
                        self.dialogo.setInformativeText(self.dialogo_mensaje)
                        self.dialogo.show()
                        
                        self.HomeWindow()
                    elif correct_user and not correct_password or not indU==indP:
                        self.dialogo_mensaje = "Verifique los datos ingresados\n "
                        self.dialogo.setInformativeText(self.dialogo_mensaje)
                        self.dialogo.show()
                        
                    else:
                        self.dialogo_mensaje = "El usuario no existe\n "
                        self.dialogo.setInformativeText(self.dialogo_mensaje)
                        self.dialogo.show()
                        
                else:
                    self.dialogo_mensaje = "Error, verifique los datos ingresados\n  La contraseña debe tener solo numeros"
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


