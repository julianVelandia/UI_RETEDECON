from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime
import pandas as pd


class Funcion_salida:


    def restar_deltas(self,HoraOut,HoraIn):
        '''
        Devuelve la diferencia en minutos
        '''
        Fecha_Hoy = datetime.today().strftime('%d-%m-%Y')
        HoraOut= HoraOut.split(':')
        HoraIn= HoraIn.split(':')        

        #Tiempo total en minutos
        if not Fecha_Hoy=="aaa":
            NumOut=int(HoraOut[0])*60+int(HoraOut[1])
            NumIn=int(HoraIn[0])*60+int(HoraIn[1])

            delta = NumOut-NumIn
            return str(delta)
        else:
            self.dialogo_mensaje = "Ha ocurrido un error al verifcar    \nlas fechas, si persiste comuniquese   \n  con el fabricante \n    "
            self.dialogo.setInformativeText(self.dialogo_mensaje)
            self.dialogo.show()
    
    def SalidaSalida(self):

        #variables locales
        nombre = self.salida_nombre.text()
        cedula = self.salida_cedula.text()
        HoraOut = datetime.today().strftime('%H:%M')
        
        try:
            df = pd.read_csv('src/models/data/DB.csv')
            Lista = df['Cedula']
    
            if nombre!="" and cedula!="":  #lógica para leer si los campos están vacíos
                if not nombre.isdigit() and not cedula.isalpha():  #detecta si numeros o letras donde no deben
                    flag = True
                    if str(df['Cedula'][0]) == str(cedula) and str(df['IsIn'][0]) == 'True':
                        flag = False
                        self.df_as_txt = open ("src/models/data/DB.csv", "r")

                        #COMO FUNCION APARTE

                        lineas = self.df_as_txt.readlines()
                        self.df_as_txt.close()
                        lineas[1] = lineas[1].replace('HO*',HoraOut).replace('D*',self.restar_deltas(HoraOut,df['HoraIn'][0])).replace('True','False')
                        self.df_as_txt = open("src/models/data/DB.csv", "w")
                        for l in lineas:
                            self.df_as_txt.write(l)
                        self.df_as_txt.close()

                        #Confirmacion
                        
                        self.dialogo_mensaje = "Se ha retirado correctamente\n    "
                        self.dialogo.setInformativeText(self.dialogo_mensaje)
                        self.dialogo.show()

                        self.HomeWindow()

                    for ced in range(len(Lista) - 1, 0, -1):
                        if str(df['Cedula'][ced]) == str(cedula) and str(df['IsIn'][ced]) == 'True':
                            flag =False
                            self.df_as_txt = open ("src/models/data/DB.csv", "r")
                            lineas = self.df_as_txt.readlines()
                            self.df_as_txt.close()
                            lineas[ced+1] = lineas[ced+1].replace('HO*',HoraOut).replace('D*',self.restar_deltas(HoraOut,df['HoraIn'][ced])).replace('True','False')
                            self.df_as_txt = open("src/models/data/DB.csv", "w")
                            for l in lineas:
                                self.df_as_txt.write(l)
                            self.df_as_txt.close()
                            #Confirmacion
                            
                            self.dialogo_mensaje = "Se ha retirado correctamente\n    "
                            self.dialogo.setInformativeText(self.dialogo_mensaje)
                            self.dialogo.show()

                            self.HomeWindow()
                    if flag:
                        
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
        except:
            
            self.dialogo_mensaje = "Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante"
            self.dialogo.setInformativeText(self.dialogo_mensaje)
            self.dialogo.show()
