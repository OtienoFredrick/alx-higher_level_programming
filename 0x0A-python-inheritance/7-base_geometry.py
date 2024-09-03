#!/usr/bin/python3
"""class BaseGeometry with a public instance method"""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implimented")

    def integer_validator(self, name, value):
        """validates a value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
