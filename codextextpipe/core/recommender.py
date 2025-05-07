import numpy as np
from codextextpipe.data.vectorizer import Vectorizer
from codextextpipe.data.cleaner import clean_text

class ContentRecommender:
    def __init__(self, max_features=5000, n_components = 25,ngram_range=(1, 2)):
        """
        Initialize the recommender with vectorization parameters.

        :param max_features: Maximum number of features for TF-IDF vectorizer
        :param ngram_range: Range of n-grams for TF-IDF vectorizer (e.g., (1, 2) for unigrams and bigrams)
        """
        self.vectorizer = Vectorizer(max_features=max_features, n_components=n_components, ngram_range=ngram_range)
        self.embeddings = None

    def fit(self, texts: list):
        """
        Fit the recommender model on the provided texts.

        :param texts: List of input texts to train the recommender
        """
        # Clean the input texts
        cleaned = [clean_text(text) for text in texts]
        
        # Vectorize the cleaned texts and reduce dimensions
        self.embeddings = self.vectorizer.fit_transform(cleaned)

    def recommend(self, query_text: str, k=3) -> list:
        """
        Get recommendations for a query text.

        :param query_text: Input text to find similar items for
        :param k: Number of recommendations to return
        :return: List of indices of similar items
        """
        # Clean the query text
        cleaned_query = clean_text(query_text)
        
        # Transform the query text into vector space
        query_vector = self.vectorizer.transform([cleaned_query])

        # Calculate cosine similarity between the query and stored embeddings
        similarities = np.dot(self.embeddings, query_vector.T).flatten()

        # Return the indices of the top 'k' most similar items
        return np.argsort(similarities)[-k:][::-1].tolist()
