def cell_logic(cell_array, i, j):
    if cell_array[i][j].get_state() == 1:
        print(f"{cell_array[i][j].get_identity()}: {cell_array[i][j].get_state()}")
    elif cell_array[i][j].get_state() == 2:
        print(f"{cell_array[i][j].get_identity()}: {cell_array[i][j].get_state()}")
    elif cell_array[i][j].get_state() == 3:
        print(f"{cell_array[i][j].get_identity()}: {cell_array[i][j].get_state()}")
    elif cell_array[i][j].get_state() == 4:
        print(f"{cell_array[i][j].get_identity()}: {cell_array[i][j].get_state()}")