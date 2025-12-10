import networkx as nx
import pandas as pd

def compute_metrics(graph_file, output_file):
    G = nx.read_edgelist(graph_file, nodetype=int)

    degree_dict = dict(G.degree())
    clustering = nx.clustering(G)
    degree_centrality = nx.degree_centrality(G)
    betweenness = nx.betweenness_centrality(G)
    closeness = nx.closeness_centrality(G)

    df = pd.DataFrame({
        "node": list(degree_dict.keys()),
        "degree": list(degree_dict.values()),
        "clustering": [clustering.get(n,0) for n in degree_dict.keys()],
        "degree_centrality": [degree_centrality.get(n,0) for n in degree_dict.keys()],
        "betweenness": [betweenness.get(n,0) for n in degree_dict.keys()],
        "closeness": [closeness.get(n,0) for n in degree_dict.keys()]
    })

    df.to_csv(output_file, index=False)

# After attacks
compute_metrics("graph_after_evasion.edgelist", "metrics_after_evasion.csv")
compute_metrics("graph_after_poisoning.edgelist", "metrics_after_poisoning.csv")

print("Metrics recomputed after attacks.")
