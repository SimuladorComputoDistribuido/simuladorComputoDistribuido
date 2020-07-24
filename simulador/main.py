import matplotlib.pyplot as plt
import networkx as nx

import simpy

from constructor import system
from procesos import process
from algorithms import algorithm


SIM_TIME = 15

if __name__ == "__main__":

    sys = system.System()
    p1 = process.Process(sys, "p1", algorithm.simple_flood_leader)
    p2 = process.Process(sys, "p2", algorithm.simple_flood)
    p3 = process.Process(sys, "p3", algorithm.simple_flood)
    p4 = process.Process(sys, "p4", algorithm.simple_flood)

    processes = [p1,p2,p3,p4]
    sys.set_processes(processes)
    sys.link_processes(p1,p2)
    sys.link_processes(p2,p3)
    sys.link_processes(p3,p4)
    sys.set_network()

    sys.simulate(10)
