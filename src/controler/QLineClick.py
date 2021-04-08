from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QLineEdit

class QLineEditClick(QLineEdit):
    clicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super(QLineEditClick, self).__init__(parent)

    def mousePressEvent(self, event):
        self.act = "Click"

    def mouseReleaseEvent(self, event):
        if self.act == "Click":
            QTimer.singleShot(QApplication.instance().doubleClickInterval(), self.performSingleClickAction)
        else:
            self.clicked.emit(self.act)

    def mouseDoubleClickEvent(self, event):
        self.act = "Double Click"

    def performSingleClickAction(self):
        if self.act == "Click":
            self.clicked.emit(self.act)