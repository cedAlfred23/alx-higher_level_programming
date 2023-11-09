#!/usr/bin/python3
""" My class module
"""


class MyClass:
    """ My class
    """

    def __init__(self, n):
        self.name = n
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)
