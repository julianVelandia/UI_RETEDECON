from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import hashlib
#locals
from src.views.teclado.teclado_letras import *
from src.views.teclado.teclado_numeros import *

class Funcion_cambiar:
    def CambiarCambiar(self):
        '''
        cambiar_pass
        pass_new_0
        pass_new_1
        cambiar_cambiar
        '''
        try:
            self.config.read('config.ini')
            users = list(self.config['users'])
            passwords = list(self.config['passwords'])
            users_values = []
            passwords_values = []

            password_anterior = self.cambiar_pass.text()
            password_new_0 = self.pass_new_0.text()
            password_new_1 = self.pass_new_1.text()


            if password_anterior != "" and password_new_0 != "" and password_new_1 != "":  # lógica para leer si los campos están vacíos
                if not password_anterior.isalpha() and not password_new_0.isalpha() and not password_new_1.isalpha():  # detecta si numeros o letras donde no deben
                    if password_new_0==password_new_1: # contraseñas iguales

                    
                        # Use the cycle to append values to the list from the document
                        for key in users:
                            users_values.append(self.config.get('users', str(key)))
                        # Check if user is in the list
                        
                        
                        # Use the cycle to append values to the list from the document
                        for key in passwords:
                            passwords_values.append(self.config.get('passwords', str(key)))
                        # Check if password is in the list
                        indU = users_values.index(self.avanzada_user.text())

                        p = password_anterior
                        h = hashlib.new("sha1", p.encode())
                        # Verifications
                        if str(h.digest()) == passwords_values[indU]:
                            correct_password = True
                            #indP = passwords_values.index(str(h.digest()))
                            indP = indU
                        else:
                            correct_password = False
                        # Existance verification
                        if correct_password and indP==indU:
                            #index a remove the values wanted

                            d = 'key' + str(indU+1)
                            self.config.remove_option('users', d)
                            self.config.remove_option('passwords', d)
                            #write again
                            with open('config.ini', 'w') as f:
                                self.config.write(f)
                                f.close()
                            self.update_keys()



                            k = len(users_values)
                            b = 'key'+str(k+1)
                            self.config.set('users',b, self.avanzada_user.text())
                            p = password_new_0
                            h = hashlib.new("sha1", p.encode())
                            self.config.set('passwords',b, str(h.digest()))
                            with open('config.ini', 'w') as f:
                                self.config.write(f)
                                f.close()


                            self.dialogo_mensaje = "Se ha cambiado la contraseña   \n"
                            self.dialogo.setInformativeText(self.dialogo_mensaje)
                            self.dialogo.show()

                            self.pantalla = 'inside'
                            #eliminar
                            self.cambiar_pass.setVisible(False)
                            self.pass_new_0.setVisible(False)
                            self.pass_new_1.setVisible(False)
                            self.cambiar_cambiar.setVisible(False)
                            
                            self.AvanzadaInsideInside()

                        else:
                            self.dialogo_mensaje = "Contraseña erronea\n"
                            self.dialogo.setInformativeText(self.dialogo_mensaje)
                            self.dialogo.show()
                    else:
                        self.dialogo_mensaje = "Las contraseñas no son iguales\n"
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
                