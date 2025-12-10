import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from networkx.algorithms import community

# Load graph
edges = []
with open("data/facebook_combined.txt", "r") as f:
    for line in f:
        u, v = line.strip().split()
        edges.append((int(u), int(v)))

G = nx.Graph()
G.add_edges_from(edges)

# -----------------------------
# 1) Degree
# -----------------------------
degree_dict = dict(G.degree())
print("Top 10 nodes by Degree:")
top_degree = sorted(degree_dict.items(), key=lambda x: x[1], reverse=True)[:10]
print(top_degree)

# -----------------------------
# 2) Clustering Coefficient
# -----------------------------
clustering = nx.clustering(G)
avg_clustering = sum(clustering.values()) / len(clustering)
print("Average Clustering Coefficient:", avg_clustering)

# -----------------------------
# 3) Centrality Measures
# -----------------------------
print("Computing centralities...")

degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

print("Top Degree Centrality:", sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5])
print("Top Betweenness Centrality:", sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:5])
print("Top Closeness Centrality:", sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)[:5])

# -----------------------------
# 4) Community Detection
# -----------------------------
print("Detecting communities...")
communities = community.greedy_modularity_communities(G)
print("Number of detected communities:", len(communities))

# -----------------------------
# Save metrics to CSV (for report)
# -----------------------------
df = pd.DataFrame({
    "node": list(degree_dict.keys()),
    "degree": list(degree_dict.values()),
    "clustering": [clustering[n] for n in degree_dict.keys()],
    "degree_centrality": [degree_centrality[n] for n in degree_dict.keys()],
    "betweenness": [betweenness_centrality[n] for n in degree_dict.keys()],
    "closeness": [closeness_centrality[n] for n in degree_dict.keys()]
})

df.to_csv("graph_metrics.csv", index=False)
print("Metrics saved to graph_metrics.csv")
