from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import numpy as np

def vectorize_tfidf(texts, max_features=1000):
    """
    Convert a list of texts into TF-IDF vectors.

    :param texts: list, list of strings (texts)
    :param max_features: int, max number of features to keep (default: 1000)
    :return: np.ndarray, TF-IDF vectors
    :example:
    >>> vectorize_tfidf(["This is a comment", "Another comment"]).shape
    (2, 7)
    """
    vectorizer = TfidfVectorizer(max_features=max_features)
    return vectorizer.fit_transform(texts).toarray()

def reduce_dimensions(vectors, n_components=2):
    """
    Reduce dimensionality of feature vectors using PCA.

    :param vectors: np.ndarray, vectorized data
    :param n_components: int, number of principal components to keep
    :return: np.ndarray, reduced vectors
    :example:
    >>> reduce_dimensions(np.array([[1, 2, 3], [4, 5, 6]]))
    array([[-1.5, -0.5], [1.5, 0.5]])
    """
    pca = PCA(n_components=n_components)
    return pca.fit_transform(vectors)
