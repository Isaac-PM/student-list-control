# -*- coding: utf-8 -*-

class Person:

    # def __init__(self) -> None:
    #     self.id:str = ""
    #     self.name:str = ""
    #     self.email:str = ""
    
    def __init__(self, id:str = "", name:str = "", email:str = "") -> None:
        self.id:str = id
        self.name:str = name
        self.email:str = email
    
    def __str__(self) -> str:
        return f"Person: {self.id}, {self.name}, {self.email}"
    
    def compare(self, person) -> bool:
        return self.id == person.id

class Student(Person):
    # def __init__(self) -> None:
    #     super().__init__()
    #     self.present:bool = False
    #     self.entryTime:str = ""
    #     self.exitTime:str = ""
    
    def __init__(self, id:str = "", name:str = "", email:str = "", present:bool = False, entryTime:str = "", exitTime:str = "") -> None:
        super().__init__(id, name, email)
        self.present:bool = present
        self.entryTime:str = entryTime
        self.exitTime:str = exitTime
    
    def __str__(self) -> str:
        return f"Student: {self.id}, {self.name}, {self.email}, {self.present}, {self.entryTime}, {self.exitTime}"

class Classroom:
    # def __init__(self) -> None:
    #     self.course_id:str = ""
    #     self.teacher:str = Person()
    #     self.students:list[Student] = []
    
    def __init__(self, course_id:str = "", teacher:Person = Person(), students:list[Student] = []) -> None:
        self.course_id:str = course_id
        self.teacher:str = teacher
        self.students:list[Student] = students
    
    def __str__(self) -> str:
        return f"Classroom: {self.course_id}, {self.teacher}, {self.students}"

class Session(Classroom):
    # def __init__(self) -> None:
    #     super().__init__()
    #     self.date:str = ""
    #     self.start:str = ""
    #     self.end:str = ""
    
    def __init__(self, course_id:str = "", teacher:str = "", students:list[Student] = [], date:str = "", start:str = "", end:str = "") -> None:
        super().__init__(course_id, teacher, students)
        self.date:str = date
        self.start:str = start
        self.end:str = end
    
    def __str__(self) -> str:
        return f"Session: {self.course_id}, {self.teacher}, {self.students}, {self.date}, {self.start}, {self.end}"