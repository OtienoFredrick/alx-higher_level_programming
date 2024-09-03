#!/usr/bin/python3
"""The function returns true if object is an instance of,
or if the object is an instance of a class that inherited
from the specified class"""


def is_kind_of_class(obj, a_class):
    return (isinstance(obj, a_class))
