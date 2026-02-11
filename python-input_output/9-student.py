#!/usr/bin/python3
"""
Student to JSON
"""


class Student:
    """
    class for Student
    self: self
    firs_name: first name of student
    last_name: last_name of student
    age: student's age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        method to json
        """
        return self.__dict__
