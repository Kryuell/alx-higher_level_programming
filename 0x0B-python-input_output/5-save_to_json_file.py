#!/usr/bin/python3
"""5-save_to_json_file module"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation."""
    import json
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
