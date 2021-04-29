from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pandas as pd
from datetime import datetime

class Funcion_estadisticas:
    posicion_fechas = 0

    def EstadisticasCambiarSemanaAtras(self):
        self.posicion_fechas += 1
        print(self.EstadisticasGetInfo())
        self.estadisticas_bar_chart.bara(self.EstadisticasGetInfo(),True)
        self.estadisticas_pie_chart.pies(self.EstadisticasGetInfo(),True)

    def EstadisticasCambiarSemanaAdelante(self):
        if  self.posicion_fechas > 0:
            self.posicion_fechas -= 1
            self.estadisticas_bar_chart.bara(self.EstadisticasGetInfo(),True)
            self.estadisticas_pie_chart.pies(self.EstadisticasGetInfo(),True)


    def EstadisticasGetInfo(self):
        self.df = pd.read_csv('src/models/data/DB.csv')
        x = []
        y = []

        df = pd.read_csv('src/models/data/DB.csv')
        fechas_unicas = []
        hoy = datetime.today().strftime('%d-%m')
        fechas_unicas.append(hoy)
        dia = int(datetime.today().strftime('%d'))
        mes = int(datetime.today().strftime('%m'))
        
        for _ in range(364):
            if dia > 1:
                dia-=1
            elif mes == 3:
                mes-=1
                dia = 28
            
            elif mes == 1 or (mes%2==0 and mes<=8) or (mes%2!=0 and mes>8):
                mes-=1
                dia = 31
            else:
                mes-=1
                dia = 30
            if mes==0:
                mes = 12
            
            if dia<10:
                disstr = str(0)+str(dia)
            else:
                disstr = str(dia)

            if mes<10:
                messtr = str(0)+str(mes)
            else:
                dismes = str(mes)

            fechas_unicas.append(disstr+'-'+messtr)

        fechas_unicas.reverse()
        #
        for _ in range(self.posicion_fechas):
            try:
                fechas_unicas.pop()
            except:
                pass

        fechas_unicas.reverse()
        for fecha in fechas_unicas:
            cont = 0
            for ent in self.df['Fecha']:
                
                if fecha+'-2021' == ent:
                    cont += 1
            y.append(cont)
            x.append(fecha)
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