from PyQt5.QtWidgets import *
import numpy as np
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

    def bara(self,info,new):
        if not new:
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
        else:
            self.ax.axis('off')
            self.actualizar(info)
    
    def actualizar(self, info):

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

#pie
class PlotCanvasP(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)  
        # Se instancia FigureCanvas para fig.
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
    def pie(self,info):
        self.xa = self.figure.add_subplot(111)
        for i in range(len(info[1])):
            if info[1][i] == 0:
                info[1][i]=0.1

        colors = ['#1F77B4']
        explode = (0.1,0.1,0.1,0.1,0.1)
        print(len(info[0]))
        wedges,text = self.xa.pie(info[1], colors = colors,wedgeprops=dict(width=0.5), startangle=-40, explode = explode)
        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-"),
                bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            self.xa.annotate(info[0][i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                        horizontalalignment=horizontalalignment, **kw)
                        
        self.xa.set_title("Porcentaje de ingresos")
        self.xa.set_facecolor('black')