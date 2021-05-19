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

carnetExist = False


class FuncionesEstudiantes:

    def s0(self):
        global nombre, cedula, carnet, temp, Fecha, HoraIn, HoraOut, Delta, Numingresos, IsIn, carnetExist

        self.textoIngreso.setVisible(False)
        self.usuarioExiste.setVisible(False)
        self.usuarioNoEncontrado.setVisible(False)
        self.usuarioRetirado.setVisible(False)

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

        carnetExist = False

        self.label_img_central.setVisible(False)
        self.movie0 = QMovie('src/views/static/gif/s0.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie0)
        self.giflabel.setVisible(True)
        self.movie0.start()

    def s1(self, uid):
        global Fecha, HoraIn, carnet, carnetExist

        carnet = uid

        df = pd.read_csv('src/models/data/DB.csv')
        Lista_carnet = df['Carnet']

        for c in range(len(Lista_carnet) - 1, 0, -1):
            if str(df['Carnet'][c]) == str(carnet) and str(df['IsIn'][c]) == 'True':
                carnetExist = True
                break

        if not carnetExist:

            self.state = 1

            Fecha = datetime.today().strftime('%d-%m-%Y')
            HoraIn = datetime.today().strftime('%H:%M')

            self.movie1 = QMovie('src/views/static/gif/s1.gif')  # Gif paso 1
            self.giflabel.setMovie(self.movie1)
            self.giflabel.setVisible(True)
            self.movie1.start()
        else:
            self.usuarioExiste.setVisible(True)
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

    def s3(self):
        self.state = 3
        self.movie3 = QMovie('src/views/static/gif/s3.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie3)
        self.giflabel.setVisible(True)
        self.movie3.start()

    def s4(self):
        self.state = 4

        # prueba
        self.submitData()
        # --------

        self.movie4 = QMovie('src/views/static/gif/s4.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie4)
        self.giflabel.setVisible(True)
        self.movie4.start()

    def s5(self):
        self.state = 5
        self.movie5 = QMovie('src/views/static/gif/s5.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie5)
        self.giflabel.setVisible(True)
        self.movie5.start()
        self.alarm.play()

    def submitData(self):
        global carnet, Numingresos

        df = pd.read_csv('src/models/data/DB.csv')
        Lista_carnet = df['Carnet']

        for nCarnet in Lista_carnet:
            if (str(nCarnet) == carnet and carnet != '*'):
                Numingresos += 1
        Numingresos = str(Numingresos)

        self.df_as_txt = open("src/models/data/DB.csv", "a")
        # ParaPandas
        # Enviar vector persona a DB

        # COMO FUNCION SEPARADA
        persona = '\n' + nombre + ',' + cedula + ',' + carnet + ',' + temp + ',' + Fecha + ',' + HoraIn + ',' + HoraOut + ',' + Delta + ',' + Numingresos + ',' + IsIn
        self.df_as_txt.write(persona)
        self.df_as_txt.close()

        # Mostrar que el usuario fue ingresado con exito
        self.textoIngreso.setVisible(True)

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

        lista = df['Carnet']

        for c in range(len(lista) - 1, 0, -1):
            if str(df['Carnet'][c]) == str(carnet) and str(df['IsIn'][c]) == 'True':

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

                self.usuarioRetirado.setVisible(True)
                self.timerText = QTimer()
                self.timerText.setInterval(1500)
                self.timerText.setSingleShot(True)
                self.timerText.start()
                self.timerText.timeout.connect(self.s0)  # función a ejecutar pasados los 3 seg

                return  # acabar la funcion si se encuentra el carnet

        self.usuarioNoEncontrado.setVisible(True)
        self.timerText = QTimer()
        self.timerText.setInterval(1500)
        self.timerText.setSingleShot(True)
        self.timerText.start()
        self.timerText.timeout.connect(self.s0)  # función a ejecutar pasados los 3 seg

    ## botones de prueba

    def botonesPrueba(self, widget):
        self.botonPrueba1 = QToolButton(widget)
        self.botonPrueba1.setText('Si')
        self.botonPrueba1.setObjectName("small")  # nombre de enlace a css
        self.botonPrueba1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.botonPrueba1.clicked.connect(self.si)
        self.botonPrueba1.setGeometry(534, 210, 60, 60)
        self.botonPrueba1.setVisible(True)

        self.botonPrueba1 = QToolButton(widget)
        self.botonPrueba1.setText('No')
        self.botonPrueba1.setObjectName("small")  # nombre de enlace a css
        self.botonPrueba1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.botonPrueba1.clicked.connect(self.no)
        self.botonPrueba1.setGeometry(634, 210, 60, 60)
        self.botonPrueba1.setVisible(True)

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
