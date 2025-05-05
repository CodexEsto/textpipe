"""Configuration management with YAML support."""

import os
import yaml
from pathlib import Path


class Config:
    _instance = None

    def __init__(self):
        self.config_path = Path(__file__).parent.parent / "config.yml"
        self._load_config()

    @classmethod
    def get(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def _load_config(self):
        defaults = {
            "processing": {
                "n_components": 25,
                "language": "english",
                "remove_stopwords": True,
                "use_stemming": False,
                "max_features": 1000,
                "allow_numeric": False,
                "min_text_length": 3,
                "handle_nan": "empty",
            },
            "logging": {"level": "INFO"},
        }

        if self.config_path.exists():
            with open(self.config_path) as f:
                self.config = {**defaults, **yaml.safe_load(f)}
        else:
            self.config = defaults

    def __getattr__(self, name):
        return self.config.get(name)
