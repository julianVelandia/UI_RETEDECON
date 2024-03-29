from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import hashlib
# locals
from src.views.teclado.teclado_letras import *
from src.views.teclado.teclado_numeros import *


class Funcion_cambiar:

    def CambiarUser(self):
        MOV = -100
        # movimiento botones
        
        

        self.cambiar_user.setGeometry(self.width/4.5, self.height/2.7 + MOV, 
                                        self.width/6.1, self.height/12)
        self.cambiar_pass.setGeometry(self.width/2.5, self.height/2.7  + MOV, 
                                        self.width/6.1, self.height/12)
        self.pass_new_0.setGeometry(self.width/4.5, self.height/2.7 +self.height/8.5+ MOV, 
                                        self.width/6.1, self.height/12)
        self.pass_new_1.setGeometry(self.width/2.5, self.height/2.7 +self.height/8.5+ MOV, 
                                        self.width/6.1, self.height/12)
        self.cambiar_cambiar.setGeometry(self.width/1.7, self.height/2.7 + MOV, 
                                        self.width/6, self.height/4.9)

        self.Teclado()
        self.NotTecladoNumerico()
        self.campo = 'Cambiar-user'


    def CambiarPass(self):
        MOV = -100
        # movimiento botones
        self.cambiar_user.setGeometry(self.width/4.5, self.height/2.7 + MOV, 
                                        self.width/6.1, self.height/12)
        self.cambiar_pass.setGeometry(self.width/2.5, self.height/2.7  + MOV, 
                                        self.width/6.1, self.height/12)
        self.pass_new_0.setGeometry(self.width/4.5, self.height/2.7 +self.height/8.5+ MOV, 
                                        self.width/6.1, self.height/12)
        self.pass_new_1.setGeometry(self.width/2.5, self.height/2.7 +self.height/8.5+ MOV, 
                                        self.width/6.1, self.height/12)
        self.cambiar_cambiar.setGeometry(self.width/1.7, self.height/2.7 + MOV, 
                                        self.width/6, self.height/4.9)

        self.NotTeclado()
        self.TecladoNumerico()
        self.campo = 'Cambiar-Pass'

    def PassNew0(self):
        MOV = -100
        # movimiento botones
        self.cambiar_user.setGeometry(self.width/4.5, self.height/2.7 + MOV, 
                                        self.width/6.1, self.height/12)
        self.cambiar_pass.setGeometry(self.width/2.5, self.height/2.7  + MOV, 
                                        self.width/6.1, self.height/12)
        self.pass_new_0.setGeometry(self.width/4.5, self.height/2.7 +self.height/8.5+ MOV, 
                                        self.width/6.1, self.height/12)
        self.pass_new_1.setGeometry(self.width/2.5, self.height/2.7 +self.height/8.5+ MOV, 
                                        self.width/6.1, self.height/12)
        self.cambiar_cambiar.setGeometry(self.width/1.7, self.height/2.7 + MOV, 
                                        self.width/6, self.height/4.9)


        self.NotTeclado()
        self.TecladoNumerico()
        self.campo = 'Cambiar-Pass0'

    def PassNew1(self):
        MOV = -100
        # movimiento botones
        self.cambiar_user.setGeometry(self.width/4.5, self.height/2.7 + MOV, 
                                        self.width/6.1, self.height/12)
        self.cambiar_pass.setGeometry(self.width/2.5, self.height/2.7  + MOV, 
                                        self.width/6.1, self.height/12)
        self.pass_new_0.setGeometry(self.width/4.5, self.height/2.7 +self.height/8.5+ MOV, 
                                        self.width/6.1, self.height/12)
        self.pass_new_1.setGeometry(self.width/2.5, self.height/2.7 +self.height/8.5+ MOV, 
                                        self.width/6.1, self.height/12)
        self.cambiar_cambiar.setGeometry(self.width/1.7, self.height/2.7 + MOV, 
                                        self.width/6, self.height/4.9)
        self.NotTeclado()
        self.TecladoNumerico()
        self.campo = 'Cambiar-Pass1'

    def Cambiar_guardar_teclado(self):
        MOV =0
        self.cambiar_user.setGeometry(self.width/4.5, self.height/2.7 + MOV, 
                                        self.width/6.1, self.height/12)
        self.cambiar_pass.setGeometry(self.width/2.5, self.height/2.7  + MOV, 
                                        self.width/6.1, self.height/12)
        self.pass_new_0.setGeometry(self.width/4.5, self.height/2.7 +self.height/8.5+ MOV, 
                                        self.width/6.1, self.height/12)
        self.pass_new_1.setGeometry(self.width/2.5, self.height/2.7 +self.height/8.5+ MOV, 
                                        self.width/6.1, self.height/12)
        self.cambiar_cambiar.setGeometry(self.width/1.7, self.height/2.7 + MOV, 
                                        self.width/6, self.height/4.9)
        self.NotTeclado()

    def CambiarCambiar(self):

        # try:
        if True:
            self.config.read('config.ini')
            users = list(self.config['users'])
            passwords = list(self.config['passwords'])
            users_values = []
            passwords_values = []

            user = self.cambiar_user.text()
            password_anterior = self.cambiar_pass.text()
            password_new_0 = self.pass_new_0.text()
            password_new_1 = self.pass_new_1.text()


            if password_anterior != "" and password_new_0 != "" and password_new_1 != "":  # lógica para leer si los campos están vacíos
                if not password_anterior.isalpha() and not password_new_0.isalpha() and not password_new_1.isalpha():  # detecta si numeros o letras donde no deben
                    if password_new_0 == password_new_1:  # contraseñas iguales

                        for key in users:
                            users_values.append(self.config.get('users', str(key)))
                        # Check if user is in the list
                        if user in users_values:
                            correct_user = True
                            indU = users_values.index(user)
                        else:
                            correct_user = False
                        # Use the cycle to append values to the list from the document
                        for key in passwords:
                            passwords_values.append(self.config.get('passwords', str(key)))
                        # Check if password is in the list
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

                            k = len(users_values) - 1
                            b = 'key' + str(k + 1)
                            self.config.set('users', b, user)
                            p = password_new_0
                            h = hashlib.new('sha1', p.encode())
                            self.config.set('passwords', b, str(h.digest()).replace("%", "%%"))
                            with open('config.ini', 'w') as f:
                                self.config.write(f)
                                f.close()

                            self.dialogo_mensaje = "Se ha cambiado la contraseña   \n"
                            self.dialogo.setInformativeText(self.dialogo_mensaje)
                            self.dialogo.show()

                            self.pantalla = 'inside'
                            # eliminar
                            self.cambiar_user.setVisible(False)
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
        '''
        except:
            self.dialogo_mensaje = "Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante"
            self.dialogo.setInformativeText(self.dialogo_mensaje)
            self.dialogo.show()
        '''

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

        for k in range(b, len(users)):
            self.config.remove_option('users', 'key' + str(k + 2))
            self.config.set('users', 'key' + str(k + 1), users_values[k])
            #####
            self.config.remove_option('passwords', 'key' + str(k + 2))
            self.config.set('passwords', 'key' + str(k + 1), passwords_values[k])
        with open('config.ini', 'w') as f:
            self.config.write(f)
            f.close()
