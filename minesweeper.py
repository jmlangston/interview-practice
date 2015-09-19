# in: a list of lists that represents a minesweeper board where 0 is a cell without a mine and 1 is a cell with a mine
# out: a list of lists mirroring the input where a mine is represented by 'x' and cells without mines are represented by the number of mines in the surrounding cells

# example:
# input =   [   [0, 0, 1, 0],
#               [0, 1, 1, 0],
#               [1, 0, 0, 0],
#               [1, 0, 0, 0]]

# output =  [   [1, 3, 'x', 2],
#               [2, 'x', 'x', 2],
#               ['x', 4, 2, 1],
#               ['x', 2, 0, 0]]


def minesweeper(grid):

    cells = get_cells(grid)

    output_grid = make_grid()

    for cell in cells:
        if grid[cell[0]][cell[1]] == 1:
            output_grid[cell[0]][cell[1]] = 'x'
        else:
            lst = list_of_indices(cell)
            for item in lst:
                if is_valid(item) is True:
                    output_grid[cell[0]][cell[1]] += grid[cell[0]][cell[1]]

    return output_grid


def get_cells(grid):

    cells = []

    for y, row in enumerate(grid):
        for x, mine in enumerate(row):
            cells.append((x,y))

    return cells


def list_of_indices(x, y):

    return[(x+i, y+j) for i in range(-1, 2) for j in range(-1, 2)]


def is_valid(cell, size):

    (x, y) = cell

    if x == -1 or y == -1 or x == size or y == size:
        return False
    return True
