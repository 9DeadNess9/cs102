from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param coord:
    :return:
    """
    com = choice([(1, 0), (0, 1)])
    cols = len(grid[0])
    posy, posx = coord
    if posy - com[0] >= 1 and posx + com[1] <= cols - 2:
        grid[posy - com[0]][posx + com[1]] = " "
    else:
        if com[0] == 0:
            com = (1, 0)
        else:
            com = (0, 1)
        if posy - com[0] >= 1 and posx + com[1] <= cols - 2:
            grid[posy - com[0]][posx + com[1]] = " "

    return grid


def bin_tree_maze(rows: int = 15, cols: int = 15, random_exit: bool = True) -> List[List[Union[str, int]]]:
    """

    :param rows:
    :param cols:
    :param random_exit:
    :return:
    """

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))

    for cell in empty_cells:
        remove_wall(grid, cell)

    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        if x_in in (0, rows - 1):
            y_in = randint(0, cols - 1)
        else:
            y_in = choice((0, cols - 1))
        if x_out in (0, rows - 1):
            y_out = randint(0, cols - 1)
        else:
            y_out = choice((0, cols - 1))
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1

    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"

    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """
    :param grid:
    :return:
    """

    exits = []
    rows = len(grid)
    cols = len(grid[0])
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "X":
                exits.append((x, y))
    return exits


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """
    :param grid:
    :param k:
    :return:
    """

    rows = len(grid)
    cols = len(grid[0])
    found = 0
    start_k = k
    coords = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == start_k:
                if found == 0:
                    k += 1
                    found = 1
                for coord in coords:
                    if (
                       0 <= x + coord[0] <= rows - 1
                       and 0 <= y + coord[1] <= cols - 1
                       and grid[x + coord[0]][y + coord[1]] == 0
                    ):
                        grid[x + coord[0]][y + coord[1]] = k
    return grid


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """
    :param grid:
    :param exit_coord:
    :return:
    """

    x, y = exit_coord
    start_x, start_y = exit_coord
    k = int(grid[x][y])
    path = [(x, y)]
    found = False
    rows = len(grid)
    cols = len(grid[0])
    coords = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while not found:
        for coord in coords:
            if 0 <= x + coord[0] < rows and 0 <= y + coord[1] < cols and grid[x + coord[0]][y + coord[1]] == k - 1:
                prev_x, prev_y = x, y
                k -= 1
                x += coord[0]
                y += coord[1]
                path.append((x, y))
        if k == 1:
            found = True
    if len(path) > int(grid[start_x][start_y]):
        grid[prev_x][prev_y] = " "
        shortest_path(grid, exit_coord)

    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """

    x, y = coord[0], coord[1]
    rows = len(grid)
    cols = len(grid[0])
    if (x == 0 and y == 0) or (x == 0 and y == rows - 1) or (x == cols - 1 and y == 0) or (x == cols - 1 and y == rows):
        return True
    if y == 0 and grid[x][y + 1] == "■":
        return True
    if y == rows - 1 and grid[x][y - 1] == "■":
        return True
    if x == 0 and grid[x + 1][y] == "■":
        return True
    if x == cols - 1 and grid[x - 1][y] == "■":
        return True
    return False


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """

    rows = len(grid)
    cols = len(grid[0])
    exits = get_exits(grid)
    k = 0
    entrance = exits[0]
    ex = exits[1]
    grid[entrance[0]][entrance[1]] = 1
    if len(exits) == 1:
        return grid, entrance
    else:
        ex = exits[1]

    if encircled_exit(grid, entrance) or encircled_exit(grid, ex):
        return grid, None

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == " " or grid[x][y] == "X":
                grid[x][y] = 0

    while grid[ex[0]][ex[1]] == 0:
        k += 1
        grid = make_step(grid, k)

    return grid, shortest_path(grid, ex)


def add_path_to_grid(
    grid: List[List[Union[str, int]]],
    path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]],
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param path:
    :return:
    """

    if path:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
