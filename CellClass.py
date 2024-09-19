class Cell:
    def __init__(self,identity, state, signal, enabled):
        self.identity = identity
        self.state = state
        self.neighbors = []
        self.signal = signal
        self.enabled = enabled

    def get_identity(self):
        return self.identity
    def get_state(self):
        return self.state
    def get_neighbors(self):
        return self.neighbors
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

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def change_state_by(self, data):
        self.state += data
    def change_signal_by(self, data):
        self.signal += data
    def change_enabled_by(self, data):
        self.enabled += data

    def find_enabled_transmitters(self):
        transmitter_array = []
        for n in range(len(self.neighbors)):
            if self.neighbors[n].state == 2 and self.neighbors[n].enabled == 0:
                transmitter_array.append(self.neighbors[n])
        return transmitter_array
    def find_enabled_resting_neurons(self):
        neuron_array = []
        for n in range(len(self.neighbors)):
            if self.neighbors[n].state == 3 and self.neighbors[n].enabled == 0:
                neuron_array.append(self.neighbors[n])
        return neuron_array