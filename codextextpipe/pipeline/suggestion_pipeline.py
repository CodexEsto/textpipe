"""Pipeline for generating content-based text recommendations."""

from codextextpipe.data import clean_text
from codextextpipe.core.recommender import ContentRecommender
from codextextpipe.data.model_io import (
    save_model,
    load_model,
    save_vectorizer,
    load_vectorizer,
)


class SuggestionPipeline:
    """
    A pipeline to generate recommendations for similar texts using content-based filtering.

    This class wraps the ContentRecommender and handles text preprocessing and similarity-based suggestion.

    Attributes:
        config (object): Configuration object for text processing.
        recommender (ContentRecommender): Underlying content-based recommendation engine.
    """

    def __init__(self, config):
        """
        Initialize the suggestion pipeline.

        Args:
            config (object): Configuration containing text preprocessing options.
        """
        self.config = config
        self.recommender = ContentRecommender(
            n_components=config.processing.get("n_components", 50)
        )
        self.texts = []  # Keep original texts for returning recommendations

    def preprocess(self, texts):
        """
        Preprocess a list of raw texts using the configuration.

        Args:
            texts (list of str): Raw text data.

        Returns:
            list of str: Cleaned text data.
        """
        return [clean_text(t) for t in texts]

    def fit(self, texts):
        """
        Fit the recommender to a list of texts.

        Args:
            texts (list of str): The corpus used for recommendation.
        """
        cleaned = self.preprocess(texts)
        self.recommender.fit(cleaned)
        self.texts = texts  # Save original texts for lookup

    def suggest(self, query_text, k=3):
        """
        Suggest k similar texts from the dataset.

        Args:
            query_text (str): The input query to find similar entries for.
            k (int): Number of suggestions to return.

        Returns:
            list of str: Top-k recommended texts from the dataset.
        """
        indices = self.recommender.recommend(query_text, k)
        return [self.texts[i] for i in indices]

    def save(self, model_path, vectorizer_path):
        """Save both the recommender model and vectorizer."""
        save_model(self.recommender, model_path)
        save_vectorizer(self.vectorizer, vectorizer_path)

    def load(self, model_path, vectorizer_path):
        """Load both the recommender model and vectorizer."""
        self.recommender = load_model(model_path)
        self.vectorizer = load_vectorizer(vectorizer_path)
