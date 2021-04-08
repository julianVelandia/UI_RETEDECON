from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime
import pandas as pd

class Funcion_ingresar:
    
    def IngresarIngresar(self,widget):
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


        df = pd.read_csv('src/models/DB.csv')
        Lista = df['Cedula']
        Lista_carnet = df['Carnet']
        try:
            #COMO FUNCION APARTE
            for cont in range(len(Lista)):
                if (str(Lista_carnet[cont]) == str(self.carnet) and not str(self.carnet) == '*') or str(Lista[cont]) == str(self.ingresar_cedula.text()):
                    self.Numingresos+=1
            self.Numingresos=str(self.Numingresos)
            print(self.Numingresos)

            if nombre != "" and cedula !="" and nombre!="":  #lógica para leer si los campos están vacíos
                if not nombre.isdigit() and not cedula.isalpha() and not nombre.isalpha():  #detecta si numeros o letras donde no deben

                    if str(df['Cedula'][0]) == str(cedula) and str(df['IsIn'][0]) == 'True':
                        cedulaExist = True
                    for ced in range(len(Lista) - 1, 0, -1):
                        if str(df['Cedula'][ced]) == str(cedula) and str(df['IsIn'][ced]) == 'True':
                            cedulaExist = True

                    if not cedulaExist:
                        self.df_as_txt = open ("src/models/DB.csv", "a")
                        # ParaPandas
                        # Enviar vector persona a DB

                        #COMO FUNCION SEPARADA
                        persona = '\n'+nombre+','+cedula+','+carnet+','+temp+','+Fecha+','+HoraIn+','+HoraOut+','+Delta+','+Numingresos+','+IsIn
                        self.df_as_txt.write(persona)
                        self.df_as_txt.close()


                        #COMO FUNCION SEPARADA
                        dialogo_exitoso = QMessageBox(widget)
                        dialogo_exitoso.setWindowTitle(self.title)
                        dialogo_exitoso.addButton("Aceptar", 0)
                        dialogo_exitoso.setInformativeText("Se ha ingresado correctamente   \n")
                        dialogo_exitoso.show()
                        self.HomeWindow()
                    else:
                        dialogo_error_cedulaExistente = QMessageBox(widget)
                        dialogo_error_cedulaExistente.setWindowTitle(self.title)
                        dialogo_error_cedulaExistente.addButton("Aceptar", 0)
                        dialogo_error_cedulaExistente.setInformativeText("El usuario ya está adentro    \n")
                        dialogo_error_cedulaExistente.show()
                else:
                    dialogo_error_typ = QMessageBox(widget)
                    dialogo_error_typ.setWindowTitle(self.title)
                    dialogo_error_typ.addButton("Aceptar", 0)
                    dialogo_error_typ.setInformativeText("Error, verifique los datos ingresados\n   ")
                    dialogo_error_typ.show()
            else:
                dialogo_error_incompleto = QMessageBox(widget)
                dialogo_error_incompleto.setWindowTitle(self.title)
                dialogo_error_incompleto.addButton("Aceptar", 0)
                dialogo_error_incompleto.setInformativeText("Debe llenar todos los campos\nantes de continuar")
                dialogo_error_incompleto.show()
        except:
            dialogo_error_escritura = QMessageBox(widget)
            dialogo_error_escritura.setWindowTitle(self.title)
            dialogo_error_escritura.addButton("Aceptar", 0)
            dialogo_error_escritura.setInformativeText("Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante")
            dialogo_error_escritura.show()