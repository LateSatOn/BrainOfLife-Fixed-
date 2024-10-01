class Cell:
    def __init__(self,identity, state, signal, enabled):
        self.identity = identity
        self.state = state
        self.neighbors_t = []
        self.neighbors_n = []
        self.signal = signal
        self.enabled = enabled

    def get_identity(self):
        return self.identity
    def get_state(self):
        return self.state
    def get_neighbors(self, specifier):
        if specifier == 'n':
            return self.neighbors_n
        elif specifier == 't':
            return self.neighbors_t

    def get_signal(self):
        return self.signal
    def get_enabled(self):
        return self.enabled

    def set_identity(self, identity):
        self.identity = identity
    def set_state(self, data):
        self.state = data
    def set_signal(self, state):
        self.signal = state
    def set_enabled(self, state):
        self.enabled = state

    def add_neighbor(self, neighbor, specifier):
        if specifier == 'n':
            self.neighbors_n.append(neighbor)
        elif specifier == 't':
            self.neighbors_t.append(neighbor)


    def change_state_by(self, data):
        self.state += data
    def change_signal_by(self, data):
        self.signal += data
    def change_enabled_by(self, data):
        self.enabled += data

    def find_enabled_transistors(self):
        enabled_transistor_neighbors = []
        for n in range(len(self.neighbors_t)):
            if self.neighbors_t[n].state == 2 and self.neighbors_t[n].enabled == 0:
                enabled_transistor_neighbors.append(self.neighbors_t[n])
        return enabled_transistor_neighbors

    def find_enabled_resting_neurons(self):
        enabled_resting_neuron_neighbors = []
        for n in range(len(self.neighbors_n)):
            if self.neighbors_n[n].state == 3 and self.neighbors_n[n].enabled == 0:
                enabled_resting_neuron_neighbors.append(self.neighbors_n[n])
        return enabled_resting_neuron_neighbors
