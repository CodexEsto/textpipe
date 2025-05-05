"""Text classification pipeline for category prediction using similar components as sentiment analysis."""

from textpipe.data import clean_text, tokenize
from textpipe.data.vectorizer import Vectorizer
from textpipe.core.classifier import TextClassifier
from textpipe.data.model_io import (
    save_model,
    load_model,
    save_vectorizer,
    load_vectorizer,
)


class CategoryPipeline:
    """
    A pipeline for text classification into categories or topics.

    This pipeline processes input texts and trains a classifier to categorize them
    into predefined labels such as "Technology", "Business", "Education", etc.

    Attributes:
        config (object): Configuration object with processing options.
        vectorizer (Vectorizer): Text vectorizer.
        classifier (TextClassifier): Text classifier.
    """

    def __init__(self, config):
        """
        Initialize the category classification pipeline.

        Args:
            config (object): Configuration containing language and processing settings.
        """
        self.config = config
        max_features = config.processing.get("max_features", 5000)
        self.vectorizer = Vectorizer(max_features=max_features)
        self.classifier = TextClassifier()

    def preprocess(self, texts):
        """
        Preprocess a list of raw texts by cleaning, tokenizing, and vectorizing.

        Args:
            texts (list of str): Input raw texts.

        Returns:
            ndarray: Vectorized representation of the texts.
        """
        cleaned = [clean_text(t, self.config) for t in texts]
        tokenized = [" ".join(tokenize(t, self.config)) for t in cleaned]
        return self.vectorizer.fit_transform(tokenized)

    def train(self, texts, labels):
        """
        Train the classifier to categorize texts.

        Args:
            texts (list of str): Training examples.
            labels (list of str): Corresponding category labels.
        """
        X = self.preprocess(texts)
        self.classifier.train(X, labels)

    def predict(self, texts):
        """
        Predict categories for new input texts.

        Args:
            texts (list of str): Raw texts to classify.

        Returns:
            list: Predicted category labels.
        """
        cleaned = [clean_text(t, self.config) for t in texts]
        tokenized = [" ".join(tokenize(t, self.config)) for t in cleaned]
        X = self.vectorizer.transform(tokenized)
        return self.classifier.predict(X)

    def save(self, model_path, vectorizer_path):
        """Save both the recommender model and vectorizer."""
        save_model(self.recommender, model_path)
        save_vectorizer(self.vectorizer, vectorizer_path)

    def load(self, model_path, vectorizer_path):
        """Load both the recommender model and vectorizer."""
        self.recommender = load_model(model_path)
        self.vectorizer = load_vectorizer(vectorizer_path)
