import matplotlib.pyplot as plt
import networkx as nx

import simpy

from constructor import sistema
from procesos import proceso


SIM_TIME = 20

if __name__ == "__main__":

    sys = sistema.Sistema()

    p1 = proceso.Proceso(sys.environment, "p1", None)
    p2 = proceso.Proceso(sys.environment, "p2", None)

    processes = [p1,p2]
    sys.set_processes(processes)


    sys.link_processes(p1,p2)

    for process in sys.get_processes():
        process.set_neighbors(sys.get_neighbors(process))


    #plt.subplot(121)
    nx.draw(sys.network, with_labels=True, font_weight='light')
    plt.show()


    env = simpy.Environment()
