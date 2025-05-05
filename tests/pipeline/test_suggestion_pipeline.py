# # tests/pipeline/test_suggestion_pipeline.py
# from textpipe.pipeline import SuggestionPipeline


# def test_suggestions():  # Changed from class-based to function-based test
#     corpus = [
#         "Python programming basics",
#         "Advanced machine learning",
#         "Web development with Django",
#         "Natural language processing",
#     ]
#     pipeline = SuggestionPipeline(n_components=2)
#     suggestions = pipeline.generate(corpus, "AI and neural networks", k=2)

#     assert len(suggestions) == 2
#     assert all(0 <= idx < len(corpus) for idx in suggestions)
