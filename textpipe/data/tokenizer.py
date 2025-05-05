"""Multilingual text tokenization with NLTK."""

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, SnowballStemmer
from textpipe.config.nltk import download_nltk_resources

download_nltk_resources()


def tokenize(text, config):
    """
    Tokenize text with optional stopword removal and stemming.
    Supports multiple languages (for stopwords and stemming).

    Args:
        text: Cleaned text string
        config: Config object with attributes:
            - language: Language code (e.g., 'english', 'french', etc.)
            - remove_stopwords: bool
            - use_stemming: bool

    Returns:
        List of processed tokens
    """
    tokens = word_tokenize(text, language=config.language)

    # Remove stopwords
    if config.remove_stopwords:
        try:
            stop_words = set(stopwords.words(config.language))
            tokens = [t for t in tokens if t.lower() not in stop_words]
        except OSError:
            raise ValueError(f"Stopwords not available for language: {config.language}")

    # Apply stemming
    if config.use_stemming:
        try:
            if config.language.lower() == "english":
                stemmer = PorterStemmer()
            else:
                stemmer = SnowballStemmer(config.language.lower())
            tokens = [stemmer.stem(t) for t in tokens]
        except ValueError:
            raise ValueError(f"Stemming not supported for language: {config.language}")

    return tokens
