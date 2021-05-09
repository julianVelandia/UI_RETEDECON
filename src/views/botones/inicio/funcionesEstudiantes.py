from src.views.teclado.teclado_numeros import *

class FuncionesEstudiantes:

    def checkState(self):
        if self.state == 0:
            self.s0()
        elif self.state == 1:
            self.s1()
        elif self.state == 2:
            self.s2()
        elif self.state == 3:
            self.s3()
        elif self.state == 4:
            self.s4()
        elif self.state == 5:
            self.s5()


    def s0(self):
        self.label_img_central.setVisible(False)
        self.movie0 = QMovie('src/views/static/gif/s0.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie0)
        self.giflabel.setVisible(True)
        self.movie0.start()


    def s1(self):
        self.movie1 = QMovie('src/views/static/gif/s1.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie1)
        self.giflabel.setVisible(True)
        self.movie1.start()


    def s2(self):
        self.movie2 = QMovie('src/views/static/gif/s2.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie2)
        self.giflabel.setVisible(True)
        self.movie2.start()


    def s3(self):
        self.movie3 = QMovie('src/views/static/gif/s3.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie3)
        self.giflabel.setVisible(True)
        self.movie3.start()


    def s4(self):
        self.movie4 = QMovie('src/views/static/gif/s4.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie4)
        self.giflabel.setVisible(True)
        self.movie4.start()


    def s5(self):
        self.movie5 = QMovie('src/views/static/gif/s5.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie5)
        self.giflabel.setVisible(True)
        self.movie5.start()
        self.alarm.play()


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