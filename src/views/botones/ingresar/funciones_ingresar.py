from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime
import pandas as pd

class Funcion_ingresar:


    def IngresarIngresar(self):
        #variables locales
        nombre = str(self.ingresar_nombre.text())
        cedula= str(self.ingresar_cedula.text())
        carnet = '*' #Entra por arduino
        temp= str(self.ingresar_temp.text())
        Fecha = datetime.today().strftime('%d-%m-%Y')
        HoraIn = datetime.today().strftime('%H:%M')
        HoraOut = 'HO*'
        Delta = 'D*'
        Numingresos = 0 
        IsIn = 'True'
        cedulaExist=False

        df = pd.read_csv('src/models/data/DB.csv')
        Lista = df['Cedula']
        Lista_carnet = df['Carnet']
        try:
            #COMO FUNCION APARTE
            for cont in range(len(Lista)):
                if (str(Lista_carnet[cont]) == carnet and not carnet == '*') or str(Lista[cont]) == cedula:
                    Numingresos+=1
            Numingresos=str(Numingresos)
            

            if nombre != "" and cedula !="" and nombre!="":  #lógica para leer si los campos están vacíos
                if not nombre.isdigit() and not cedula.isalpha() and not temp.isalpha():  #detecta si numeros o letras donde no deben

                    if str(df['Cedula'][0]) == str(cedula) and str(df['IsIn'][0]) == 'True':
                        cedulaExist = True
                    for ced in range(len(Lista) - 1, 0, -1):
                        if str(df['Cedula'][ced]) == str(cedula) and str(df['IsIn'][ced]) == 'True':
                            cedulaExist = True

                    if not cedulaExist:
                        self.df_as_txt = open ("src/models/data/DB.csv", "a")
                        # ParaPandas
                        # Enviar vector persona a DB

                        #COMO FUNCION SEPARADA
                        persona = '\n'+nombre+','+cedula+','+carnet+','+temp+','+Fecha+','+HoraIn+','+HoraOut+','+Delta+','+Numingresos+','+IsIn
                        self.df_as_txt.write(persona)
                        self.df_as_txt.close()


                        #COMO FUNCION SEPARADA
                        self.dialogo_mensaje = "El usuario fue ingresado \n con éxito"
                        self.dialogo.setInformativeText(self.dialogo_mensaje)
                        self.dialogo.show()

                        self.HomeWindow()
                    else:
                        self.dialogo_mensaje = "El usuario ya está adentro    \n"
                        self.dialogo.setInformativeText(self.dialogo_mensaje)
                        self.dialogo.show()
                else:
                    
                    self.dialogo_mensaje = "Error, verifique los datos ingresados\n   "
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
            
