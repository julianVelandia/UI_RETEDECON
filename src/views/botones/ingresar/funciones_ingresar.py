from datetime import datetime
import pandas as pd


class Funcion_ingresar:

    def Ingresar_desplegar_teclado_numerico_cedula(self):
        self.campo = 'ingresar-cedula'
        #self.Ingresar_desplegar_teclado_numerico()

    def Ingresar_desplegar_teclado_numerico_temp(self):
        self.campo = 'ingresar-temp'
        #self.Ingresar_desplegar_teclado_numerico()

    def Ingresar_desplegar_teclado_numerico(self):
        MOV = -self.height/10
        # movimiento botones
        self.ingresar_nombre.setGeometry(self.width/3.6, (self.height/2.7) + MOV, 
                                        self.width/4.2, self.height/12)
        self.ingresar_cedula.setGeometry(self.width/3.6, (self.height/2.7)+(self.height/8.5)+MOV, 
                                        self.width/7, self.height/12)
        self.ingresar_temp.setGeometry((self.width/3.6) + (self.width/6), (self.height/2.7)+(self.height/8.5)+MOV, 
                                        self.width/14, self.height/12)
        self.ingresar_ingresar.setGeometry(self.width/1.8, (self.height/2.7) + MOV, 
                                        self.width/6, self.height/4.9)
        self.NotTeclado()
        self.TecladoNumerico()

    def Ingresar_guardar_teclado_numerico(self):
        self.ingresar_nombre.setGeometry(self.width/3.6, self.height/2.7, 
                                        self.width/4.2, self.height/12)
        self.ingresar_cedula.setGeometry(self.width/3.6, (self.height/2.7)+self.height/8.5, 
                                        self.width/7, self.height/12)
        self.ingresar_temp.setGeometry((self.width/3.6) + (self.width/6), (self.height/2.7)+self.height/8.5, 
                                        self.width/14, self.height/12)
        self.ingresar_ingresar.setGeometry(self.width/1.8, self.height/2.7, 
                                        self.width/6, self.height/4.9)
        self.NotTecladoNumerico()

    def Ingresar_desplegar_teclado(self):
        MOV = -self.height/10
        # movimiento botones
        #self.ingresar_nombre.setGeometry(self.width/3.6, (self.height/2.7) + MOV,
        #                                self.width/4.2, self.height/12)
        #self.ingresar_cedula.setGeometry(self.width/3.6, (self.height/2.7)+(self.height/8.5)+MOV,
        #                                self.width/7, self.height/12)
        #self.ingresar_temp.setGeometry((self.width/3.6) + (self.width/6), (self.height/2.7)+(self.height/8.5)+MOV,
        #                                self.width/14, self.height/12)
        #self.ingresar_ingresar.setGeometry(self.width/1.8, (self.height/2.7) + MOV,
        #                                self.width/6, self.height/4.9)
        #self.Teclado()
        self.NotTecladoNumerico()
        self.campo = 'ingresar-nombre'

    def Ingresar_guardar_teclado(self):
        self.ingresar_nombre.setGeometry(self.width/3.6, self.height/2.7, 
                                        self.width/4.2, self.height/12)
        self.ingresar_cedula.setGeometry(self.width/3.6, (self.height/2.7)+self.height/8.5, 
                                        self.width/7, self.height/12)
        self.ingresar_temp.setGeometry((self.width/3.6) + (self.width/6), (self.height/2.7)+self.height/8.5, 
                                        self.width/14, self.height/12)
        self.ingresar_ingresar.setGeometry(self.width/1.8, self.height/2.7, 
                                        self.width/6, self.height/4.9)
        self.NotTeclado()

    def IngresarIngresar(self):
        # variables locales
        nombre = str(self.ingresar_nombre.text())
        cedula = str(self.ingresar_cedula.text())
        carnet = '*'  # Entra por arduino
        temp = str(self.ingresar_temp.text())
        Fecha = datetime.today().strftime('%d-%m-%Y')
        HoraIn = datetime.today().strftime('%H:%M')
        HoraOut = 'HO*'
        Delta = 'D*'
        IsIn = 'True'

        df = pd.read_csv('src/models/data/DB.csv')

        try:

            Numingresos = str(len(df[(df['Cedula'] == cedula)]))

            if nombre != "" and cedula != "" and nombre != "":  # lógica para leer si los campos están vacíos
                if not nombre.isdigit() and not cedula.isalpha() and not temp.isalpha():  # detecta si numeros o letras donde no deben

                    cedulaExist = df[(df['Cedula'] == str(cedula)) & (df['IsIn'])].index.tolist()

                    if not float(temp) >= 37.5:
                        if not cedulaExist:
                            self.df_as_txt = open("src/models/data/DB.csv", "a")
                            # ParaPandas

                            # Enviar vector persona a DB

                            # COMO FUNCION SEPARADA
                            persona = '\n' + nombre + ',' + cedula + ',' + carnet + ',' + temp + ',' + Fecha + ',' + HoraIn + ',' + HoraOut + ',' + Delta + ',' + Numingresos + ',' + IsIn
                            self.df_as_txt.write(persona)
                            self.df_as_txt.close()

                            # COMO FUNCION SEPARADA
                            self.dialogo_mensaje = "El usuario fue ingresado \n con éxito"
                            self.dialogo.setInformativeText(self.dialogo_mensaje)
                            self.dialogo.show()

                            self.HomeWindow()
                        else:
                            self.dialogo_mensaje = "El usuario ya está adentro    \n"
                            self.dialogo.setInformativeText(self.dialogo_mensaje)
                            self.dialogo.show()
                    else:
                        # reproducir alarma
                        self.alarm.play()

                        self.dialogo_mensaje = "EL USUARIO TIENE FIEBRE    \n"
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
        except Exception as e:
            print(e)
            self.dialogo_mensaje = "Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante"
            self.dialogo.setInformativeText(self.dialogo_mensaje)
            self.dialogo.show()
