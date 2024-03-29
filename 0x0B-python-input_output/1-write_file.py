#!/usr/bin/python3
"""Write_file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns
     the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters
