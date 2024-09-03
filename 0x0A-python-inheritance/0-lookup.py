#!/usr/bin/python3
""" Funtion that returns list of avaialble attributes of a an object"""


def lookup(obj):
    """The function returns all attributes and methods of an object"""
    return dir(obj)
