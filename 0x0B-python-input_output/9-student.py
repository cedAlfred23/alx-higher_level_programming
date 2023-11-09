#!/usr/bin/python3
"""Module defining the class Student"""


class Student:
    """
    Class that defines properties of student.

    Attributes:
        first_name (str): first name of student.
        last_name (int): last name of student.
        age (int): age of student.
    """
    def __init__(self, f_name, l_name, age):
        """Creates new instances of Student.

        Args:
            first_name (str): first name of student.
            last_name (int): last name of student.
            age (int): age of student.
        """
        self.first_name = f_name
        self.last_name = l_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: dictionary representation.
        """
        return self.__dict__
