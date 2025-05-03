import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "textpipe"
copyright = "2025, Codex"
author = "Codex"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

autosummary_generate = True
napoleon_google_docstring = True
napoleon_numpy_docstring = True

templates_path = ["_templates"]

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "textpipe.config.rst",
    "textpipe.data.rst",
    "textpipe.models.rst",
    "textpipe.pipeline.rst",
    "textpipe.utils.rst",
]


# HTML output options
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

html_theme_options = {
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "show_toc_level": 2,
    "navigation_with_keys": True,
}

html_context = {
    "github_user": "your-github-username",
    "github_repo": "textpipe",
    "github_version": "main",
    "doc_path": "docs",
}
