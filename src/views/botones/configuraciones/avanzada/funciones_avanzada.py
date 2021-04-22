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

    def Ad_Conf_guardar_teclado(self):
        self.avanzada_user.setGeometry(164, 240, 320, 70)
        self.avanzada_pass.setGeometry(164,330,320,70)
        self.avanzada_ingresar.setGeometry(570, 240, 280, 160)
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
        self.inside_agregar.setVisible(True)
        self.inside_enviar.setVisible(True)
        self.inside_cambiar.setVisible(True)
        self.inside_capacidad.setVisible(True)
        self.inside_eliminar.setVisible(True)
        self.avanzada_ingresar.setVisible(False)
        self.avanzada_user.setVisible(False)
        self.avanzada_pass.setVisible(False)
        '''
        self.configuraciones_apagar.setVisible(False)
        self.configuraciones_ajustes.setVisible(False)
        self.configuraciones_datos.setVisible(False)
        self.configuraciones_avanzada.setVisible(False)
        self.label_img_central.setVisible(False)
        self.label_img_esquina.setVisible(True)
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)
        self.configuracion_avanzada_user.setVisible(False)
        self.configuracion_avanzada_pass.setVisible(False)
        self.ingresar_Ad_Conf.setVisible(False)
        self.ingresar_capacidad.setVisible(False)
        self.configuracion_capacidad_text.setVisible(False)
        '''
        self.Ad_Conf_guardar_teclado()
        self.NotTecladoNumerico()