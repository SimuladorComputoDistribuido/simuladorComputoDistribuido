import simpy

class Process(object):
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

    def wait_to_infinity(self):
        yield self.env.timeout(simpy.core.Infinity)

    def wait_time(self, time):
        yield self.env.timeout(time)

    def wait(self, time=None):
        if time is None:
            return self.env.process(self.wait_to_infinity())
        else:
            return self.env.process(self.wait_time(time))

    def show(self, message):
        print('Process %s | %s | at t=%d' % (self.name, message, self.env.now))

    def __str__(self):
        return self.name
