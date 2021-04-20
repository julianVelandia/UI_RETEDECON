from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pandas as pd


class Funcion_estadisticas:
    def get_info(self):
        self.df = pd.read_csv('src/models/data/DB.csv')

        #x = ['Lunes','Martes','Miercoles','Jueves','Viernes']
        x = []
        y = []

        #llenar x
       
        fechas_unicas = set(self.df['Fecha'])

        
        for fecha in fechas_unicas:
            cont =0 
            for ent in self.df['Fecha']:
                if fecha == ent:
                    cont +=1
            y.append(cont)
            x.append(str(fecha).replace('-2021',''))
            if len(x)>4:
                break
        
        

            


        print(x)
        print(y)
        return [x,y]
    