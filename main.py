import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from presentation import *

class gui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("presentation/view.ui", self)

def main():
    app = QApplication(sys.argv)
    my_app = gui()
    my_app.show()
    my_app.setWindowTitle("Student attendance")
    my_app.setWindowIcon(QtGui.QIcon("presentation/students-cap.png"))
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()