import networkx as nx
import simpy
from algorithms import *
import algorithms as al
import proceso

class simulador:

    def __init__(self):
        self.environment = simpy.Environment()
        self.network = nx.Graph()
        self.processes = None
        self.black_box = None

    def build_network(self, nodes = 1, edges = -1, type = None):
        """Builds a graph of Processes.

        Keyword arguments:
        nodes -- the number of nodes in the graph (defaults to 1)
        edges -- the number of edges in the graph (defaults to 1)
        type -- the type of graph to generate (defaults to None)

        If no graph type is specified, either a random graph or a complete graph
        is generated depending on the number of edges specified.
        """
        if type == None:
            if edges == -1:
                self.network = nx.complete_graph(nodes)
            else:
                self.network = nx.gnm_random_graph(nodes, edges)
        else:
            self.network = self.graph_types(nodes, edges, type)
        nx.set_node_attributes(self.network, None, 'process')

    def graph_types(self, nodes, edges, type):
        switcher = {
            "cycle": nx.cycle_graph(nodes),
            "path": nx.path_graph(nodes),
            "star": nx.star_graph(nodes),
            "random": nx.gnm_random_graph(nodes, edges),
            "tree": nx.random_tree(nodes)
        }
        return switcher.get(type, nx.gnm_random_graph(nodes, edges))

    def instance_network(self, process_names):
        nx.set_node_attributes(self.network, None, "process")
        for i in range(self.network.number_of_nodes()):
            self.network.nodes[i]['process'] = proceso.proceso(self.environment, process_names[i], self.black_box)
        self.processes = list(self.network.nodes.data('process'))

    def get_algorithm(self, algorithm):
        switcher = {
            "propagation": propagation()
        }
        return switcher.get(type, default())

    def add_process(self, name):
        self.network.add_node(proceso(self.environment, name, self.black_box))

    def link_processes(self, p1, p2):
        self.network.add_edge(p1,p2)
        p1.neighbors.add(p2)
        p2.neighbors.add(p1)

    def get_processes(self):
        return self.network.nodes()

    def simulate(self, time, algorithm, process_names = None, nodes = 1, edges = -1, type = None):
        self.build_network(nodes, edges, type)
        self.black_box = self.get_algorithm(algorithm)
        self.instance_network(range(self.network.number_of_nodes()))
        for process in self.processes:
            process[1].neighbors = self.network.neighbors(process[0])
            process[1].black_box = self.black_box
            process[1].message = "Holi"
            # env.process(process)
        # self.environment.run(until=time)
