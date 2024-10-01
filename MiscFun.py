from CellClass import Cell # Imports Cell class
import math # Mathematical functions

# Fills the cell_list with Cell objects
def fill_cell_list(rows, cols, cell_list, state, signal, disabled):
    for i in range(rows):
        inner = []
        for j in range(cols):
            inner.append(Cell(state, signal, disabled))
        cell_list.append(inner)

# Adds neighbors to each cell in cell_list
def fill_cell_list_neighbors(rows, cols, cell_list, specifier, diagonal=False):
    for i in range(rows):
        for j in range(cols):
            # Adds adjacent neighbors if within bounds
            # Adds diagonal neighbors if within bounds and diagonal is True
            if i > 0 and j > 0 and diagonal:
                cell_list[i][j].add_neighbor(cell_list[i - 1][j - 1], specifier)
            if i > 0:
                cell_list[i][j].add_neighbor(cell_list[i - 1][j], specifier)
            if i > 0 and j < len(cell_list) - 1 and diagonal:
                cell_list[i][j].add_neighbor(cell_list[i - 1][j + 1], specifier)
            if j > 0:
                cell_list[i][j].add_neighbor(cell_list[i][j - 1], specifier)
            if j < len(cell_list) - 1:
                cell_list[i][j].add_neighbor(cell_list[i][j + 1], specifier)
            if i < len(cell_list) - 1 and j > 0 and diagonal:
                cell_list[i][j].add_neighbor(cell_list[i + 1][j - 1], specifier)
            if i < len(cell_list) - 1:
                cell_list[i][j].add_neighbor(cell_list[i + 1][j], specifier)
            if i < len(cell_list) - 1 and j < len(cell_list) - 1 and diagonal:
                cell_list[i][j].add_neighbor(cell_list[i + 1][j + 1], specifier)

# Returns the count of cells with states 2(Transmitter), 3(Resting neuron), or 4(Firing neuron) in the specified quarter of the grid
def first_quarter(matrix):
    rows, cols = len(matrix), len(matrix[0])
    mid_row, mid_col = math.ceil(rows / 2), math.ceil(cols / 2)

    first_quarter_value = 0
    for i in range(mid_row - 1):
        for j in range(mid_col - 1):
            if matrix[i][j].state in {2, 3, 4}:
                first_quarter_value += 1

    return first_quarter_value
def second_quarter(matrix):
    rows, cols = len(matrix), len(matrix[0])
    mid_row, mid_col = math.ceil(rows / 2), math.ceil(cols / 2)

    second_quarter_value = 0
    for i in range(mid_row - 1):
        for j in range(mid_col, cols):
            if matrix[i][j].state in {2, 3, 4}:
                second_quarter_value += 1

    return second_quarter_value
def third_quarter(matrix):
    rows, cols = len(matrix), len(matrix[0])
    mid_row, mid_col = math.ceil(rows / 2), math.ceil(cols / 2)

    third_quarter_value = 0
    for i in range(mid_row, rows):
        for j in range(mid_col - 1):
            if matrix[i][j].state in {2, 3, 4}:
                third_quarter_value += 1

    return third_quarter_value
def fourth_quarter(matrix):
    rows, cols = len(matrix), len(matrix[0])
    mid_row, mid_col = math.ceil(rows / 2), math.ceil(cols / 2)

    fourth_quarter_value = 0
    for i in range(mid_row, rows):
        for j in range(mid_col, cols):
            if matrix[i][j].state in {2, 3, 4}:
                fourth_quarter_value += 1

    return fourth_quarter_value
