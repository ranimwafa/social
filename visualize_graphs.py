import matplotlib
matplotlib.use("Agg")  # مهم جدًا عشان matplotlib يحفظ الصور بدل ما يحاول يفتح نافذة

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# ---- Load original graph ----
G = nx.read_edgelist("data/facebook_combined.txt")

# ---- Load bot labels if موجودة ----
try:
    bot_labels = pd.read_csv("bot_labels.csv")
    bot_nodes = set(bot_labels[bot_labels['label']==1]['node'])
except:
    bot_nodes = set()
    print("No bot_labels.csv found. Proceeding without bot info.")

# ---- Visualization function ----
def visualize_graph(G, bot_nodes=set(), filename="graph.png", title="Graph"):
    plt.figure(figsize=(8, 8))
    pos = nx.spring_layout(G, seed=42)  # layout ثابت عشان الرسم يتكرر نفس الشكل
    node_colors = ["red" if n in bot_nodes else "skyblue" for n in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=50)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Graph saved as {filename}")

# ---- Visualize original graph ----
visualize_graph(G, bot_nodes, filename="graph_original.png", title="Original Graph")

# ---- If recomputed metrics after attacks exist, load and visualize ----
try:
    G_structural = nx.read_edgelist("graph_structural_evasion.txt")
    visualize_graph(G_structural, bot_nodes, filename="graph_structural.png", title="After Structural Evasion")
except:
    print("No structural evasion graph found.")

try:
    G_poison = nx.read_edgelist("graph_poisoning.txt")
    visualize_graph(G_poison, bot_nodes, filename="graph_poison.png", title="After Graph Poisoning")
except:
    print("No graph poisoning file found.")
