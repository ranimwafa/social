import networkx as nx
import pandas as pd
import random
import copy

# Load Graph
edges = []
with open("data/facebook_combined.txt", "r") as f:
    for line in f:
        u, v = line.strip().split()
        edges.append((int(u), int(v)))

G = nx.Graph()
G.add_edges_from(edges)

# Load bot labels
labels = pd.read_csv("bot_labels.csv")
bot_nodes = labels[labels['label'] == 1]['node'].tolist()

# -----------------------------
# 1) Structural Evasion Attack
# -----------------------------
G_evasion = copy.deepcopy(G)

for bot in bot_nodes[:50]:   # apply attack on 50 bots
    neighbors = list(G_evasion.neighbors(bot))
    if len(neighbors) > 3:
        remove_edges = random.sample(neighbors, 3)
        for n in remove_edges:
            G_evasion.remove_edge(bot, n)

nx.write_edgelist(G_evasion, "graph_after_evasion.edgelist")
print("Structural evasion attack completed.")

# -----------------------------
# 2) Graph Poisoning Attack
# -----------------------------
G_poison = copy.deepcopy(G)

normal_nodes = labels[labels['label'] == 0]['node'].tolist()

for bot in bot_nodes[:50]:
    new_neighbors = random.sample(normal_nodes, 4)
    for n in new_neighbors:
        G_poison.add_edge(bot, n)

nx.write_edgelist(G_poison, "graph_after_poisoning.edgelist")
print("Graph poisoning attack completed.")
