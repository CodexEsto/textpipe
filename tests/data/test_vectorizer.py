import pytest
import numpy as np
from textpipe.data.vectorizer import vectorize_tfidf, reduce_dimensions

def test_vectorize_tfidf():
    """Test TF-IDF vectorization."""
    texts = ["This is a comment", "Another comment"]
    vectors = vectorize_tfidf(texts)
    assert vectors.shape == (2, 7), "Expected vectorized shape (2, 7)."


def test_reduce_dimensions():
    """Test PCA dimensionality reduction."""
    vectors = np.array([[1, 2, 3], [4, 5, 6]])
    reduced_vectors = reduce_dimensions(vectors, n_components=2)
    assert reduced_vectors.shape == (2, 2), "Expected reduced shape (2, 2)."


@pytest.mark.parametrize(
    "texts, max_features, expected_shape",
    [
        (["This is a comment", "Another comment"], 5, (2, 5)),
        (["Short text", "Longer text here"], 3, (2, 3))
    ]
)
def test_tfidf_with_max_features(texts, max_features, expected_shape):
    """Test TF-IDF with max_features parameter."""
    vectors = vectorize_tfidf(texts, max_features=max_features)
    assert vectors.shape == expected_shape, f"Expected shape {expected_shape}, got {vectors.shape}"
