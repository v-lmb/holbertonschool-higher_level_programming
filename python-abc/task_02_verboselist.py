#!/usr/bin/python3
"""
Extending the Python List with Notifications
"""


class VerboseList(list):
    """
    class VerboseList
    """

    def append(self, item):
        """
        append
        self: self
        item: item
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        extend
        self: self
        iterable: iterable
        """
        super().extend(iterable)
        print(f"Extended list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        remove
        self: self
        item: item
        """
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """
        append
        self: self
        index: index
        """
        item = super().pop(index)
        print(f"Popped [{item}] from index the list.")
        return item
