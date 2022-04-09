from params import NetworkParameters
import networkx as nx
import matplotlib.pyplot as plt
from constants import NodeColors


class Network:
    def __init__(self):
        self.N = NetworkParameters.dimension_N
        self.M = NetworkParameters.dimension_M

    def generate_network(self):
        return nx.grid_2d_graph(self.N, self.M)

    @staticmethod
    def plot_network(self, graph):
        pos = {(x, y): (y, -x) for x, y in graph.nodes()}
        labels = dict(((i, j), f"{i},{j}") for i, j in graph.nodes())
        plt.close()
        nx.draw_networkx(
            graph,
            pos=pos,
            labels=labels,
            node_size=400,
            node_color=NodeColors.GREEN
        )
        plt.axis("off")
        plt.show()
