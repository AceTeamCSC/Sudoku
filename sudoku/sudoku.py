# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.


.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""


# def foo(param1: str) -> str:
#    """Return string with PEP 484 type annotations.

#    Args:
#    param1: The first parameter.

#    Returns:
#        The return value.

#    """
#    if 1 == 0:
#        print("stuff")
#    return param1

import numpy as np
import random


class Sudoku:
    def __init__(self):
        self._attempts_so_far = 0
        # FIXME
        self.empty_numbers = 2
        # max_attempts is the number of times a player can guess incorrectly.
        self._max_attempts = self.empty_numbers + 1
        self._matrix = self.generate()
        assert Sudoku.check_valid_puzzle(self._matrix)
        self._masked_coordinates = set()

    def verify(self, row, column, value):
        return self._matrix[row, column] == value

    def attempt(self, row, column, value):
        if self.verify(row, column, value):
            self._masked_coordinates.remove((row, column))
            print("Correct")
            self.display()

        else:
            print("Incorrect")
            self._attempts_so_far += 1

        print(
            f"There are {self._max_attempts - self._attempts_so_far} attempt(s) left")

    @property
    def attempts_exhausted(self):
        return self._attempts_so_far >= self._max_attempts

    @property
    def in_play(self):
        return self._masked_coordinates != set() and not self.attempts_exhausted

    @staticmethod
    def run():
        s = Sudoku()

        s.remove_random()
        print("Welcome to Sudoku")
        print("Rules:")
        print("All rows should have the digits 1-9, without repition.")
        print("All columns should have the digits 1-9, without repition.")
        print("All 9 sub-matrices should have the digits 1-9, without repition.")
        print(
            "To play, enter the row, column, and answer at the command prompt. The format is: <row> <column> <value>"
        )
        print("Please note this game uses 0 indexing")
        print("Good luck!\n")

        s.display()

        while s.in_play:
            print(s._masked_coordinates)

            response = input("Enter your guess. ")

            if response.count(" ") > 2:
                print("There are too many spaces in your response")
                continue

            response = response.split(" ")

            row = response[0]
            column = response[1]
            value = response[2]

            if not row.isdigit() or not column.isdigit() or not value.isdigit():
                print("Please enter integers only")
                continue

            row = int(row)
            column = int(column)
            if (row, column) not in s._masked_coordinates:
                print("This coordinate is not missing")
                continue

            s.attempt(row=row, column=column, value=int(value))

        print("Game over!")

        if not s.attempts_exhausted:
            print("Winner!")

    @staticmethod
    def generate():
        # generate sudoku puzzle solution
        board = np.zeros(9 * 9, dtype=np.int32).reshape([9, 9])

        # 1. Fill all the diagonal 3x3 matrices.
        # 2. Fill recursively rest of the non-diagonal matrices.
        #    For every cell to be filled, we try all numbers until
        #    we find a safe number to be placed.

        # for i in range(0, 9):
        #    matrix[i, :] = np.random.randint(1, 10, 9)
        # return matrix

        m = 3
        n = m ** 2

        def backtrack_search(c=0):
            i, j = divmod(c, n)
            i0, j0 = i - i % m, j - j % m  # Origin of mxm block
            # Generate a random sample from 1-9 without replacement.
            numbers = np.random.choice(range(1, 10), 9, replace=False)
            block = board[i0: i0 + m, j0: j0 + m]
            for x in numbers:
                if (
                    x not in board[i]  # row
                    and x not in board[:, j]  # column
                    and x not in block
                ):
                    board[i, j] = x

                    # print(f'is valid? {Sudoku.check_valid_puzzle(board)}')
                    print(c, n ** 2)
                    print(board)
                    # if {Sudoku.check_valid_puzzle(board)}:
                    #    return board

                    if c + 1 >= n ** 2 or backtrack_search(c + 1) is not None:
                        # print(f'inside return {c + 1}, {n ** 2}')
                        return board
            else:
                # No result found, need to backtrack
                board[i, j] = 0
                return None

        return backtrack_search()

        # m = 3
        # n = m ** 2
        # board = [[None for _ in range(n)] for _ in range(n)]

        # def search(c=0):
        #    "Recursively search for a solution starting at position c."
        #    i, j = divmod(c, n)
        #    i0, j0 = i - i % m, j - j % m  # Origin of mxm block
        #    numbers = list(range(1, n + 1))
        #    random.shuffle(numbers)
        #    for x in numbers:
        #        if (x not in board[i]  # row
        #                and all(row[j] != x for row in board)  # column
        #                and all(x not in row[j0:j0 + m]  # block
        #                        for row in board[i0:i])):
        #            board[i][j] = x
        #            if c + 1 >= n ** 2 or search(c + 1):
        #                return board
        #    else:
        #        # No number is valid in this cell: backtrack and try again.
        #        board[i][j] = None
        #        return None

        # return search()

    @staticmethod
    def is_valid_array(arr):
        return np.array_equal(sorted(arr), np.arange(1, 10, 1))

    @staticmethod
    def check_valid_puzzle(board):
        # print(Sudoku.is_valid_array(np.array([9,2,4,3,5,6,7,8,1])))
        # print(Sudoku.is_valid_array(np.array([1,2,9,4,5,6,6,8,9])))
        for i in range(9):
            if not Sudoku.is_valid_array(board[i]):
                print(f"not valid row {board[i]}")
                return False

        for i in range(9):
            if not Sudoku.is_valid_array(board[:, i]):
                print(f"not valid column {board[:,i]}")
                return False
        # FIXME block check
        coords = [
            (0, 0),
            (0, 3),
            (0, 6),
            (3, 0),
            (3, 3),
            (3, 6),
            (6, 0),
            (6, 3),
            (6, 6),
        ]
        for i, j in coords:
            block = board[i: i + 3, j: j + 3]
            if not Sudoku.is_valid_array(block.reshape([1, 9])[0]):
                print(
                    f"({i}, {j}) failed because of {block.reshape([1, 9])[0]}")
                return False
        return True

    def remove_random(self):
        # update set of masked coordinates once in the beginning of the game

        while len(self._masked_coordinates) < self.empty_numbers:
            coordinate = random.choice(np.argwhere(np.array(self._matrix) > 0))
            self._masked_coordinates.add(tuple(coordinate))

    def display(self):

        print(self._matrix)

        for row in range(self._matrix.shape[0]):
            for column in range(self._matrix.shape[1]):
                if column == 0:
                    print("|", end=" ")

                if (row, column) in self._masked_coordinates:
                    print("-", end=" ")
                else:
                    print(self._matrix[row, column], end=" ")
                if (column + 1) % 9 == 0:
                    print("|")
                    continue
                if (column + 1) % 3 == 0:
                    print("|", end=" ")

            if (row + 1) % 3 == 0 and row < self._matrix.shape[1] - 1:
                print("  ----- + ----- + -----")


if __name__ == "__main__":
    Sudoku.run()
