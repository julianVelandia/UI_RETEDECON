from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication

from src.MainWindow import MainWindow
from src.StudentWindow import StudentWindow
from src.communication.PySerialmain import Read, UNO

def main():
    app = QApplication([])
    alarm = QSound("src/views/static/alarm.wav")
    student = StudentWindow(alarm)
    student.showFullScreen()
    student.show()
    window = MainWindow(alarm,student)
    window.show()
    app.exec_()
    re = Read(window)
    re.execute()


if __name__ == '__main__':
    main()
