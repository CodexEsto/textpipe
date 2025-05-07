"""Advanced text vectorization with TF-IDF and dimension reduction."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD


class Vectorizer:
    def __init__(self, max_features=1000, n_components = 25, ngram_range=(1, 2)):
        # Validate max_features
        if (
            not (isinstance(max_features, int) and max_features > 0)
            and max_features is not None
        ):
            raise ValueError(
                f"'max_features' must be a positive integer or None. Got {type(max_features).__name__}: {max_features}"
            )

        self.vectorizer = TfidfVectorizer(
            max_features=max_features, ngram_range=ngram_range, stop_words=None
        )
        self.reducer = TruncatedSVD(n_components=n_components)

    def fit_transform(self, texts):
        if not all(isinstance(text, str) for text in texts):
            raise ValueError("All elements in 'texts' must be strings.")
        tfidf = self.vectorizer.fit_transform(texts)
        return self.reducer.fit_transform(tfidf)

    def transform(self, texts):
        tfidf = self.vectorizer.transform(texts)
        return self.reducer.transform(tfidf)
