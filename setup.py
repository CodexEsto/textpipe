from setuptools import setup, find_packages

setup(
    name="Textpipe",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "scikit-learn",
        "nltk",
        "pandas",
        "sphinx",
        "bs4",
        "beautifulsoup4",
        "pytest",  # Usually listed under extras, but fine here too
    ],
    author="Textpipe Team",
    author_email="codexesto@gmail.com",
    license="MIT",
    python_requires=">=3.6",
    keywords="text processing, text analysis, natural language processing",
    description="all in one tool for text processing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/CodexEsto/textpipe",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    
)
