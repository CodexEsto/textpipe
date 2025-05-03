import re
from nltk.tokenize import word_tokenize, TweetTokenizer


def basic_tokenizer(text):
    """
    Tokenizes text by:
    - Lowercasing
    - Splitting contractions via apostrophes
    - Preserving @ and # symbols
    - Splitting on spaces

    :param str text: Input text to tokenize
    :return: List of tokens
    :rtype: list

    Example:
        >>> basic_tokenizer("Python's great, isn't it?")
        ['python', 's', 'great', 'isn', 't', 'it']
    """
    text = text.lower()
    text = re.sub(r"['’]", " ", text)  # Split contractions
    text = re.sub(r"[^\w\s@#]", "", text)  # Remove unwanted chars
    return text.split()


def nltk_tokenizer(text):
    """
    Tokenizes text using NLTK's word_tokenize with pre-configured resources.

    :param str text: Input text to tokenize
    :return: List of tokens
    :rtype: list

    Example:
        >>> nltk_tokenizer("Hello, world!")
        ['Hello', ',', 'world', '!']
    """
    return word_tokenize(text)


def tweet_tokenizer(text):
    """
    Tokenizes text using NLTK's TweetTokenizer.

    :param str text: Input text to tokenize
    :return: List of tokens
    :rtype: list

    Example:
        >>> tweet_tokenizer("Hello @user, check #Python!")
        ['Hello', '@user', ',', 'check', '#Python', '!']
    """
    return TweetTokenizer().tokenize(text)
