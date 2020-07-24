import simpy

class proceso:
    """docstring for ."""

    def __init__(self, environment, name, blackbox):
        self.environment = environment
        self.name = name
        self.neighbors = None
        self.blackbox = blackbox
        self.messages = []

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def send_message(self, process):
        process.messages = self.messages
        print(self.messages)

    def run(self):
        while True:
            blackbox(self)

    def __str__(self):
        return self.name
