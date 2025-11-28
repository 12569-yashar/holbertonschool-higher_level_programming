#!/usr/bin/python3
"""salam"""


class Student:
    """salam"""

    def __init__(self, first_name, last_name, age):
        """salam"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ salam"""
        return self.__dict__.copy()
