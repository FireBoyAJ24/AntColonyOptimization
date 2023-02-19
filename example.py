import numpy as np
import sys
import matplotlib.pyplot as plt
import networkx as nx
import random
from ant_colony import AntColony
G = nx.Graph()

seed = 0
random.seed(seed)
np.random.seed(seed)

distances = np.array([[np.inf, 2, 2, 5, 7],
                      [2, np.inf, 4, 8, 2],
                      [2, 4, np.inf, 1, 3],
                      [5, 8, 1, np.inf, 2],
                      [7, 2, 3, 2, np.inf]])

ant_colony = AntColony(distances, 1, 1, 100, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.run()
print ("shorted_path: {}".format(shortest_path))
print(distances.shape)

num_rows, num_cols =  distances.shape

for i in range(1, num_cols + 1, 1):
    G.add_node(i)

for a in range(1, num_cols + 1, 1):
    for b in range(1, num_rows + 1, 1):
        if a != b:
            ds = distances[a - 1][b - 1]
            print(ds)
            G.add_edge(a, b, weight=ds)

pos = {
    1:(1,5),
    2:(4.5,6.6),
    3:(3.6, 1.4),
    4:(5.8, 2.5),
    5:(7.9, 3.6)
}

for u,v, d in G.edges(data=True):
    print(u,v)
    print(d)
    print("=============")
edge_labels={(u,v):d["weight"] for u,v,d in G.edges(data=True)}

nx.draw(G, with_labels=True, node_color="blue", node_size=2000, font_color="white", font_family="arial", font_weight="bold")
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.5)
plt.margins(0.2)
plt.show()