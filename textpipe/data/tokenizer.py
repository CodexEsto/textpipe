import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
import string

def basic_tokenizer(text):
    """
    Tokenizes the input text by splitting on spaces and handling basic punctuation.

    Args:
        text (str): The input text to tokenize.

    Returns:
        list: A list of tokens (words).
    
    Example:
    >>> basic_tokenizer("Hello, world!")
    ['hello', 'world']
    """
    # Lowercase the text and remove punctuation
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.split()

def nltk_tokenizer(text):
    """
    Tokenizes the input text using NLTK's word_tokenize function.

    Args:
        text (str): The input text to tokenize.

    Returns:
        list: A list of tokens (words).
    
    Example:
    >>> nltk_tokenizer("Hello, world!")
    ['Hello', ',', 'world', '!']
    """
    return word_tokenize(text)

def tweet_tokenizer(text):
    """
    Tokenizes the input text using NLTK's TweetTokenizer (handles hashtags, mentions).

    Args:
        text (str): The input text to tokenize.

    Returns:
        list: A list of tokens (words, hashtags, mentions).
    
    Example:
    >>> tweet_tokenizer("Hello @user, check #Python!")
    ['Hello', '@user', ',', 'check', '#Python', '!']
    """
    tokenizer = TweetTokenizer()
    return tokenizer.tokenize(text)
