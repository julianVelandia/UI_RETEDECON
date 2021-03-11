from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys




class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp,self).__init__(parent = parent)
        
        with open("style.css") as f:
            self.setStyleSheet(f.read())


        self.setMinimumSize(1024,600)    #tamaño mínimo
        self.setMaximumSize(1024,600)  #tamaño máximo
        self.setWindowTitle('Input')   #titulo

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setObjectName("window")


        self.ingresar = QPushButton('ingreso',self.centralWidget)
        self.ingresar.setGeometry(72, 606-66, 238, 66)
        self.ingresar.setObjectName("bingresar")

        self.estatus = QPushButton('status',self.centralWidget)
        self.estatus.setGeometry(310, 606-66, 238, 66)
        self.estatus.setObjectName("bestatus")


        self.estatus = QPushButton('estatus',self.centralWidget)
        self.estatus.setGeometry(548, 606-66, 238, 66)
        self.estatus.setObjectName("bestatus")

        self.estatus = QPushButton('estatus',self.centralWidget)
        self.estatus.setGeometry(786, 606-66, 238, 66)
        self.estatus.setObjectName("bestatus")

if __name__=='__main__':
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()