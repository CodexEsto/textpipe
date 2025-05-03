import pytest
from textpipe.data.loader import load_csv, load_json, load_txt, load_html


def test_load_csv():
    """Test loading CSV file."""
    data = load_csv("data/tests/comments.csv")
    assert not data.empty, "CSV file should load data correctly."


def test_load_json():
    """Test loading JSON file."""
    data = load_json("data/tests/comments.json")
    assert isinstance(data, list), "JSON file should load into a dictionary."


def test_load_txt():
    """Test loading TXT file."""
    data = load_txt("data/tests/comments.txt")
    assert isinstance(data, list), "TXT file should load data as a list of strings."
    assert len(data) > 0, "TXT file should contain at least one line."


def test_load_html():
    """Test loading HTML file."""
    data = load_html("data/tests/comments.html")
    assert isinstance(data, str), "HTML file should load into a string."
    assert len(data) > 0, "HTML file should contain text content."


@pytest.mark.parametrize(
    "file_path, expected_exception",
    [
        ("data/non_existent.csv", FileNotFoundError),
        ("data/non_existent.json", FileNotFoundError),
        ("data/non_existent.txt", FileNotFoundError),
    ],
)
def test_file_not_found(file_path, expected_exception):
    """Test that loading non-existent files raises FileNotFoundError."""
    with pytest.raises(expected_exception):
        if file_path.endswith(".csv"):
            load_csv(file_path)
        elif file_path.endswith(".json"):
            load_json(file_path)
        elif file_path.endswith(".txt"):
            load_txt(file_path)
        else:
            load_html(file_path)
