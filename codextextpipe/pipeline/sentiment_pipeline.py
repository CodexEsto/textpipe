"""Sentiment analysis pipeline using text cleaning, tokenization, vectorization, and classification."""

from codextextpipe.data import clean_text, tokenize
from codextextpipe.data.vectorizer import Vectorizer
from codextextpipe.core.classifier import TextClassifier
from codextextpipe.data.model_io import (
    save_model,
    load_model,
    save_vectorizer,
    load_vectorizer,
)


class SentimentPipeline:
    """
    A pipeline for end-to-end sentiment analysis.

    This class performs preprocessing (cleaning, tokenizing, vectorizing) and trains a classifier
    to predict sentiment (e.g., positive, negative, neutral) for given text inputs.

    Attributes:
        config (object): Configuration object with language and processing options.
        vectorizer (Vectorizer): Converts text into numerical features.
        classifier (TextClassifier): Trained model to predict sentiment.
    """

    def __init__(self, config):
        """
        Initialize the pipeline with configuration and components.

        Args:
            config (object): A configuration object containing processing options.
        """
        self.config = config
        max_features = config.processing.get("max_features", 5000)
        self.vectorizer = Vectorizer(max_features=max_features)
        self.classifier = TextClassifier()

    def preprocess(self, texts):
        """
        Preprocess a list of raw texts by cleaning, tokenizing, and vectorizing.

        Args:
            texts (list of str): Raw text inputs.

        Returns:
            ndarray: Vectorized form of input texts.
        """
        cleaned = [clean_text(t, self.config) for t in texts]
        tokenized = [" ".join(tokenize(t, self.config)) for t in cleaned]
        return self.vectorizer.fit_transform(tokenized)

    def train(self, texts, labels):
        """
        Train the sentiment classifier.

        Args:
            texts (list of str): Training text samples.
            labels (list of str or int): Corresponding sentiment labels.
        """
        X = self.preprocess(texts)
        self.classifier.train(X, labels)

    def predict(self, texts):
        """
        Predict sentiment for a list of new texts.

        Args:
            texts (list of str): Raw text inputs to classify.

        Returns:
            list: Predicted sentiment labels.
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
