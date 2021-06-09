from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime
import pandas as pd


class Funcion_salida:

    def Retirar_desplegar_teclado(self):
        MOV = -100
        # movimiento botones
        self.salida_nombre.setGeometry(self.width/3.6, (self.height/2.7)+MOV, 
                                        self.width/4.2, self.height/12)
        self.salida_cedula.setGeometry(self.width/3.6, (self.height/2.7)+(self.height/8.5)+MOV, 
                                        self.width/4.2, self.height/12)
                                        
        self.salida_salida.setGeometry(self.width/1.8, (self.height/2.7)+MOV, 
                                        self.width/6, self.height/4.9)
        self.Teclado()
        self.NotTecladoNumerico()
        self.campo = 'retirar-nombre'

    def Retirar_guardar_teclado(self):
       
        # movimiento botones
        

        self.salida_nombre.setGeometry(self.width/3.6, self.height/2.7, 
                                        self.width/4.2, self.height/12)
        self.salida_cedula.setGeometry(self.width/3.6, (self.height/2.7)+self.height/8.5, 
                                        self.width/4.2, self.height/12)
                                        
        self.salida_salida.setGeometry(self.width/1.8, self.height/2.7, 
                                        self.width/6, self.height/4.9)
        self.NotTeclado()

    def Retirar_desplegar_teclado_numerico_cedula(self):
        MOV = -100
        # movimiento botones
        self.salida_nombre.setGeometry(self.width/3.6, (self.height/2.7)+MOV, 
                                        self.width/4.2, self.height/12)
        self.salida_cedula.setGeometry(self.width/3.6, (self.height/2.7)+(self.height/8.5)+MOV, 
                                        self.width/4.2, self.height/12)
                                        
        self.salida_salida.setGeometry(self.width/1.8, (self.height/2.7)+MOV, 
                                        self.width/6, self.height/4.9)
        self.NotTeclado()
        self.TecladoNumerico()
        self.campo = 'retirar-cedula'

    def restar_deltas(self, HoraOut, HoraIn):
        '''
        Devuelve la diferencia en minutos
        '''
        Fecha_Hoy = datetime.today().strftime('%d-%m-%Y')
        HoraOut = HoraOut.split(':')
        HoraIn = HoraIn.split(':')

        # Tiempo total en minutos
        if not Fecha_Hoy == "aaa":
            NumOut = int(HoraOut[0]) * 60 + int(HoraOut[1])
            NumIn = int(HoraIn[0]) * 60 + int(HoraIn[1])

            delta = NumOut - NumIn
            return str(delta)
        else:
            self.dialogo_mensaje = "Ha ocurrido un error al verifcar    \nlas fechas, si persiste comuniquese   \n  con el fabricante \n    "
            self.dialogo.setInformativeText(self.dialogo_mensaje)
            self.dialogo.show()

    def SalidaSalida(self):

        # variables locales
        nombre = self.salida_nombre.text()
        cedula = self.salida_cedula.text()
        HoraOut = datetime.today().strftime('%H:%M')

        try:
            df = pd.read_csv('src/models/data/DB.csv')

            if nombre != "" and cedula != "":  # lógica para leer si los campos están vacíos
                if not nombre.isdigit() and not cedula.isalpha():  # detecta si numeros o letras donde no deben
                    persona = df[(df['Cedula'] == str(cedula)) & (df['IsIn'])].index.tolist()

                    if persona:
                        ced = persona[0]
                        self.df_as_txt = open("src/models/data/DB.csv", "r")
                        lineas = self.df_as_txt.readlines()
                        self.df_as_txt.close()
                        lineas[ced + 1] = lineas[ced + 1].replace('HO*', HoraOut).replace('D*', self.restar_deltas(
                            HoraOut, df['HoraIn'][ced])).replace('True', 'False')
                        self.df_as_txt = open("src/models/data/DB.csv", "w")
                        for l in lineas:
                            self.df_as_txt.write(l)
                        self.df_as_txt.close()
                        # Confirmacion

                        self.dialogo_mensaje = "Se ha retirado correctamente\n    "
                        self.dialogo.setInformativeText(self.dialogo_mensaje)
                        self.dialogo.show()

                        self.HomeWindow()
                    else:
                        self.dialogo_mensaje = "Error, no se encontró a ese usuario\n    "
                        self.dialogo.setInformativeText(self.dialogo_mensaje)
                        self.dialogo.show()
                else:

                    self.dialogo_mensaje = "Error, verifique los datos ingresados\n   "
                    self.dialogo.setInformativeText(self.dialogo_mensaje)
                    self.dialogo.show()
                    print('hola')
            else:

                self.dialogo_mensaje = "Debe llenar todos los campos\nantes de continuar"
                self.dialogo.setInformativeText(self.dialogo_mensaje)
                self.dialogo.show()
        except Exception as e:
            print(e)
            self.dialogo_mensaje = "Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante"
            self.dialogo.setInformativeText(self.dialogo_mensaje)
            self.dialogo.show()
