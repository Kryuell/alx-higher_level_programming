#!/usr/bin/python3
"""6-load_from_json_file module"""


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    import json
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
