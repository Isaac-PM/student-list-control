# -*- coding: utf-8 -*-

from importlib.machinery import SourceFileLoader

from presentation import list_model as lm

p = SourceFileLoader("people", "app/users/people.py").load_module()

class Controller():
    def __init__(self, lm_model:lm.Model = lm.Model()):
        self.lm_model = lm_model

    def add_student(self, data:tuple([str, str, str])) -> None:
        if len(self.lm_model.current_classroom.students) == 0:
            self.lm_model.current_classroom.students.append(p.Student(data[0], data[1], data[2]))
            return
        for i in range (len(self.lm_model.current_classroom.students)):
            if data[0] == self.lm_model.current_classroom.students[i].id:
                return
        self.lm_model.current_classroom.students.append(p.Student(data[0], data[1], data[2]))