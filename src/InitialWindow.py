import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from HomeWindow import *

class InitialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        with open("style.css") as s:
            self.setStyleSheet(s.read())

        self.title = 'RETEDECON'
        self.width = 1024
        self.height = 600
        self.iniciar()
        self.homeW=HomeWindow()
        self.cambiar()


    def iniciar(self):
        'Dimensions'
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.width, self.height)  # tamaño mínimo
        self.setMaximumSize(self.width, self.height)  # tamaño máximo
        self.setWindowIcon(QIcon("static/favicon3.png"))  # Favicon
        'css linking'
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setObjectName("window")  # nombre que enlaza en css
        'Central Logo set'
        self.label_img_central = QLabel(self)
        self.label_img_central.setGeometry(289, -10,self.width, self.height)
        self.pixmap = QPixmap('static/Logo_central.png')  #Imagen central
        self.label_img_central.setPixmap(self.pixmap)
        ''
        self.show()
        self.timer = QTimer()
        self.timer.setInterval(2500)
        self.timer.setSingleShot(True)
        self.timer.start()
        self.timer.timeout.connect(self.cambiar)

    def cambiar(self):
        self.timer.timeout.connect(self.HomeW)


    def HomeW(self):
        self.homeW.iniciar()
        self.label_img_central.setGeometry(0, 0, 0, 0)  # oculta la imagen
        print(1)
        self.homeW.show()
        self.setVisible(False)

if __name__=='__main__':
    app = QApplication([])
    window = InitialWindow()
    #window.show()
    app.exec_()