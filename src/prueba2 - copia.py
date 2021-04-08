import sys, os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import matplotlib
matplotlib.use('Qt5Agg') # Make sure that we are using QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class SecondWindow(QWidget):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        # WINDOW SETTINGS
        Form.setWindowTitle('Hello')
        self.p = QPalette()
        self.pixmap = QPixmap(os.getcwd() + "/logo.png").scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.p.setBrush(QPalette.Background, QBrush(self.pixmap))
        self.setPalette(self.p)

        # CREATE FIGURE AND SETTINGS
        self.figure = plt.figure()
        self.figure.patch.set_facecolor('None')
        self.figure.patch.set_alpha(0)
        self.canvas = FigureCanvas(self.figure)
        self.axes = self.figure.add_subplot(111)

        # WINDOW LAYOUT (with H1 and H2)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.canvas,1)
        self.layout().setContentsMargins(50, 50, 50, 50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = SecondWindow()
    form.show()
    sys.exit(app.exec_())