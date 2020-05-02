"""Tests for sudoku.py."""

import builtins

import mock
import numpy as np

from sudoku.sudoku import Sudoku


def is_valid_array(arr):
    return np.array_equal(sorted(arr), np.arange(1, 10, 1))


def check_valid_puzzle(board):
    # Check that all digits 1-9 are represented in the row and are not duplicated.
    for i in range(9):
        if not is_valid_array(board[i]):
            return False

    # Check that all digits 1-9 are represented in the column and are not duplicated.
    for i in range(9):
        if not is_valid_array(board[:, i]):
            return False

    coords = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    # Check that all digits 1-9 are represented in the subset and are not duplicated.
    for i, j in coords:
        block = board[i : i + 3, j : j + 3]
        if not is_valid_array(block.reshape([1, 9])[0]):
            return False
    return True


def test_generate():
    """Test the generate algorithm is correct."""
    assert check_valid_puzzle(Sudoku.generate())


def test_verify_true(sudoku_board):
    s = sudoku_board

    # Correct guess
    assert s.verify(row=0, column=0, value=1)


def test_verify_false(sudoku_board):
    s = sudoku_board

    # Incorrect guess
    assert not s.verify(row=0, column=0, value=8)


def test_attempt_true(sudoku_board):
    s = sudoku_board
    s._masked_coordinates = {(0, 0)}
    s._attempts_so_far = 3
    # Correct guess
    s.attempt(row=0, column=0, value=1)

    # The _attempts_so_far count is unchanged since the guess was correct.
    assert sudoku_board._attempts_so_far == 3


def test_attempt_false(sudoku_board):
    s = sudoku_board
    s._attempts_so_far = 3
    # Incorrect guess
    s.attempt(row=0, column=0, value=8)

    # The _attempts_so_far count has increased by one since the guess was incorrect.
    assert s._attempts_so_far == 4


def test_attempts_exhausted_true(sudoku_board):
    """The _attempts_so_far is less than _max_attempts and therefore
    attempts_exhausted() is False."""
    s = sudoku_board
    s._attempts_so_far = 5
    s._max_attempts = 6

    assert not s.attempts_exhausted


def test_attempts_exhausted_false(sudoku_board):
    """The _attempts_so_far is greater than _max_attempts and
    therefore attempts_exhausted() is True."""
    s = sudoku_board
    s._attempts_so_far = 3
    s._max_attempts = 2

    assert s.attempts_exhausted


def test_in_play_masked_coordinates_exist_and_attempts_exist(sudoku_board):
    """in_play will be True since there are still missing coordinates and
    attempts_exhausted is False."""
    s = sudoku_board
    # A masked coordinate needs to be found.
    s._masked_coordinates = {(0, 0)}
    # Still chances to guess.
    s._max_attempts = 2
    s._attempts_so_far = 1

    # Continue playing.
    assert s.in_play


def test_in_play_coordinates_unmasked_empty_and_attempts_exist(sudoku_board):
    """in_play will be False since there are no masked_coordinates, even though
    attempts_exhausted is False."""
    s = sudoku_board
    # All masked coordinates found.
    s._masked_coordinates = set()
    # Still chances to guess.
    s._max_attempts = 2
    s._attempts_so_far = 1

    # Game over - win.
    assert not s.in_play


def test_in_play_masked_coordinates_exist_and_attempts_exhausted(sudoku_board):
    """in_play will be False since attempts_exhausted is True, even though
    masked_coordinates exist."""
    s = sudoku_board
    # A masked coordinate needs to be found.
    s._masked_coordinates = {(0, 0)}
    # No more chances to guess.
    s._max_attempts = 1
    s._attempts_so_far = 1

    # Game over - lose.
    assert not s.in_play


def test_in_play_coordinates_unmasked_empty_and_attempts_exhausted(sudoku_board):
    """in_play will be False since attempts_exhausted is True and there are no
    masked_coordinates."""
    s = sudoku_board
    # All masked coordinates found.
    s._masked_coordinates = set()
    # No more chances to guess.
    s._max_attempts = 1
    s._attempts_so_far = 1

    # Game over - win.
    assert not s.in_play


def test_display(capsys):
    """Test board image."""
    s = Sudoku()
    s._matrix = np.zeros(9 * 9, dtype=np.int32).reshape([9, 9])

    sudoku_image = """\
| 0 0 0 | 0 0 0 | 0 0 0 |
| 0 0 0 | 0 0 0 | 0 0 0 |
| 0 0 0 | 0 0 0 | 0 0 0 |
  ----- + ----- + -----
| 0 0 0 | 0 0 0 | 0 0 0 |
| 0 0 0 | 0 0 0 | 0 0 0 |
| 0 0 0 | 0 0 0 | 0 0 0 |
  ----- + ----- + -----
| 0 0 0 | 0 0 0 | 0 0 0 |
| 0 0 0 | 0 0 0 | 0 0 0 |
| 0 0 0 | 0 0 0 | 0 0 0 |
"""

    s.display()
    out, err = capsys.readouterr()
    assert out == sudoku_image


def test_remove_random():
    """Testing the set of coordinates to be removed."""
    s = Sudoku()
    s.empty_numbers = 2
    s._matrix = np.arange(1, 3, 1).reshape([1, 2])

    s.remove_random()
    # The assertion checks the complete list of coordinates so random doesn't have to
    # be mocked.
    assert s._masked_coordinates == {(0, 1), (0, 0)}


def test_info_message(sudoku_board):
    s = sudoku_board
    welcome_message = """
        Welcome to Sudoku
        Rules:
        All rows should have the digits 1-9, without repetition.
        All columns should have the digits 1-9, without repetition.
        All 9 sub-matrices should have the digits 1-9, without repetition.
        To play, enter the row, column, and answer at the command prompt. The
        Format is: <row> <column> <value>
        Type exit to leave
        Please note this game uses 0 indexing
        Good luck!\n
        """
    assert s.intro_message() == welcome_message


def test_run():
    s = Sudoku()

    with mock.patch.object(builtins, "input", lambda _: "exit"):
        assert s.run() is exit()
