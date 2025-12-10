import networkx as nx
import matplotlib.pyplot as plt

# Load data
edges = []
with open("data/facebook_combined.txt", "r") as f:
    for line in f:
        u, v = line.strip().split()
        edges.append((int(u), int(v)))

# Build graph
G = nx.Graph()
G.add_edges_from(edges)

print("Number of Nodes:", G.number_of_nodes())
print("Number of Edges:", G.number_of_edges())

# Draw sample from graph (small part)
sample_nodes = list(G.nodes())[:200]
H = G.subgraph(sample_nodes)

plt.figure(figsize=(8, 8))
nx.draw(H, node_size=20)
plt.title("Sample Facebook Graph")
plt.show()
