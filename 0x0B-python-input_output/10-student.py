#!/usr/bin/python3
"""Module 10-student.
Creates a Student class."""


class Student:
    """Class that defines a student.
    Public attributes:
        - first_name
        - last_name
        - age
    Public method to_json()."""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation
        of a Student instance.
        Args:
            - attrs: list of attributes
        Returns: the dict representation of the instance."""

        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()
