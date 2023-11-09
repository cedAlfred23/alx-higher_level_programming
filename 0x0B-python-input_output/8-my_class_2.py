#!/usr/bin/python3
""" My class module
"""


class MyClass:
    """ My class
    """

    score = 0

    def __init__(self, p_name, n = 4):
        self.__name = p_name
        self.number = n
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)
