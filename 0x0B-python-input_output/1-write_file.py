#!/usr/bin/python3
"""Module containing the function write_file"""


def write_file(file_name="", e_text=""):
    """Writes a string to a text file (UTF8) and returns the number
    of characters written.

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): string of text to write to file. Defaults to "".

    Returns:
        int: number of characters written to file.
    """
    with open(file_name, 'w', encoding="utf-8") as f:
        """This method returns the number of characters written to a file."""
        return f.write(e_text)
