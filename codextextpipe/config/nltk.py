"""NLTK resource management."""

import nltk


def download_nltk_resources():
    """Download required NLTK datasets."""
    resources = {"tokenizers": ["punkt"], "corpora": ["stopwords"]}

    for category, names in resources.items():
        for name in names:
            try:
                nltk.data.find(f"{category}/{name}")
            except LookupError:
                nltk.download(name)
