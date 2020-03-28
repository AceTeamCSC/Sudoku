"""Tests for sudoku.py."""

from sudoku.sudoku import Sudoku

def test_is_valid_array():
    assert Sudoku.is_valid_array([1]) == False