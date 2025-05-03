from . import data
from . import models
from . import pipeline
from . import utils

__all__ = ["data", "models", "pipeline", "utils"]  # Public API


# Import and configure NLTK
from .config import configure_nltk

# Initialize NLTK when package is imported
configure_nltk()
