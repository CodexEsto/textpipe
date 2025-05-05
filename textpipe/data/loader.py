"""Enhanced data loader with config-aware processing."""

import pandas as pd
from ..utils.logger import logger
from ..config.config import Config

config = Config.get()


def load_csv(path, text_column="text", label_column="label"):
    """Load and pre-process CSV data with type validation."""
    try:
        df = pd.read_csv(path)

        # Handle missing values based on config
        if config.handle_nan == "drop":
            df = df.dropna(subset=[text_column])
        else:
            df[text_column] = df[text_column].fillna("")

        # Convert to strings and clean invalid characters
        df[text_column] = (
            df[text_column]
            .astype(str)
            .apply(lambda x: x.encode("ascii", "ignore").decode().strip())
        )

        texts = df[text_column].tolist()
        labels = df[label_column].tolist() if label_column in df.columns else None

        logger.info(f"Loaded {len(texts)} documents from {path}")
        return (texts, labels) if labels else texts

    except Exception as e:
        logger.error(f"Error loading CSV: {str(e)}")
        raise


def load_txt(path):
    """Load text from a .txt file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [f.read()]
    except Exception as e:
        logger.error(f"Error loading text file: {str(e)}")
        raise


# TODO: Implement load_json and load_html functions with the same load_csv structure
