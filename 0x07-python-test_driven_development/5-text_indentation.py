#!/usr/bin/python3


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
    - text: A string representing the input text.

    Raises:
    - TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']

    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in punctuation_chars and i != len(text) - 1:
            print('\n\n', end='')
        i += 1
