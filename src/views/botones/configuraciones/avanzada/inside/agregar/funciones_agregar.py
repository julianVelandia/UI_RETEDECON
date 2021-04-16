from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import hashlib
#locals
from src.views.teclado.teclado_letras import *
from src.views.teclado.teclado_numeros import *

class Funcion_agregar:
    def AgregarAgregar(self):
        try:
            self.config.read('config.ini')
            users = list(self.config['users'])
            users_values = []
            if self.agregar_username.text() != "" and self.agregar_pass.text() != "":  # lógica para leer si los campos están vacíos
                if not self.agregar_username.text().isdigit() and not self.agregar_pass.text().isalpha():  # detecta si numeros o letras donde no deben
                    # Use the cycle to append values to the list from the document
                    for key in users:
                        users_values.append(self.config.get('users', str(key)))
                    # Check if user is in the list
                    if self.agregar_username.text() in users_values:
                        is_user = True
                    else:
                        is_user = False
                    # Existance verification
                    if not is_user:
                        k = len(users_values)
                        b = 'key'+str(k+1)
                        self.config.set('users',b, self.agregar_username.text())
                        p = self.agregar_pass.text()
                        h = hashlib.new("sha1", p.encode())
                        self.config.set('passwords',b, str(h.digest()))
                        with open('config.ini', 'w') as f:
                            self.config.write(f)
                            f.close()
                        ####
                        self.dialogo_mensaje = "Se ha registrado correctamente   \n"
                        self.dialogo.setInformativeText(self.dialogo_mensaje)
                        self.dialogo.show()
                        self.HomeWindow()
                    else:
                        self.dialogo_mensaje = "El usuario ya existe\n "
                        self.dialogo.setInformativeText(self.dialogo_mensaje)
                        self.dialogo.show()
                else:
                    self.dialogo_mensaje = "Error, verifique los datos ingresados\n La contraseña debe tener solo numeros\n  "
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