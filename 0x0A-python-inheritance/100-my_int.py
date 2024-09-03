#!/usr/bin/python3
"""Class MyInt inherits from int"""

class MyInt(int):
    """Inverts int operators == and !="""

    def __eq__(self, value):
        """Override == operator with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return self.real == value
