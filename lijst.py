#!/usr/bin/env python
"""
Printing out a list in a list
"""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"

def main():
    list = [['.', '.', '.', '.', '.', '.'],
             ['.', 'O', 'O', '.', '.', '.'],
             ['O', 'O', 'O', 'O', '.', '.'],
             ['O', 'O', 'O', 'O', 'O', '.'],
             ['.', 'O', 'O', 'O', 'O', 'O'],
             ['O', 'O', 'O', 'O', 'O', '.'],
             ['O', 'O', 'O', 'O', '.', '.'],
             ['.', 'O', 'O', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.']]


    print("now which matrix do you want to do?")

    print("1. 90 degrees")
    print("2. 270 degrees")

    pick = input()


    # # Reverse 90 degrees
    if pick == "1":
        for x in range(6):                                 # 6 values bij the X-comme
            for y in range(9):                             # 9 values bij the Y-comme
                if y < 8:
                    print(list[y][-(x + 1)], end="")       # Print out the matrix but 90 degrees anti-clockwise
                else:
                    print(list[y][x])

    print("\n")

    # Reverse 270 degrees
    if pick == "2":
        for x in range(6):                                 # 6 values bij the X-comme
             for y in range(9):                            # 9 values bij the Y-comme
                if y < 8:
                    print(list[y][+(x)], end="")           # Print out the matrix but 90 degrees clockwise
                else:
                    print(list[y][x])

if __name__ == '__main__':  # code to execute if called from command-line
    main()