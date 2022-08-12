from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from configparser import ConfigParser
# locals
from src.views.botones.inicio.boton import Boton
from src.views.teclado.teclado_numeros import TecladoNumeros
from src.views.teclado.teclado_letras import TecladoLetras
from src.views.botones.estudiantes.funcionesEstudiantes import FuncionesEstudiantes
from src.communication.PySerialmain import Read, UNO
from src.views.botones.inicio.funciones import Funciones
import threading
# informacion de las pantallas
from screeninfo import get_monitors


class StudentWindow(QMainWindow, Boton, TecladoNumeros, TecladoLetras, Read,UNO,FuncionesEstudiantes):  # Ventana principal
    def __init__(self, alarm, parent=None, *args):
        super(StudentWindow, self).__init__(parent=parent)
        with open("src/views/static/styles.css") as f:
            self.setStyleSheet(f.read())

        self.cedula_cache = ''
        self.carnet = ''
        self.title = 'RETEDECON'
        self.config = ConfigParser()
        self.width = get_monitors()[1].width
        self.height = get_monitors()[1].height

        # alarma
        self.alarm = alarm

        self.setMinimumSize(self.width, self.height)  # tamaño mínimo
        self.setMaximumSize(self.width, self.height)  # tamaño máximo
        self.setWindowTitle(self.title)  # titulo
        self.setWindowIcon(QIcon("src/views/static/icons/favicon3.png"))  # Favicon

        # Widget principal
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setObjectName("window")  # nombre que enlaza en css

        # s0
        self.giftEstudiantes(self.centralWidget)
        self.state = 0

        # Imagen central
        self.labelEsquina(self.centralWidget)
        self.label_img_central = QLabel(self)
        self.pixmap = QPixmap('src/views/static/icons/Logo_central.png')  # Imagen central
        self.label_img_central.setGeometry(self.width / 2 - self.pixmap.width() / 2,
                                           self.height / 2 - self.pixmap.height() / 2, self.pixmap.width(),
                                           self.pixmap.height())
        self.label_img_central.setPixmap(self.pixmap)
        self.label_img_central.setVisible(True)

        # Timer animación
        self.timer = QTimer()
        self.timer.setInterval(2500)
        self.timer.setSingleShot(True)
        self.timer.start()
        self.timer.timeout.connect(self.s0)  # función a ejecutar pasados los 3 seg

        # textos
        self.textosEstado(self.centralWidget)

        # labels camara
        self.labelsCamara(self.centralWidget)
        
        FuncionesEstudiantes.__init__(self)
        self.started.connect(self.startC)
        self.s4Signal.connect(self.startS4)
        
    def startC(self):
        threading.Thread(target=self.s1(), daemon=False).start()
    def startS4(self):
        threading.Thread(target=self.s4(), daemon=False).start()