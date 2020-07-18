import simpy

class Proceso(object):
    """docstring for ."""

    def __init__(self, environment, name, blackbox):
        self.environment = environment
        self.name = name
        self.neighbors = None
        self.blackbox = blackbox

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def send_message(self, process):
        pass

    def run(self):
        while True:
            blackbox(self)

    def __str__(self):
        return self.name
