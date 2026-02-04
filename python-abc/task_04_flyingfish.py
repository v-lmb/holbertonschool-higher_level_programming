#!/usr/bin/python3
"""
The Enigmatic FlyingFish
"""
from abc import ABC, abstractmethod


class Fish(ABC):
    """
    Abstract Class Fish
    """
    def __init__(self):
        pass

    @abstractmethod
    def swim(self):
        """
        Swim Method
        self: self
        """
        print("The fish is swimming")

    @abstractmethod
    def habitat(self):
        """
        habitat Method
        self: self
        """
        print("The fish lives in water")


class Bird(ABC):
    """
    Abstract Class Bird
    """
    def __init__(self):
        pass

    @abstractmethod
    def fly(self):
        """
        fly Method
        self: self
        """
        print("The bird is flying")

    @abstractmethod
    def habitat(self):
        """
        habitat Method
        self: self
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish Class
    """
    def __init__(self):
        pass

    def fly(self):
        """
        fly Method
        self: self
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Swim Method
        self: self
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        habitat Method
        self: self
        """
        print("The flying fish lives both in water and the sky!")
