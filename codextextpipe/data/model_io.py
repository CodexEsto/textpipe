"""
Utility functions for saving and loading trained models using pickle.
"""

import pickle
import os


def save_model(model, path: str):
    """
    Save a trained model to a pickle file.

    Args:
        model: The trained model (e.g., ContentRecommender or any scikit-learn-like model).
        path (str): File path where the model should be saved (e.g., 'models/recommender.pkl').
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(model, f)


def load_model(path: str):
    """
    Load a previously saved model from a pickle file.

    Args:
        path (str): File path where the model is stored.

    Returns:
        The deserialized model object.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found at: {path}")

    with open(path, "rb") as f:
        model = pickle.load(f)

    return model


def save_vectorizer(vectorizer, path: str):
    """
    Save a trained vectorizer (e.g., TfidfVectorizer or CountVectorizer) to a pickle file.

    Args:
        vectorizer: The vectorizer object to save.
        path (str): File path where the vectorizer should be saved (e.g., 'models/vectorizer.pkl').
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(vectorizer, f)


def load_vectorizer(path: str):
    """
    Load a previously saved vectorizer from a pickle file.

    Args:
        path (str): File path where the vectorizer is stored.

    Returns:
        The deserialized vectorizer object.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Vectorizer file not found at: {path}")

    with open(path, "rb") as f:
        vectorizer = pickle.load(f)

    return vectorizer
