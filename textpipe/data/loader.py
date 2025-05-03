import pandas as pd
import json
import os


def load_csv(file_path):
    """
    Load a CSV file into a pandas DataFrame.

    :param file_path: str, path to the CSV file
    :return: pd.DataFrame, loaded CSV data
    :example:
    >>> load_csv('data/comments.csv').head()
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    return pd.read_csv(file_path)


def load_json(file_path):
    """
    Load a JSON file into a Python dictionary.

    :param file_path: str, path to the JSON file
    :return: dict, loaded JSON data
    :example:
    >>> load_json('data/comments.json')['comments'][0]
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, "r") as file:
        return json.load(file)


def load_txt(file_path):
    """
    Load a plain text file.

    :param file_path: str, path to the text file
    :return: list, each line in the text file
    :example:
    >>> load_txt('data/comments.txt')[:2]
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, "r") as file:
        return file.readlines()


def load_html(file_path):
    """
    Load an HTML file and extract text content.

    :param file_path: str, path to the HTML file
    :return: str, extracted text content
    :example:
    >>> load_html('data/comments.html')[:100]
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, "r") as file:
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(file, "html.parser")
        return soup.get_text()
