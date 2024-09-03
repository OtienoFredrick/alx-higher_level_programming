#!/usr/bin/python3
"""The class inherits from lists"""


class MyList(list):
    """The class inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
