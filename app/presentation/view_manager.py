# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from importlib.machinery import SourceFileLoader

from presentation import list_model as lm
from presentation import list_controller as lc

p = SourceFileLoader("people", "app/users/people.py").load_module()

def list_table_model_parser(classroom_students:list[p.Student]):
    data:list[list] = []
    for i in range(len(classroom_students)):
        data.append([classroom_students[i].id, classroom_students[i].name, classroom_students[i].email])
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
                self.existing_radio_button.clicked.connect(lambda:self.manage_radio_buttons())
                self.create_radio_button.clicked.connect(lambda:self.manage_radio_buttons())
                self.add_student_button.clicked.connect(lambda:self.add_student())
                self.save_button.clicked.connect(lambda:self.save_classroom())
                self.existing_combo_box.currentIndexChanged.connect(lambda:self.load_classroom())
                # self.existing_combo_box.set_default_text("Select a classroom")
                self.create_line_edit.setEnabled(False)
                self.existing_combo_box.setEnabled(False)
                self.list_controller.load_classrooms()
                self.update(["start"])
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
        if not self.existing_radio_button.isChecked() and not self.create_radio_button.isChecked():
            self.existing_radio_button.setStyleSheet("border: 1px solid red;")
            self.create_radio_button.setStyleSheet("border: 1px solid red;")
            return
        if self.create_radio_button.isChecked() and self.create_line_edit.text() == "":
            self.create_line_edit.setStyleSheet("border: 1px solid red;")
            return
        if self.existing_radio_button.isChecked() and self.existing_combo_box.currentText() == "":
            self.existing_combo_box.setStyleSheet("border: 1px solid red;")
            return
        data:tuple([str, str, str]) = (self.id_line_edit.text(), self.name_line_edit.text(), self.email_line_edit.text())
        if data[0] == "" or data[1] == "" or data[2] == "":
            if data[0] == "": self.id_line_edit.setStyleSheet("border: 1px solid red;")
            if data[1] == "": self.name_line_edit.setStyleSheet("border: 1px solid red;")
            if data[2] == "": self.email_line_edit.setStyleSheet("border: 1px solid red;")
            return
        else:
            self.list_controller.add_student(data)
            self.update(["add_student"])

    def save_classroom(self) -> None:
        if self.create_radio_button.isChecked() and self.create_line_edit.text() == "":
            self.create_line_edit.setStyleSheet("border: 1px solid red;")
            return
        """
        modo: si es crear una nueva o usar una existente
        nombre de la clase
        lista de estudiantes
        
        """
        if self.create_radio_button.isChecked():
            data:tuple([str, str]) = ("create", self.create_line_edit.text())
            self.list_controller.save_classroom(data)
    
    def load_classroom(self) -> None:
        data:tuple([str]) = (self.existing_combo_box.currentText())
        self.list_controller.load_classroom(data)
        self.update(["load_classroom"])

    def update(self, args:list = []) -> None:
        if args[0] == "start":
            if len(self.list_model.classrooms) != 0:
                self.existing_combo_box.currentIndexChanged.disconnect()
                self.existing_combo_box.clear()
                self.existing_combo_box.addItems([classroom.course_id for classroom in self.list_model.classrooms])
                self.existing_combo_box.currentIndexChanged.connect(lambda:self.load_classroom())
        
        if args[0] == "add_student" or args[0] == "start":
            if len(self.list_model.current_classroom.students) == 0: return
            data:list[list] = list_table_model_parser(self.list_model.current_classroom.students)
            self.student_table.setRowCount(len(data))
            self.student_table.setColumnCount(len(data[0]))
            for i in range(len(data)):
                self.student_table.setItem(i, 0, QTableWidgetItem(data[i][0]))
                self.student_table.setItem(i, 1, QTableWidgetItem(data[i][1]))
                self.student_table.setItem(i, 2, QTableWidgetItem(data[i][2]))
            header = self.student_table.horizontalHeader()       
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        
        if args[0] == "load_classroom":
            self.update(["start"])