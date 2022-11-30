# -*- coding: utf-8 -*-

import pickle
from importlib.machinery import SourceFileLoader

p = SourceFileLoader("people", "app/users/people.py").load_module() # Is this Pythonic?

from presentation import view_manager as vm
# Going crazy with Python's import system...
# import view_manager as vm
# vm = SourceFileLoader("view_manager", "app/presentation/view_manager.py").load_module() # Is this Pythonic?

class Model():
    def __init__(self):
        self.classrooms:list[p.Classroom] = []
        self.current_classroom = p.Classroom()
    
    def save_classrooms(self):
        with open("app/data/classrooms.pickle", "wb") as file:
            pickle.dump(self.classrooms, file)

    def load_classrooms(self):
        try:
            with open("app/data/classrooms.pickle", "rb") as file:
                self.classrooms = pickle.load(file)
        except:
            self.classrooms = []
    