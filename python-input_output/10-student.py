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

    def to_json(self, attrs=None):
        """
        method to json
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for attribut in attrs:
            if hasattr(self, attribut):
                new_dict[attribut] = getattr(self, attribut)
        return new_dict
