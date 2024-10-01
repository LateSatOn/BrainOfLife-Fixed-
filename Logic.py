def cell_logic(cell_list, i, j):
    cell = cell_list[i][j]
    enabled_transistors = cell_list[i][j].find_enabled_transistors()
    enabled_resting_neurons = cell_list[i][j].find_enabled_resting_neurons()

    if cell.get_state() == 1 and cell.get_enabled() == 0:
        for n in range(len(enabled_transistors)):
            enabled_transistors[n].change_signal_by(1)
            enabled_transistors[n].change_enabled_by(1)

        cell.set_enabled(5)

    elif cell.get_state() == 2 and cell.get_enabled() == 0 and cell.get_signal() > 0:
        for n in range(len(enabled_transistors)):
            print(f"{n}")
            enabled_transistors[n].change_signal_by(1)
            enabled_transistors[n].change_enabled_by(1)
        for n in range(len(enabled_resting_neurons)):
            print(f"{n}")
            enabled_resting_neurons[n].change_signal_by(1)
            enabled_resting_neurons[n].change_enabled_by(1)

        cell.set_signal(0)
        cell.set_enabled(2)

    elif cell.get_state() == 3 and cell.get_enabled() == 0 and cell.get_signal() > 0:
        cell.set_state(4)

        cell.set_enabled(1)

    elif cell.get_state() == 4 and cell.get_enabled() == 0:
        for n in range(len(enabled_transistors)):
            enabled_transistors[n].change_signal_by(1)
            enabled_transistors[n].change_enabled_by(1)
        cell.set_state(3)

        cell.set_signal(0)
        cell.set_enabled(2)
