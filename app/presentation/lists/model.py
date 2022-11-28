# -*- coding: utf-8 -*-

import pickle
from importlib.machinery import SourceFileLoader

from view_lists import ViewList

p = SourceFileLoader("people", "app/users/people.py").load_module()
# Going crazy with Python's import system!

class Model():
    def __init__(self):
        self.classrooms:list[p.Classroom] = []
        self.current_classroom = p.Classroom()
        self.observer = ViewList()
    
    def save_classrooms(self):
        with open("app/data/classrooms.pickle", "wb") as file:
            pickle.dump(self.classrooms, file)

    def load_classrooms(self):
        with open("app/data/classrooms.pickle", "rb") as file:
            self.classrooms = pickle.load(file)

"""
model_test = Model()
model_test.classrooms = [p.Student("1", "name1", "email1", True, "entry", "exit"), p.Student("2", "name2", "email2", True, "entry", "exit")]
# model_test.save_classrooms()
model_test.load_classrooms()

for i in range(len(model_test.classrooms)):
    print(model_test.classrooms[i])
"""
