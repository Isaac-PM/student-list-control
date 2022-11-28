# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class Gui(QMainWindow):
    __instance:uic = None

    @staticmethod
    def get_instance():
        if Gui.__instance is None:
            Gui()
        return Gui.__instance

    def __init__(self):
        super().__init__()
        if Gui.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            try:
                Gui.__instance = uic.loadUi("app/presentation/view.ui", self)
            except:
                print ("Unexpected error:", sys.exc_info()[0])