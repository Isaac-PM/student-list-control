# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from presentation import view_manager as vm

def main():
    app = QApplication(sys.argv)
    my_app = vm.Gui().get_instance()
    my_app.show()
    my_app.setWindowTitle("Student attendance")
    my_app.setWindowIcon(QtGui.QIcon("presentation/students-cap.png"))
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
