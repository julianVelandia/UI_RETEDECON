from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from configparser import ConfigParser
# locals
from src.views.botones.inicio.boton import Boton
from src.views.teclado.teclado_numeros import TecladoNumeros
from src.views.teclado.teclado_letras import TecladoLetras

# informacion de las pantallas
# from screeninfo import get_monitors
import ctypes


class StudentWindow(QMainWindow, Boton, TecladoNumeros, TecladoLetras):  # Ventana principal
    def __init__(self, alarm, parent=None, *args):
        super(StudentWindow, self).__init__(parent=parent)
        with open("src/views/static/styles.css") as f:
            self.setStyleSheet(f.read())

        self.cedula_cache = ''
        self.carnet = ''
        self.title = 'RETEDECON'
        self.config = ConfigParser()
        # self.width = get_monitors()[0].width
        # self.height = get_monitors()[0].height
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        self.width = user32.GetSystemMetrics(0)
        self.height = user32.GetSystemMetrics(1)

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

        # # Mensajes
        # self.dialogo_mensaje = 'Error404'
        # self.dialogo = QMessageBox(self.centralWidget)
        # self.dialogo.setWindowTitle('RETEDECON')
        # self.dialogo.addButton("Aceptar", 0)
        # self.dialogo.setInformativeText(self.dialogo_mensaje)

        # Estados

        self.widthGif = 207
        self.heightGif = 207

        # s0
        self.giflabel = QLabel(self.centralWidget)
        self.movie0 = QMovie('src/views/static/gif/s0.gif')  # Gif paso 1
        self.giflabel.setGeometry(self.width / 2 - self.widthGif / 2, self.height / 2 - self.heightGif / 2,
                                  self.widthGif, self.heightGif)
        self.giflabel.setMovie(self.movie0)
        self.giflabel.setVisible(False)

        self.state = 0

        # Imagen central
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
        self.timer.timeout.connect(self.checkState)  # función a ejecutar pasados los 3 seg

        # Solo para pruebas
        self.botonesPrueba(self.centralWidget)