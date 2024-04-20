#!/usr/bin/python3
# 0-square.py
"""Defines a square """


class Square:
    """The class defines a square"""
    def __init__(self, size=0):
        """Initializing square class
        Args:
            size - Represents the size if the square defines
        Raises:
            Type Error: if size is not an integer
        Value Error:
            If size is not an integer
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
