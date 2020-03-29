# -*- coding: utf-8 -*-
"""A game of Sudoku against the computer."""


import random

import numpy as np


class Sudoku:
    def __init__(self):
        self._attempts_so_far = 0
        # FIXME
        # Lower this number when testing.
        self.empty_numbers = 4
        # _guess_padding is the number of guesses of a perfect game.
        self._guess_padding = 1
        # _max_attempts is the number of times a player can guess incorrectly.
        self._max_attempts = self.empty_numbers + self._guess_padding
        self._matrix = self.generate()
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

        print(f"There are {self._max_attempts - self._attempts_so_far} attempt(s) left")

    @property
    def attempts_exhausted(self):
        return self._attempts_so_far >= self._max_attempts

    @property
    def in_play(self):
        return self._masked_coordinates != set() and not self.attempts_exhausted

    @staticmethod
    def intro_message():
        welcome_message = """
        Welcome to Sudoku
        Rules:
        All rows should have the digits 1-9, without repition.
        All columns should have the digits 1-9, without repition.
        All 9 sub-matrices should have the digits 1-9, without repition.
        To play, enter the row, column, and answer at the command prompt. The
        Format is: <row> <column> <value>
        Type exit to leave
        Please note this game uses 0 indexing
        Good luck!\n
        """
        return welcome_message

    @staticmethod
    def run():
        s = Sudoku()
        user_exit = False
        s.remove_random()
        print(s.intro_message())
        s.display()

        while s.in_play:
            print(s._masked_coordinates)
            response = input("Enter your guess. ")

            if response == "exit":
                print("Goodbye")
                user_exit = True
                break

            if response.count(" ") > 2:
                print("There are too many spaces in your response")
                continue

            try:
                response = response.split(" ")
                row = response[0]
                column = response[1]
                value = response[2]
            except IndexError:
                print("Invalid response")
                continue

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
        if not s.attempts_exhausted and not user_exit:
            print("Winner!")

    @staticmethod
    def generate():
        # generate sudoku puzzle solution
        board = np.zeros(9 * 9, dtype=np.int32).reshape([9, 9])

        def backtrack_search(constraint=0):
            i, j = divmod(constraint, 9)
            i0, j0 = i - i % 3, j - j % 3  # Origin of subset
            # Generate a random sample from 1-9 without replacement.
            numbers = np.random.choice(range(1, 10), 9, replace=False)
            subset = board[i0 : i0 + 3, j0 : j0 + 3]
            for x in numbers:
                if (
                    x not in board[i]  # row
                    and x not in board[:, j]  # column
                    and x not in subset  # subset
                ):
                    board[i, j] = x

                    if (
                        constraint + 1 >= 9 ** 2
                        or backtrack_search(constraint + 1) is not None
                    ):
                        return board
            else:
                # No result found, need to backtrack
                board[i, j] = 0
                return None

        return backtrack_search()

    def remove_random(self):
        # Update set of masked coordinates once in the beginning of the game.

        while len(self._masked_coordinates) < self.empty_numbers:
            coordinate = random.choice(np.argwhere(np.array(self._matrix) > 0))
            self._masked_coordinates.add(tuple(coordinate))

    def display(self):
        # FIXME
        # Uncomment this for testing. Uncommenting this will make the display test fail
        # print(self._matrix)

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
