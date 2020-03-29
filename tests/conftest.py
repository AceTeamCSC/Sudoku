# -*- coding: utf-8 -*-

import numpy as np
import pytest

from sudoku.sudoku import Sudoku


@pytest.fixture
def sudoku_board():
    s = Sudoku()
    # creates numpy array [[1 2 3] [4 5 6]].
    s._matrix = np.arange(1, 7, 1).reshape([2, 3])

    return s
