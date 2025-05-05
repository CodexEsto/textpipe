# from textpipe.pipeline import SentimentPipeline


# class TestSentimentPipeline:
#     def test_pipeline():
#         texts = ["Excellent service!", "Worst experience ever.", "It was okay."]
#         labels = [1, 0, 0]  # Added required labels

#         pipeline = SentimentPipeline()
#         pipeline.run(texts, labels)  # Train first
#         scores = pipeline.run(texts)  # Now predict

#         assert len(scores) == 3
#         assert scores[0] > scores[1]
