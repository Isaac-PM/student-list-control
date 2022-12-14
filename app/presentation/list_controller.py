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
    
    def load_classroom(self, data) -> None:
        for i in range(len(self.lm_model.classrooms)):
            if data[0] == self.lm_model.classrooms[i].course_id:
                self.lm_model.current_classroom = self.lm_model.classrooms[i]
                return

    def load_classrooms(self) -> None:
        self.lm_model.load_classrooms()

    def save_classroom(self, data) -> None: # Verificar repetidos
        if data[0] == "create":
            for i in range(len(self.lm_model.classrooms)):
                if data[1] == self.lm_model.classrooms[i].course_id:
                    return
            self.lm_model.current_classroom.course_id = data[1]
            self.lm_model.classrooms.append(self.lm_model.current_classroom)
            self.lm_model.save_classrooms()
