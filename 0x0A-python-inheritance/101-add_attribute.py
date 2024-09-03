#!/usr/bin/python3
"""this module defines a function that adds attribute to objects"""


def add_attribute(obj, att, value):
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add a new attribute")
    setattr(obj, att, value)
