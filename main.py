from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication
# LOCALS
from src.MainWindow import MainWindow
from src.StudentWindow import StudentWindow


def main():
    app = QApplication([])

    screen = app.screens()
    alarm = QSound("src/views/static/alarm.wav")

    student = StudentWindow(alarm)
    window = MainWindow(alarm, student)

    student.showFullScreen()
    window.showFullScreen()

    try:
        student.setGeometry(screen[1].geometry())
        window.setGeometry(screen[0].geometry())
    except Exception as e:
        print(e)
    app.exec_()


if __name__ == '__main__':
    main()
