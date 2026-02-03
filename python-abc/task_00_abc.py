#!/usr/bin/python3
"""
Setting up the Abstract Class:
Import the necessary components from the abc module.
Define the Animal class, ensuring it inherits from ABC to mark it as abstract.
Inside the Animal class, declare an abstract method name
sound using the @abstractmethod decorator.
Implementing the Subclasses:
Create a subclass named Dog that inherits from the Animal class.
Implement the sound method in the Dog class to return the string “Bark”.
Similarly, create a subclass named Cat that also inherits from the Animal class
Implement the sound method in the Cat class to return the string “Meow”.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract Class Animal
    """
    def __init__(self):
        pass

    @abstractmethod
    def sound(self):
        """
        Dog Class
        """
        pass


class Dog(Animal):
    """
    Dog Class
    """
    def __init__(self):
        pass

    def sound(self):
        """
        Dog Sound
        """
        super().sound()
        return ("Bark")


class Cat(Animal):
    """
    Cat Class
    """
    def __init__(self):
        pass

    def sound(self):
        """
        Cat Sound
        """
        super().sound()
        return ("Meow")
