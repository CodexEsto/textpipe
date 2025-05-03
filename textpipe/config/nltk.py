# textpipe/_config.py

import os
import nltk


def configure_nltk():
    """Initialize NLTK with custom settings"""
    nltk_data_path = os.path.join(os.path.expanduser("~"), "nltk_data")
    os.makedirs(nltk_data_path, exist_ok=True)

    if nltk_data_path not in nltk.data.path:
        nltk.data.path.append(nltk_data_path)

    _download_resource("punkt_tab", nltk_data_path)
    _download_resource("averaged_perceptron_tagger", nltk_data_path)


def _download_resource(name, path):
    """Internal helper for resource downloads"""
    try:
        nltk.data.find(f"tokenizers/{name}")
    except LookupError:
        nltk.download(name, download_dir=path, quiet=True)
