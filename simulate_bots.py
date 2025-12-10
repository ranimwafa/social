import pandas as pd
import random

# Load nodes from graph_metrics.csv
df = pd.read_csv("graph_metrics.csv")
nodes = df['node'].tolist()

# Simulate bots (10% randomly)
num_bots = int(0.1 * len(nodes))
bot_nodes = random.sample(nodes, num_bots)

labels = []
for n in nodes:
    if n in bot_nodes:
        labels.append(1)  # bot
    else:
        labels.append(0)  # normal

df_labels = pd.DataFrame({'node': nodes, 'label': labels})
df_labels.to_csv("bot_labels.csv", index=False)
print("Simulated bot labels saved to bot_labels.csv")
