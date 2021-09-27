"""
Christopher Liu, Lucas Lee, Lucas Tom-Wong, Zhaoyu Lin
SoftDev
A Program to Print a SoftDev Student's Name
2021-09-21
"""

import sys
from random import randrange


def read_names(filename: str):
    """Reads a text file containing a list of names, where each line contains
    one name, and returns a list of the names."""
    file_contents = ""
    with open(filename, "r") as f:
        file_contents = f.read()
    names = file_contents.split("\n")

    # Remove empty lines
    names = [name for name in names if name]
    return names


def main():
    """Prints a random student name given two files containing lists of names,
    where each line contains one name."""
    if len(sys.argv) != 3:
        print("Usage: python names.py pd1_filename pd2_filename")
        return

    pd1 = read_names(sys.argv[1])
    pd2 = read_names(sys.argv[2])
    names = pd1 + pd2

    # Pick a random name from the list of pd1 and pd2 names
    name_index = randrange(len(names))
    print(names[name_index])


if __name__ == "__main__":
    main()
