import re
import string

def clean_text(text):
    """
    Clean the input text by removing punctuation, converting to lowercase, and stripping extra spaces.

    :param text: str, input raw text
    :return: str, cleaned text
    :example:
    >>> clean_text("Hello, world! How's it going?")
    'hello world hows it going'
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single one
    return text.strip()  # Remove leading/trailing spaces



# def clean_text(text):
#     text = re.sub(r'[^a-z\s]', '', text)  # Remove punctuation
#     text = re.sub(r'\s+', ' ', text)      # Normalize spaces
#     return text.strip()  
def remove_stopwords(text, stopwords):
    """
    Remove stopwords from the text.

    :param text: str, input text
    :param stopwords: set, set of stopwords to be removed
    :return: str, text without stopwords
    :example:
    >>> stopwords = {"is", "the", "in", "a", "to"}
    >>> remove_stopwords("This is a sample text", stopwords)
    'sample text'
    """
    words = text.split()
    return ' '.join([word for word in words if word.lower() not in stopwords])
