#!/usr/bin/python3
""" contains a function that returns a dictionary"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return obj.__dict__
