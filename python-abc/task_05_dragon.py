#!/usr/bin/python3
"""
The Mystical Dragon
"""


class SwimMixin:
    """
    class SwimMixin
    """
    def __init__(self):
        pass

    def swim(self):
        """
        Swim Method
        self: self
        """
        print("The creature swims!")


class FlyMixin:
    """
    class FlyMixin
    """
    def __init__(self):
        pass

    def fly(self):
        """
        Fly Method
        self: self
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    class Dragon
    """
    def __init__(self):
        pass

    def roar(self):
        """
        Roar Method
        self: self
        """
        print("The dragon roars!")
