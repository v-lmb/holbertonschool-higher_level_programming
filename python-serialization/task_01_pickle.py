#!/usr/bin/python3
import pickle


class CustomObject:
    """
    Class for CustomObject
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        method display
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialze(self, filename):
        """
        method serialze
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        method deserialize
        """
        try:
            with open(filename, "rb") as f:
                pickle.load(f)
        except Exception:
            return None
