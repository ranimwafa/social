import pandas as pd
import joblib
from sklearn.metrics import classification_report, roc_auc_score

model = joblib.load("baseline_model.joblib")
labels = pd.read_csv("bot_labels.csv")

def evaluate(metrics_file, title):
    features = pd.read_csv(metrics_file)
    df = features.merge(labels, on='node', how='inner')

    X = df.drop(columns=['node','label'])
    y = df['label']

    y_pred = model.predict(X)
    y_prob = model.predict_proba(X)[:,1]

    print("\n======", title, "======")
    print(classification_report(y, y_pred))
    print("ROC AUC:", roc_auc_score(y, y_prob))

evaluate("graph_metrics.csv", "Baseline (No Attack)")
evaluate("metrics_after_evasion.csv", "After Structural Evasion")
evaluate("metrics_after_poisoning.csv", "After Graph Poisoning")
