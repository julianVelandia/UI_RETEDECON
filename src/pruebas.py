import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QMenu
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 ventana con menu'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.showMaximized()

        menuPrincipal = self.menuBar()
        menuArchivo = menuPrincipal.addMenu('Archivo')

        subMenu = QMenu('Archivo de texto', self)
        subMenuAccion = QAction('Nuevo', self)
        subMenu.addAction(subMenuAccion)
        subMenuAbrir = QAction('Abrir', self)
        subMenu.addAction(subMenuAbrir)
        menuArchivo.addMenu(subMenu)

        exitButton = QAction(QIcon('exit.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        menuArchivo.addAction(exitButton)

        menuAyuda = menuPrincipal.addMenu('Ayuda')
        ayudaAcercade = QAction('Acerca de', self)
        menuAyuda.addAction(ayudaAcercade)

        self.show()

if __name__ == '__main__':
    app = QApplication([])
    window = App()
    window.show()
    app.exec_()