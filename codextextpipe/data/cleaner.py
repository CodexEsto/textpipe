"""Text cleaning functions."""

import re


def clean_text(text):
    """
    Clean text based on configuration.

    Args:
        text: Input text string
        config: Config object with cleaning parameters

    Returns:
        Cleaned text string
    """
    pattern = r"[^a-zA-Z\s]" 
    cleaned = re.sub(pattern, "", text)
    # if len(cleaned) < config.min_text_length:
    #     return ''
    # # Numeric handling
    # if not config.allow_numeric:
    #     cleaned = re.sub(r'\d+', '', cleaned)
    return cleaned.lower().strip() 
