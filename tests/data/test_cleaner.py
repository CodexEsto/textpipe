# tests/data/test_cleaner.py

import pytest
from textpipe.data.cleaner import clean_text, remove_stopwords


def test_clean_text():
    """Test basic text cleaning functionality."""
    raw_text = "Hello, world! How's it going?"
    cleaned_text = clean_text(raw_text)
    assert cleaned_text == "hello world how's it going", "Basic cleaning failed"


def test_remove_stopwords():
    """Test stopword removal with case insensitivity."""
    text = "This is a sample text"
    stopwords = {"is", "the", "a", "in", "to", "and", "this"}
    cleaned_text = remove_stopwords(text, stopwords)
    assert cleaned_text == "sample text", "Stopword removal failed"


@pytest.mark.parametrize(
    "raw_text, expected_cleaned_text",
    [
        ("Hello!!!", "hello"),
        ("Python is awesome.", "python is awesome"),
        ("   Space   and   punctuation!   ", "space and punctuation"),
    ],
)
def test_clean_text_various_cases(raw_text, expected_cleaned_text):
    """Test edge cases and various input formats."""
    cleaned_text = clean_text(raw_text)
    assert cleaned_text == expected_cleaned_text, (
        f"Expected '{expected_cleaned_text}', got '{cleaned_text}'"
    )
