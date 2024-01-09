#!/usr/bin/python3
"""Append_after module """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line
     containing a specific string.
    """
    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
        file.seek(0)
        file.writelines(new_lines)
        file.truncate()
