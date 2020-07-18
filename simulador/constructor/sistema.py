import networkx as nx
import simpy

class Sistema(object):
    """docstring for ."""

    def __init__(self):
        self.environment = simpy.Environment()
        self.network = nx.Graph()
        self.processes = None

    def build_network(connections):
        pass

    def link_processes(self, p1, p2):
        self.network.add_edge(p1,p2)

    def set_processes(self, processes):
        self.processes = processes
        self.network.add_nodes_from(self.processes)

    def get_processes(self):
        return self.network.nodes()

    def get_neighbors(self, process):
        return self.network.neighbors(process)

    def simulate(time):
        for process in self.processes:
            env.process(process)
        self.environment.run(until=time)
