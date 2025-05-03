import re


def clean_text(text):
    """
    Clean the input text by removing punctuation (except apostrophes), converting to lowercase,
    and normalizing whitespace.

    :param str text: Input raw text
    :return: Cleaned text with consistent formatting
    :rtype: str

    Example:
        >>> clean_text("Hello, world! How's it going?")
        'hello world how's it going'
        >>> clean_text("   Space   and   punctuation!   ")
        'space and punctuation'
    """
    text = text.lower()
    text = re.sub(r"[^\w\s']", "", text)  # Keep apostrophes
    text = re.sub(r"\s+", " ", text)  # Normalize whitespace
    return text.strip()


def remove_stopwords(text, stopwords):
    """
    Remove stopwords from text while preserving original word order.

    :param str text: Input text to process
    :param set stopwords: Set of stopwords to remove
    :return: Text with stopwords removed
    :rtype: str

    Example:
        >>> stopwords = {"is", "the", "in", "a", "to"}
        >>> remove_stopwords("This is a sample text", stopwords)
        'sample text'
    """
    words = clean_text(text).split()
    lower_stopwords = {s.lower() for s in stopwords}
    return " ".join([word for word in words if word not in lower_stopwords])
