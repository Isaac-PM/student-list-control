# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from importlib.machinery import SourceFileLoader

from presentation import list_model as lm
from presentation import list_controller as lc
from presentation import list_table_model as ltm

p = SourceFileLoader("people", "app/users/people.py").load_module()

def list_table_model_parser(classroom_students:list[p.Student]):
    data:list[list] = []
    for i in range(len(classroom_students)):
        data.append([classroom_students[i].id, classroom_students[i].name, classroom_students[i].email])
    print(data)
    return data

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
                self.list_model = lm.Model()
                self.list_controller = lc.Controller(self.list_model)
                self.list_model.load_classrooms()
                self.existing_combo_box.addItems([classroom.course_id for classroom in self.list_model.classrooms])
                self.student_table.setModel(ltm.TableModel(list_table_model_parser(self.list_model.current_classroom.students)))
                self.existing_radio_button.clicked.connect(lambda:self.manage_radio_buttons())
                self.create_radio_button.clicked.connect(lambda:self.manage_radio_buttons())
                self.add_student_button.clicked.connect(lambda:self.add_student())
            except:
                print ("Unexpected error:", sys.exc_info()[0])

    def manage_radio_buttons(self) -> None:
        if self.existing_radio_button.isChecked():
            self.create_line_edit.setEnabled(False)
            self.existing_combo_box.setEnabled(True)
        elif self.create_radio_button.isChecked():
            self.create_line_edit.setEnabled(True)
            self.existing_combo_box.setEnabled(False)

    def add_student(self) -> None:
        data:tuple([str, str, str]) = (self.id_line_edit.text(), self.name_line_edit.text(), self.email_line_edit.text())
        if data[0] == "" or data[1] == "" or data[2] == "":
            if data[0] == "": self.id_line_edit.setStyleSheet("border: 1px solid red;")
            if data[1] == "": self.name_line_edit.setStyleSheet("border: 1px solid red;")
            if data[2] == "": self.email_line_edit.setStyleSheet("border: 1px solid red;")
        else:
            self.list_controller.add_student(data)
        list_table_model_parser(self.list_model.current_classroom.students)
        self.update(["add_student"])

    def update(self, args:list = []) -> None:
        if args[0] == "add_student":
            # pass
            self.student_table.setModel(ltm.table_model(list_table_model_parser(self.list_model.current_classroom.students)))

        return
    