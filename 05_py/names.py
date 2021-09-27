"""
Christopher Liu, Ella Krechmer, Ivan Lam
SoftDev
A Program to Print a SoftDev Student's Name
2021-09-27
"""

# SUMMARY:
# I worked with Ella Krechmer and Ivan Lam. We combined the code from each of
# our groups, though we mainly used the approach that my previous group used in
# the first classwork assignment, which was to get the list of names from two
# text files containing lists of names that are specified in the command line.

# DISCOVERIES:
# random.randrage(n) allows us to pick a random int between 0 and n-1,
# inclusive, which is helpful for picking a random index in a list.

# QUESTIONS:
# N/A

# COMMENTS:
# The dictionary data structure specified in the assignment seems to not be the
# most efficient structure at this point, and we didn't originally use it.
# However, it perhaps would be more useful in a large project for better
# scalability.

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
    """Prints a random student name. Takes two lists of names, from the command
    line, where each argument is a path to a file containing a list of names."""
    if len(sys.argv) != 3:
        print("Usage: python names.py pd1_filename pd2_filename")
        return

    # Data structure: a dictionary of periods contiaining the list of students
    # in that period
    periods = {"pd1": read_names(sys.argv[1]), "pd2": read_names(sys.argv[2])}

    # Iterate over the periods to make a list of all of the names
    names = []
    for period in periods.keys():
        names += periods[period]

    # Pick a random name from the list of all names
    name_index = randrange(len(names))
    print(names[name_index])


if __name__ == "__main__":
    main()
