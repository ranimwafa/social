import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
import joblib

# Load features and labels
features = pd.read_csv("graph_metrics.csv")
labels = pd.read_csv("bot_labels.csv")

df = features.merge(labels, on='node')

X = df.drop(columns=['node','label'])
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
y_prob = clf.predict_proba(X_test)[:,1]

print(classification_report(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, y_prob))

# Save model
joblib.dump(clf, "baseline_model.joblib")
print("Baseline model saved to baseline_model.joblib")
