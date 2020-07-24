import simpy

class Proceso(object):
    """docstring for ."""

    def __init__(self, sys, name, blackbox):
        self.sys = sys
        self.env = sys.env
        self.name = name
        self.neighbors = None
        self.blackbox = blackbox
        self.action = self.env.process(self.blackbox(self))

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def send_all(self, message):
        for process in self.neighbors:
            self.sys.deliver(message, process)

    def wait(self):
        yield self.env.timeout(simpy.core.Infinity)

    def wait_message(self):
        try:
            yield self.env.process(self.wait())
        except simpy.Interrupt as msg:
            return msg

    def __str__(self):
        return self.name
