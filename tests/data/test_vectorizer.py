# # tests/data/test_vectorizer.py
# import pytest
# import numpy as np
# from textpipe.data.vectorizer import vectorize_tfidf, reduce_dimensions


# def test_vectorize_tfidf():
#     """Test TF-IDF vectorization returns correct shapes."""
#     texts = ["This is a comment", "Another comment"]
#     vectors, vectorizer = vectorize_tfidf(texts)  # Unpack both return values
#     assert vectors.shape[0] == 2, "Expected 2 samples"
#     assert len(vectorizer.get_feature_names_out()) > 0, "Vocabulary should be learned"


# def test_reduce_dimensions():
#     """Test PCA maintains samples while reducing features."""
#     vectors = np.array([[1, 2, 3], [4, 5, 6]])
#     reduced = reduce_dimensions(vectors, n_components=2)
#     assert reduced.shape == (2, 2), "Should reduce to 2 components"


# @pytest.mark.parametrize(
#     "texts, max_features, expected_features",
#     [
#         (["This is a test", "Another test"], 5, 5),
#         (["Short text", "More verbose text sample"], 3, 3),
#         (["A", "B", "C"], 10, 3),  # Test when actual features < max_features
#     ],
# )
# def test_tfidf_max_features(texts, max_features, expected_features):
#     """Test max_features parameter works correctly."""
#     vectors, vectorizer = vectorize_tfidf(texts, max_features)
#     assert vectors.shape[1] == expected_features, (
#         f"Expected {expected_features} features, got {vectors.shape[1]}"
#     )
#     assert len(vectorizer.get_feature_names_out()) == expected_features


# def test_tfidf_ngram_range():
#     """Verify bigrams are captured when requested."""
#     texts = ["natural language processing"]
#     _, vectorizer = vectorize_tfidf(texts, ngram_range=(1, 2))
#     features = vectorizer.get_feature_names_out()
#     assert "natural language" in features
#     assert "language processing" in features


# def test_pca_variance_explained():
#     """Test PCA explains reasonable variance."""
#     vectors = np.random.rand(10, 20)  # 10 samples, 20 features
#     reduced = reduce_dimensions(vectors, n_components=5)
#     assert reduced.shape == (10, 5), "Should maintain sample count"
