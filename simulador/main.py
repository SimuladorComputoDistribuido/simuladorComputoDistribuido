import matplotlib.pyplot as plt
import networkx as nx

import simpy

from constructor import sistema
from procesos import proceso
from algorithms import algorithm


SIM_TIME = 15

if __name__ == "__main__":

    sys = sistema.Sistema()
    p1 = proceso.Proceso(sys, "p1", algorithm.ping)
    p2 = proceso.Proceso(sys, "p2", algorithm.pong)

    processes = [p1,p2]
    sys.set_processes(processes)
    sys.link_processes(p1,p2)
    sys.set_network()

    sys.simulate(10)
