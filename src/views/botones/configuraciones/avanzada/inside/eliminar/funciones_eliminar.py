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
                        passwords_values.append(self.config.get('passwords', str(key)))
                    # Check if password is in the list
                    p = self.eliminar_pass.text()
                    h = hashlib.new("sha1", p.encode())
                    # Verifications
                    if str(h.digest()) == passwords_values[indU]:
                        correct_password = True
                        #indP = passwords_values.index(str(h.digest()))
                        indP = indU
                    else:
                        correct_password = False
                    # Existance verification
                    if correct_user and correct_password and indP==indU:
                        #index a remove the values wanted
                        d = 'key' + str(indU+1)
                        self.config.remove_option('users', d)
                        self.config.remove_option('passwords', d)
                        #write again
                        with open('config.ini', 'w') as f:
                            self.config.write(f)
                            f.close()
                        self.update_keys()
                        self.dialogo_mensaje = "Se ha eliminado correctamente   \n"
                        self.dialogo.setInformativeText(self.dialogo_mensaje)
                        self.dialogo.show()


                        self.pantalla = 'inside'
                        #eliminar
                        self.eliminar_username.setVisible(False)
                        self.eliminar_pass.setVisible(False)
                        self.eliminar_eliminar.setVisible(False)
                        self.AvanzadaInsideInside()


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

    def update_keys(self):
        self.config.read('config.ini')
        users = list(self.config['users'])
        passwords = list(self.config['passwords'])
        users_values = []
        passwords_values = []
        key = 0
        for keyy in users:
            users_values.append(self.config.get('users', str(keyy)))
        for keyy in users:
            passwords_values.append(self.config.get('passwords', str(keyy)))

        for keys in users:
            key += 1
            if not str(keys) == 'key' + str(key):
                print("falta " + 'key' + str(key))
                break
            else:
                print(str(keys))
        a = len(users) - key + 1
        b = len(users) - a
        print(a)
        print(b)

        for k in range(b, len(users)):
            self.config.remove_option('users', 'key' + str(k + 2))
            self.config.set('users', 'key' + str(k + 1), users_values[k])
            #####
            self.config.remove_option('passwords', 'key' + str(k + 2))
            self.config.set('passwords', 'key' + str(k + 1), passwords_values[k])
        with open('config.ini', 'w') as f:
            self.config.write(f)
            f.close()