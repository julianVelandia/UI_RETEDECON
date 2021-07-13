import math
from datetime import datetime

import numpy as np
import pandas as pd
from src.views.teclado.teclado_numeros import *

# librerias camara
# import busio
# import board
from scipy.interpolate import griddata
from colour import Color

# import adafruit_amg88xx

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

        self.texto_temporal.setVisible(False)
        self.texto_informativo.setText('Por favor coloque\nsu carnet en el lector')
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

        self.texto_temporal.setVisible(False)
        self.texto_informativo.setText('Por favor acerquese\n a la camara para\ntomar su temperatura')
        self.texto_informativo.setVisible(True)

        carnet = uid

        df = pd.read_csv('src/models/data/DB.csv')

        carnetExist = df[(df['Carnet'] == str(carnet)) & (df['IsIn'])].index.tolist()

        if not carnetExist:

            self.state = 1

            Fecha = datetime.today().strftime('%d-%m-%Y')
            HoraIn = datetime.today().strftime('%H:%M')

            self.giflabel.setVisible(False)

            for row in self.labelMatrix:
                for label in row:
                    label.setVisible(True)

            self.timerC = QTimer()
            self.timerC.timeout.connect(self.actualizarCamara)  # función a ejecutar pasados los 5 seg
            self.timerC.start(100)

            self.timer2 = QTimer()
            self.timer2.setInterval(5000)
            self.timer2.setSingleShot(True)
            self.timer2.start()
            self.timer2.timeout.connect(self.tStop)  # función a ejecutar pasados los 3 seg

            # self.timer.stop()

            # self.movie1 = QMovie('src/views/static/gif/s1.gif')  # Gif paso 1
            # self.giflabel.setMovie(self.movie1)
            # self.giflabel.setVisible(True)
            # self.movie1.start()
        else:
            self.texto_informativo.setVisible(False)
            self.texto_temporal.setText('El usuario ya\nse encuentra adentro')
            self.texto_temporal.setVisible(True)

            self.timerText = QTimer()
            self.timerText.setInterval(1500)
            self.timerText.setSingleShot(True)
            self.timerText.start()
            self.timerText.timeout.connect(self.s0)  # función a ejecutar pasados los 5 seg

    def tStop(self):
        self.timerC.stop()

    def s2(self):
        global Fecha, HoraIn

        for row in self.labelMatrix:
            for label in row:
                label.setVisible(False)

        self.texto_temporal.setVisible(False)
        self.texto_informativo.setText('Por favor coloque\nsu carnet en el lector')
        self.texto_informativo.setVisible(True)

        self.state = 2
        self.movie2 = QMovie('src/views/static/gif/s2.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie2)
        self.giflabel.setVisible(True)
        self.movie2.start()

    def s3(self):

        self.texto_temporal.setVisible(False)
        self.texto_informativo.setText('Acerque sus manos\nal dispensador de gel')
        self.texto_informativo.setVisible(True)

        self.state = 3
        self.movie3 = QMovie('src/views/static/gif/s3.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie3)
        self.giflabel.setVisible(True)
        self.movie3.start()

    def s4(self):

        self.texto_temporal.setVisible(False)
        self.texto_informativo.setText('Ya puede entrar\nal edificio')
        self.texto_informativo.setVisible(True)
        self.state = 4

        # prueba
        self.submitData()
        # --------

        self.movie4 = QMovie('src/views/static/gif/s4.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie4)
        self.giflabel.setVisible(True)
        self.movie4.start()

    def s5(self):

        self.texto_temporal.setVisible(False)
        self.texto_informativo.setText('¡Alerta!\n\nNo se han seguido\nlos pasos correctamente')
        self.texto_informativo.setVisible(True)

        self.state = 5
        self.movie5 = QMovie('src/views/static/gif/s5.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie5)
        self.giflabel.setVisible(True)
        self.movie5.start()
        self.alarm.play()

    def constrain(self, val, min_val, max_val):
        return min(max_val, max(min_val, val))

    def map_value(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def actualizarCamara(self):

        # i2c_bus = busio.I2C(board.SCL, board.SDA)
        # low range of the sensor (this will be blue on the screen)
        MINTEMP = 20.0
        # high range of the sensor (this will be red on the screen)
        MAXTEMP = 40.0
        # how many color values we can have
        COLORDEPTH = 1024
        # initialize the sensor
        # sensor = adafruit_amg88xx.AMG88XX(i2c_bus)

        points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
        grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]

        blue = Color("indigo")
        colors = list(blue.range_to(Color("red"), COLORDEPTH))
        # create the array of colors
        colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]

        # read the pixels
        pixels = []
        for row in sensor.pixels:
            pixels = pixels + row

        pixels = [self.map_value(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1) for p in pixels]

        # perform interpolation
        bicubic = griddata(points, pixels, (grid_x, grid_y), method="cubic")

        # print(bicubic)
        # print(len(bicubic))
        # print(len(bicubic[0]))

        # draw everything
        for ix, row in enumerate(bicubic):
            for jx, pixel in enumerate(row):
                labelColor = colors[self.constrain(int(pixel), 0, COLORDEPTH - 1)]
                self.labelMatrix[ix][jx].setStyleSheet("background-color: rgb" + str(labelColor))

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
        self.texto_informativo.setVisible(False)
        self.texto_temporal.setText('El usuario fue ingresado\ncon éxito')
        self.texto_temporal.setVisible(True)
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

            self.texto_informativo.setVisible(False)
            self.texto_temporal.setText('Usuario retirado')
            self.texto_temporal.setVisible(True)
            self.timerText = QTimer()
            self.timerText.setInterval(1500)
            self.timerText.setSingleShot(True)
            self.timerText.start()
            self.timerText.timeout.connect(self.s0)  # función a ejecutar pasados los 3 seg

        else:
            self.texto_informativo.setVisible(False)
            self.texto_temporal.setText('Usuario no encontrado')
            self.texto_temporal.setVisible(True)

            self.timerText = QTimer()
            self.timerText.setInterval(1500)
            self.timerText.setSingleShot(True)
            self.timerText.start()
            self.timerText.timeout.connect(self.s0)  # función a ejecutar pasados los 3 seg

    ############# PRUEBA

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
