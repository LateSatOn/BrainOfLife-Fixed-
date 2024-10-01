class Cell:
    def __init__(self, state, signal, disabled):
        # Initialize cell with state, signal, and disabled status
        self.state = state
        self.neighbors_t = []  # List of transistor neighbors
        self.neighbors_n = []  # List of neuron neighbors
        self.signal = signal  # Signal value of the cell
        self.disabled = disabled  # Disabled status (affects behavior)

    # Getters for the cell's attributes
    def get_state(self):
        return self.state
    def get_signal(self):
        return self.signal
    def get_disabled(self):
        return self.disabled

    # Setters to update the cell's state, signal, and disabled status
    def set_state(self, data):
        self.state = data
    def set_signal(self, state):
        self.signal = state
    def set_disabled(self, state):
        self.disabled = state

    # Methods to change the cell's attributes by a given value
    def change_state_by(self, data):
        self.state += data
    def change_signal_by(self, data):
        self.signal += data
    def change_disabled_by(self, data):
        self.disabled += data

    # Add a neighbor to the cell's list of neighbors based on the specifier ('n' for neuron, 't' for transistor)
    def add_neighbor(self, neighbor, specifier):
        if specifier.lower() == "n":
            self.neighbors_n.append(neighbor)
        elif specifier.lower() == 't':
            self.neighbors_t.append(neighbor)

    # Find enabled neighbors based on specifier ('n' for neurons, 't' for transistors)
    def find_enabled(self, specifier):
        enabled_neighbors = []
        if specifier.lower() == "n":
            for n in range(len(self.neighbors_n)):
                # Neurons must be in state 3 and enabled
                if self.neighbors_n[n].state == 3 and self.neighbors_n[n].disabled == 0:
                    enabled_neighbors.append(self.neighbors_n[n])
        elif specifier.lower() == 't':
            for n in range(len(self.neighbors_t)):
                # Transistors must be in state 2 and enabled
                if self.neighbors_t[n].state == 2 and self.neighbors_t[n].disabled == 0:
                    enabled_neighbors.append(self.neighbors_t[n])
        return enabled_neighbors
