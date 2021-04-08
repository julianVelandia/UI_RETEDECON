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
        #Ojo, si las fechas son distintas pueden haber problemas
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
            dialogo_error_fecha = QMessageBox(self.centralWidget)
            dialogo_error_fecha.setWindowTitle(self.title)
            dialogo_error_fecha.addButton("Aceptar", 0)
            dialogo_error_fecha.setInformativeText("Ha ocurrido un error al verifcar    \nlas fechas, si persiste comuniquese   \n  con el fabricante \n    ")
            dialogo_error_fecha.show()
    
    def SalidaSalida(self,widget):

        #variables locales
        nombre = str(self.salida_nombre.text())
        cedula= str(self.salida_nombre.text())
        carnet = '*' #Entra por arduino
        Fecha = datetime.today().strftime('%d-%m-%Y')
        HoraIn = datetime.today().strftime('%H:%M')
        HoraOut = 'HO*'
        Delta = 'D*'
        Numingresos = 0 
        IsIn = 'True'

        try:
            df = pd.read_csv('src/models/DB.csv')
            Lista = df['Cedula']
            carnet = '*'
            HoraOut = datetime.today().strftime('%H:%M')

            if nombre!="" and cedula!="":  #lógica para leer si los campos están vacíos
                if not nombre.isdigit() and not cedula.isalpha():  #detecta si numeros o letras donde no deben
                    flag = True
                    if str(df['Cedula'][0]) == cedula and str(df['IsIn'][0]) == 'True':
                        flag = False
                        self.df_as_txt = open ("src/models/DB.csv", "r")

                        #COMO FUNCION APARTE

                        lineas = self.df_as_txt.readlines()
                        self.df_as_txt.close()
                        lineas[1] = lineas[1].replace('HO*',HoraOut).replace('D*',self.restar_deltas(HoraOut,df['HoraIn'][0])).replace('True','False')
                        print(lineas[1])
                        self.df_as_txt = open("../DB.csv", "w")
                        for l in lineas:
                            self.df_as_txt.write(l)
                        self.df_as_txt.close()

                        #Confirmacion
                        dialogo_exitoso = QMessageBox(widget)
                        dialogo_exitoso.setWindowTitle(self.title)
                        dialogo_exitoso.addButton("Aceptar", 0)
                        dialogo_exitoso.setInformativeText("Se ha retirado correctamente\n    ")
                        dialogo_exitoso.show()
                        #########self.HomeWindow()

                    for ced in range(len(Lista) - 1, 0, -1):
                        if str(df['Cedula'][ced]) == cedula and str(df['IsIn'][ced]) == 'True':
                            flag =False
                            self.df_as_txt = open ("../DB.csv", "r")
                            lineas = self.df_as_txt.readlines()
                            self.df_as_txt.close()
                            lineas[ced+1] = lineas[ced+1].replace('HO*',HoraOut).replace('D*',self.restar_deltas(HoraOut,df['HoraIn'][ced])).replace('True','False')
                            self.df_as_txt = open("../DB.csv", "w")
                            for l in lineas:
                                self.df_as_txt.write(l)
                            self.df_as_txt.close()
                            #Confirmacion
                            dialogo_exitoso = QMessageBox(self.centralWidget)
                            dialogo_exitoso.setWindowTitle(self.title)
                            dialogo_exitoso.addButton("Aceptar", 0)
                            dialogo_exitoso.setInformativeText("Se ha retirado correctamente\n    ")
                            dialogo_exitoso.show()
                            #####self.HomeWindow()
                    if flag:
                        dialogo_error_busqueda = QMessageBox(widget)
                        dialogo_error_busqueda.setWindowTitle(self.title)
                        dialogo_error_busqueda.addButton("Aceptar", 0)
                        dialogo_error_busqueda.setInformativeText("Error, no se encontró a ese usuario\n    ")
                        dialogo_error_busqueda.show()
                else:
                    dialogo_error_typ_out = QMessageBox(widget)
                    dialogo_error_typ_out.setWindowTitle(self.title)
                    dialogo_error_typ_out.addButton("Aceptar", 0)
                    dialogo_error_typ_out.setInformativeText("Error, verifique los datos ingresados\n   ")
                    dialogo_error_typ_out.show()
            else:
                dialogo_error_incompleto_out = QMessageBox(widget)
                dialogo_error_incompleto_out.setWindowTitle(self.title)
                dialogo_error_incompleto_out.addButton("Aceptar", 0)
                dialogo_error_incompleto_out.setInformativeText("Debe llenar todos los campos\nantes de continuar")
                dialogo_error_incompleto_out.show()
        except:
            dialogo_error_lectura = QMessageBox(widget)
            dialogo_error_lectura.setWindowTitle(self.title)
            dialogo_error_lectura.addButton("Aceptar", 0)
            dialogo_error_lectura.setInformativeText("Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante")
            dialogo_error_lectura.show()