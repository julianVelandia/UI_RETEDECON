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
        #se llama a la funcion plot()
        
        #self.bar()

    def bar(self,info):
        #Se agrega un subplot y creo que el 111 define como las dimensiones
        ax = self.figure.add_subplot(111)
        ax.set_xlabel('X-Axis',color ='white')  #Texto de las leyendas y color
        ax.set_ylabel('Y-Axis',color ='white')
        #ax.plot(data, 'r-', color='red') ------> Esto está comentado porque es para añadir una grafica de linea
        #Aca creo los datos de prueba que puse
        #a = ['Lunes','Martes','Miercoles','Jueves','Viernes']
        #b = [10,10,10,10,5]
        ax.set_facecolor('black') #color fondo de la grafica
        ax.spines['left'].set_color('white')    #pinta la regla de la izquierda
        ax.spines['bottom'].set_color('white')   #pinta la regla de abajo
        ax.tick_params(axis='x', colors='white')    #pinta los valores del eje x
        ax.tick_params(axis='y', colors='white')    #pinta los valores del eje y
        ax.bar(info[0],info[1]) #Esta funcion crea las barras donde a esta en x y b en y
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
        # se llama a la funcion plot()
        #self.pie()
    def pie(self,info):
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:

        #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        ax = self.figure.add_subplot(111)
        ax.pie(info[1], labels=info[1], autopct='%1.1f%%',shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
