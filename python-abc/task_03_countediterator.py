#!/usr/bin/python3
"""
CountedIterator - Keeping Track of Iteration
"""


class CountedIterator:
    """
    CountedtIreator class
    """

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """
        class get_count
        self: self
        """
        return self.counter

    def __next__(self):
        """
        __next__
        self: self
        """
        item = next(self.iterator)
        self.counter += 1
        return item
