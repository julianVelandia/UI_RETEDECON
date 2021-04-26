from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pandas as pd


class Funcion_estadisticas:
    posicion_fechas = 0

    def EstadisticasCambiarSemanaAtras(self):
        if self.posicion_fechas < 20 and self.posicion_fechas >= 0:
            self.posicion_fechas += 1
            self.estadisticas_bar_chart.actualizar(self.EstadisticasGetInfo())
            # [['hola','hla','holads','hodla','holda'],[0,0,1,0,0]]
            # self.estadisticas_bar_chart.setVisible(False)
            # del self.estadisticas_bar_chart
            # del self.estadisticas_pie_chart
            # self.graficas_estadisticas()

        # print('p1:'+str(self.posicion_fechas))

    def EstadisticasCambiarSemanaAdelante(self):
        if self.posicion_fechas < 20 and self.posicion_fechas > 0:
            self.posicion_fechas -= 1
            self.estadisticas_bar_chart.setVisible(True)
        # print('p2:'+str(self.posicion_fechas))

    def EstadisticasGetInfo(self):
        self.df = pd.read_csv('src/models/data/DB.csv')
        x = []
        y = []

        df = pd.read_csv('src/models/data/DB.csv')
        fechas_unicas = []

        aux = ''
        for f in df['Fecha']:
            if f != aux:
                fechas_unicas.append(f)
                aux = f

        fechas_unicas.reverse()
        # print('fechas ' + str(self.posicion_fechas))
        for _ in range(self.posicion_fechas):
            try:
                fechas_unicas.pop()
                print(fechas_unicas)
            except:
                pass

        for fecha in fechas_unicas:
            cont = 0
            for ent in self.df['Fecha']:
                if fecha == ent:
                    cont += 1
            y.append(cont)
            x.append(str(fecha).replace('-2021', ''))
            if len(x) > 4:
                break

        return [x, y]

    def EstadisticasOcupacion(self):
        df = pd.read_csv('src/models/data/DB.csv')
        Lista = df['IsIn']
        # print(Lista)
        self.ocupacion_actual = 0
        for i in Lista:
            if i == True:
                self.ocupacion_actual += 1
        print('Ocupacion Actual: ' + str(self.ocupacion_actual))
        self.estadisticas_ocupacion.setText('Ocupación Actual: ' + str(self.ocupacion_actual))

    def EstadisticasDuracion(self):
        df = pd.read_csv('src/models/data/DB.csv')
        deltas = df['Delta']
        deltas = deltas[deltas != "D*"].astype(int)  # Seleccionar solamente los que ya salieron
        self.duracion = sum(deltas) // len(deltas)
        self.estadisticas_duracion.setText('Duración promedio\nen minutos: ' + str(self.duracion))

    def EstadisticasPersonasDia(self):
        df = pd.read_csv('src/models/data/DB.csv')
        dates = df['Fecha']
        keys = set(dates.to_list())
        prom = len(dates) // len(keys)
        self.estadisticas_personasDia.setText('Promedio de personas\npor día: ' + str(prom))
