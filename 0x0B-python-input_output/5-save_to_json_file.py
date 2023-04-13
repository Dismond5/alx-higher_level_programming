#!/usr/bin/python3
""" contains a function writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using json"""
    with open(filename, 'w') as f:
        json.dump(my_obj,f)
