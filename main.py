from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication

from src.MainWindow import MainWindow
from src.StudentWindow import StudentWindow

def main():
    app = QApplication([])
    alarm = QSound("src/views/static/alarm.wav")
    window = MainWindow(alarm)
    window.show()
    student = StudentWindow(alarm)
    student.showFullScreen()
    student.show()
    app.exec_()


if __name__ == '__main__':
    main()
