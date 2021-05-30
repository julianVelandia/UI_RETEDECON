from datetime import datetime
import pandas as pd
from src.views.teclado.teclado_numeros import *

nombre = "*"
cedula = "*"
carnet = "*"
temp = "*"
Fecha = "*"
HoraIn = "*"
HoraOut = 'HO*'
Delta = 'D*'
Numingresos = 0
IsIn = 'True'


class FuncionesEstudiantes:

    


    def s0(self):
        global nombre, cedula, carnet, temp, Fecha, HoraIn, HoraOut, Delta, Numingresos, IsIn

        self.texto_informativo.setText('El usuario fue ingresado \n con éxito')
        self.texto_informativo.setVisible(True)

        self.botonPrueba1.setVisible(True)
        self.botonPrueba2.setVisible(True)

        self.state = 0

        nombre = "*"
        cedula = "*"
        carnet = "*"
        temp = "*"
        Fecha = "*"
        HoraIn = "*"
        HoraOut = 'HO*'
        Delta = 'D*'
        Numingresos = 0
        IsIn = 'True'

        self.label_img_central.setVisible(False)
        self.movie0 = QMovie('src/views/static/gif/s0.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie0)
        self.giflabel.setVisible(True)
        self.movie0.start()

    def s1(self, uid):
        global Fecha, HoraIn, carnet

        carnet = uid

        df = pd.read_csv('src/models/data/DB.csv')

        carnetExist = df[(df['Carnet'] == str(carnet)) & (df['IsIn'])].index.tolist()

        if not carnetExist:

            self.state = 1

            Fecha = datetime.today().strftime('%d-%m-%Y')
            HoraIn = datetime.today().strftime('%H:%M')

            self.movie1 = QMovie('src/views/static/gif/s1.gif')  # Gif paso 1
            self.giflabel.setMovie(self.movie1)
            self.giflabel.setVisible(True)
            self.movie1.start()
        else:
            self.texto_informativo.setText('El usuario fue ingresado \n con éxito')

            self.timerText = QTimer()
            self.timerText.setInterval(1500)
            self.timerText.setSingleShot(True)
            self.timerText.start()
            self.timerText.timeout.connect(self.s0)  # función a ejecutar pasados los 3 seg

    def s2(self):
        global Fecha, HoraIn

        self.state = 2
        self.movie2 = QMovie('src/views/static/gif/s2.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie2)
        self.giflabel.setVisible(True)
        self.movie2.start()
                

        self.texto_informativo.setText("estado 2")

    def s3(self):
        self.state = 3
        self.movie3 = QMovie('src/views/static/gif/s3.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie3)
        self.giflabel.setVisible(True)
        self.movie3.start()
        self.texto_informativo.setText("estado 3")


    def s4(self):
        self.state = 4

        # prueba
        self.submitData()
        # --------

        self.movie4 = QMovie('src/views/static/gif/s4.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie4)
        self.giflabel.setVisible(True)
        self.movie4.start()
        self.texto_informativo.setText("estado 4")


    def s5(self):
        self.state = 5
        self.movie5 = QMovie('src/views/static/gif/s5.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie5)
        self.giflabel.setVisible(True)
        self.movie5.start()
        self.alarm.play()
        self.texto_informativo.setText("estado 5")


    def submitData(self):
        global carnet, Numingresos

        df = pd.read_csv('src/models/data/DB.csv')

        Numingresos = str(len(df[(df['Carnet'] == carnet) & (df['Carnet'] != '*')]))

        self.df_as_txt = open("src/models/data/DB.csv", "a")
        # ParaPandas
        # Enviar vector persona a DB

        # COMO FUNCION SEPARADA
        persona = '\n' + nombre + ',' + cedula + ',' + carnet + ',' + temp + ',' + Fecha + ',' + HoraIn + ',' + HoraOut + ',' + Delta + ',' + Numingresos + ',' + IsIn
        self.df_as_txt.write(persona)
        self.df_as_txt.close()

        # Mostrar que el usuario fue ingresado con exito
        self.texto_informativo.setText('Ingreso')

        self.timerText = QTimer()
        self.timerText.setInterval(1500)
        self.timerText.setSingleShot(True)
        self.timerText.start()
        self.timerText.timeout.connect(self.s0)  # función a ejecutar pasados 1.5 seg

    def restar_deltas(self, HoraOut, HoraIn):
        '''
        Devuelve la diferencia en minutos
        '''
        HoraOut = HoraOut.split(':')
        HoraIn = HoraIn.split(':')

        # Tiempo total en minutos
        NumOut = int(HoraOut[0]) * 60 + int(HoraOut[1])
        NumIn = int(HoraIn[0]) * 60 + int(HoraIn[1])

        delta = NumOut - NumIn

        return str(delta)

    def salida(self, uid):

        HoraOut = datetime.today().strftime('%H:%M')
        carnet = uid

        df = pd.read_csv('src/models/data/DB.csv')

        persona = df[(df['Carnet'] == str(carnet)) & (df['IsIn'])].index.tolist()

        if persona:
            c = persona[0]

            self.df_as_txt = open("src/models/data/DB.csv", "r")
            lineas = self.df_as_txt.readlines()
            self.df_as_txt.close()
            lineas[c + 1] = lineas[c + 1].replace('HO*', HoraOut).replace('D*', self.restar_deltas(HoraOut,
                                                                                                   df['HoraIn'][
                                                                                                       c])).replace(
                'True', 'False')
            self.df_as_txt = open("src/models/data/DB.csv", "w")
            for l in lineas:
                self.df_as_txt.write(l)
            self.df_as_txt.close()

            self.texto_informativo.setText('Usuario retirado')
            self.timerText = QTimer()
            self.timerText.setInterval(1500)
            self.timerText.setSingleShot(True)
            self.timerText.start()
            self.timerText.timeout.connect(self.s0)  # función a ejecutar pasados los 3 seg

        else:

            self.texto_informativo.setText('Usuario no encontrado')

            self.timerText = QTimer()
            self.timerText.setInterval(1500)
            self.timerText.setSingleShot(True)
            self.timerText.start()
            self.timerText.timeout.connect(self.s0)  # función a ejecutar pasados los 3 seg

    def si(self):
        self.state = (self.state + 1) % 5
        self.checkState()

    def no(self):
        self.state = 5
        self.checkState()

    def checkState(self):
        if self.state == 0:
            self.s0()
        elif self.state == 1:
            self.s1("carnetPrueba")
        elif self.state == 2:
            self.s2()
        elif self.state == 3:
            self.s3()
        elif self.state == 4:
            self.s4()
        elif self.state == 5:
            self.s5()