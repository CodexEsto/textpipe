import pytest
from textpipe.data.tokenizer import basic_tokenizer, nltk_tokenizer, tweet_tokenizer


def test_basic_tokenizer():
    """Test basic_tokenizer function."""
    text = "Hello, world!"
    tokens = basic_tokenizer(text)
    assert tokens == ['hello', 'world'], f"Expected ['hello', 'world'], got {tokens}"


def test_nltk_tokenizer():
    """Test nltk_tokenizer function."""
    text = "Hello, world!"
    tokens = nltk_tokenizer(text)
    assert tokens == ['Hello', ',', 'world', '!'], f"Expected ['Hello', ',', 'world', '!'], got {tokens}"


def test_tweet_tokenizer():
    """Test tweet_tokenizer function."""
    text = "Hello @user, check out #Python!"
    tokens = tweet_tokenizer(text)
    assert tokens == ['Hello', '@user', ',', 'check', 'out', '#Python', '!'], f"Expected ['Hello', '@user', ',', 'check', 'out', '#Python', '!'], got {tokens}"


@pytest.mark.parametrize(
    "text, expected_tokens",
    [
        ("This is a test.", ['this', 'is', 'a', 'test']),
        ("Tokenize @user and #tags!", ['tokenize', '@user', 'and', '#tags']),
        ("Python's great, isn't it?", ['python', 's', 'great', 'isn', 't', 'it'])
    ]
)
def test_tokenize_various_cases(text, expected_tokens):
    """Test tokenizer with various input cases."""
    tokens = basic_tokenizer(text)
    assert tokens == expected_tokens, f"Expected {expected_tokens}, got {tokens}"
