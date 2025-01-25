import pytest
from minesweeper import minesweeper


@pytest.mark.parametrize("scenario, gridSize, mines, expected", [
    ("Empty grid", [0, 0], [], []),
    ("No mines", [2, 2], [], [[".", "."], [".", "."]]),
    ("1 mine", [1, 1], [[0, 0]], [["*"]]),
    ("1 mine, 2by1 grid", [2, 1], [[0, 0]], [["*", 1]]),
    ("1 mine, 3by2 grid", [3, 2], [[1, 0]], [[1, "*", 1], [1, 1, 1]]),
    ("2 mines, 3by2 grid", [3, 2], [
     [1, 0], [1, 1]], [[2, "*", 2], [2, "*", 2]]),
    ("3 mines, 5by3 grid", [5, 3], [[0, 0], [1, 0], [1, 2]], [
        ["*", "*", 1, ".", "."],
        [3, 3, 2, ".", "."],
        [1, "*", 1, ".", "."]
    ]),
])
def test_minesweeper_scenarios(scenario, gridSize, mines, expected):
    print(scenario)
    assert minesweeper(gridSize, mines) == expected


# def test_empty_grid():
#     assert minesweeper([0, 0], []) == []

# def test_no_mines():
#     assert minesweeper([2, 2], []) == [[".", "."], [".", "."]]

# def test_1_mine():
#     assert minesweeper([1, 1], [[0, 0]]) == [["*"]]

# def test_1_mine_in_2by2_grid():
#     assert minesweeper([2, 1], [[0, 0]]) == [["*", 1]]

# def test_1_mine_in_3by2_grid():
#     assert minesweeper([3, 2], [[1, 0]]) == [[1, "*", 1], [1, 1, 1]]

# def test_2_mines_in_3by2_grid():
#     assert minesweeper([3, 2], [[1, 0], [1, 1]]) == [[2, "*", 2], [2, "*", 2]]

# def test_3_mines_in_5by3_grid():
#     assert minesweeper([5, 3], [[0, 0], [1, 0], [1, 2]]) == [
#         ["*", "*", 1, ".", "."],
#         [3, 3, 2, ".", "."],
#         [1, "*", 1, ".", "."]
#     ]
