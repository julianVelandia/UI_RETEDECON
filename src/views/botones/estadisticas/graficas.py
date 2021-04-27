from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

#bar
class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100, facecolor = 'black'):
        fig = Figure(figsize=(width, height), dpi=dpi, facecolor=facecolor)#facecolor es el color del fondo del canvas
        #Se instancia FigureCanvas para fig.
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        


    def bara(self,info):
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel('Fechas',color ='white')  
        self.ax.set_ylabel('Ingresos totales',color ='white')

        self.ax.set_facecolor('black') #color fondo de la grafica
        self.ax.spines['left'].set_color('white')    #pinta la regla de la izquierda
        self.ax.spines['bottom'].set_color('white')   #pinta la regla de abajo
        self.ax.tick_params(axis='x', colors='white')    #pinta los valores del eje x
        self.ax.tick_params(axis='y', colors='white')    #pinta los valores del eje y


        self.ax.bar(info[0],info[1]) #Esta funcion crea las barras donde a esta en x y b en y
        self.draw() #Dibuja en el canvas
    
    def actualizar(self, info):
        self.ax = self.figure.add_subplot(111)
        #self.ax.set_xlabel('Fechas',color ='white')  
        #self.ax.set_ylabel('Ingresos totales',color ='white')

        self.ax.set_facecolor('black') #color fondo de la grafica
        #self.ax.spines['left'].set_color('white')    #pinta la regla de la izquierda
        #self.ax.spines['bottom'].set_color('white')   #pinta la regla de abajo
        self.ax.tick_params(axis='x', colors='white')    #pinta los valores del eje x
        self.ax.tick_params(axis='y', colors='white')    #pinta los valores del eje y


        self.ax.bar(info[0],info[1]) #Esta funcion crea las barras donde a esta en x y b en y
        self.draw() #Dibuja en el canvas
#pie
class PlotCanvasP(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)  # facecolor es el color del fondo del canvas
        # Se instancia FigureCanvas para fig.
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)#######SUPER IMPORTANTE, ESTE PARÁMETRO CONVIERTE DE VENTANA A OBJETO
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
    def pie(self,info):

        ax = self.figure.add_subplot(111)
        ax.pie(info[1], labels=info[1], autopct='%1.1f%%',shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
