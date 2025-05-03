# # tests/config/test_nltk.py

# import shutil
# import pytest
# import nltk
# import os
# from textpipe.config import configure_nltk

# @pytest.fixture(autouse=True)
# def clean_nltk_environment(monkeypatch, tmp_path):
#     """
#     Provides a clean NLTK environment for each test
#     Ensures tests don't interfere with each other
#     """
#     # Mock user home to temporary path
#     monkeypatch.setattr(os.path, 'expanduser', lambda _: str(tmp_path))
    
#     # Clear NLTK's internal paths
#     nltk.data.path.clear()
    
#     # Remove any existing test data
#     nltk_dir = tmp_path / "nltk_data"
#     if nltk_dir.exists():
#         shutil.rmtree(nltk_dir)

# def test_full_configuration():
#     """
#     Comprehensive test of NLTK configuration
#     Covers both modern and legacy resource access
#     """
#     configure_nltk()
    
#     # Verify modern resources
#     assert nltk.data.find('tokenizers/punkt'), "Modern punkt resource missing"
#     assert nltk.data.find('taggers/averaged_perceptron_tagger'), "POS tagger missing"
    
#     # Verify legacy structure
#     nltk_dir = os.path.expanduser("~/nltk_data")
    
#     # Check main symlink
#     legacy_root = os.path.join(nltk_dir, 'tokenizers/punkt_tab')
#     assert os.path.islink(legacy_root), "Main legacy symlink not created"
#     assert os.path.realpath(legacy_root) == os.path.join(nltk_dir, 'tokenizers/punkt')
    
#     # Check language-specific symlink
#     legacy_lang = os.path.join(legacy_root, 'english')
#     if os.path.exists(legacy_lang):  # Some NLTK versions don't have language subdirs
#         assert os.path.islink(legacy_lang), "Language symlink missing"
#         assert os.path.realpath(legacy_lang) == os.path.join(nltk_dir, 'tokenizers/punkt/english')