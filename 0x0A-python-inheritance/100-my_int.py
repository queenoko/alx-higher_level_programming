#!/usr/bin/python3
"""MyInt class that inherits from int"""


class MyInt(int):
    """int operators == and != is inverted"""

    def __eq__(self, value):
        """Replace == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Replace!= operator with == behavior"""
        return self.real == value
