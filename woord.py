#!/usr/bin/env python
"""
een script waarbij je om input vraagt achter een willekeurig woord en
waarbij het script het woord achterstevoren weergeeft.
"""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


def main():
    WORD = input("Give me a word user ")[::-1]     # Asking for input and what that input is reverse it
    print(WORD)                                    # Printing the input from the user

if __name__ == '__main__':  # code to execute if called from command-line
    main()
