"""Text classifier with multiple algorithm support."""

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


class TextClassifier:
    def __init__(self, model_type="logreg"):
        self.models = {
            "logreg": LogisticRegression(max_iter=1000),
            "svm": SVC(probability=True),
            "randomforest": RandomForestClassifier(),
        }
        self.model = self.models[model_type]

    def train(self, X, y):
        self.model.fit(X, y)

    def predict_proba(self, X):
        return self.model.predict_proba(X)

    def predict(self, X):
        """Predict class labels for the input data."""
        return self.model.predict(X)
