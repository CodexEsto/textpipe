from setuptools import setup, find_packages

setup(
    name="textpipe",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "scikit-learn",
        "nltk",
        "pandas",
        "sphinx",
        "pytest",  # Usually listed under extras, but fine here too
    ],
    author="Your Name",
    description="all in one tool for text tokenization and vectorization",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
