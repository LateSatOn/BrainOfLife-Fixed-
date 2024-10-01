# Defines the behavior of a cell based on its state and signals
def cell_logic(cell_list, i, j):
    cell = cell_list[i][j] # Retrieve the current cell
    enabled_transistors = cell.find_enabled('t') # Get enabled transistors for the current cell
    enabled_resting_neurons = cell.find_enabled('n') # Get enabled resting neurons for the current cell

    # If the cell is in state 1 and not enabled, propagate signals to transistors
    if cell.get_state() == 1 and cell.get_disabled() == 0:
        for n in range(len(enabled_transistors)):
            enabled_transistors[n].change_signal_by(1) # Increase transistor signal
            enabled_transistors[n].change_disabled_by(1) # Disable transistor for current iteration

        cell.set_disabled(5) # Disable the current cell for 4 iterations

    # If the cell is in state 2, has no enabled status, and has signal > 0
    elif cell.get_state() == 2 and cell.get_disabled() == 0 and cell.get_signal() > 0:
        for n in range(len(enabled_transistors)):
            enabled_transistors[n].change_signal_by(1) # Increase transistor signal
            enabled_transistors[n].change_disabled_by(1) # Disable transistor for current iteration
        for n in range(len(enabled_resting_neurons)):
            enabled_resting_neurons[n].change_signal_by(1) # Increase neuron signal
            enabled_resting_neurons[n].change_disabled_by(1) # Disable neuron for current iteration

        cell.set_signal(0) # Reset cell signal
        cell.set_disabled(2) # Disable the current cell for 1 iteration

    # If the cell is in state 3, has no enabled status, and has signal > 0
    elif cell.get_state() == 3 and cell.get_disabled() == 0 and cell.get_signal() > 0:
        cell.set_state(4)  # Change cell state to 4 (special action)
        cell.set_disabled(1)  # Disable cell for current iteration

    # If the cell is in state 4 and not enabled, reset signal and go back to state 3
    elif cell.get_state() == 4 and cell.get_disabled() == 0:
        for n in range(len(enabled_transistors)):
            enabled_transistors[n].change_signal_by(1) # Increase transistor signal
            enabled_transistors[n].change_disabled_by(1) # Disable transistor for current iteration

        cell.set_state(3)  # Return the cell to state 3
        cell.set_signal(0)  # Reset cell signal
        cell.set_disabled(2)  # Disable the current cell for 1 iteration
