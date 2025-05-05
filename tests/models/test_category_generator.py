# # tests/test_category_generator.py
# """
# Integration test for news article category generation using title + body.
# Dataset columns: category, title, body
# """

# import pandas as pd
# from textpipe.pipeline.category_generator import CategoryGenerator
# from textpipe.data.cleaner import clean_text
# from sklearn.metrics import adjusted_rand_score


# def test_news_category_generation():
#     # Load dataset
#     df = pd.read_csv("data/news-article-categories.csv")

#     # Validate columns
#     assert {"category", "title", "body"}.issubset(df.columns), (
#         "Missing required columns"
#     )

#     # Preprocess text
#     df = df.dropna(subset=["title", "body"])
#     df["text"] = df["title"] + " " + df["body"]
#     texts = df["text"].apply(clean_text).tolist()
#     true_labels = df["category"].astype("category").cat.codes

#     # Initialize generator with parameters suitable for news data
#     generator = CategoryGenerator(
#         n_categories=10,  # Match typical news category counts
#         method="lda",  # Better for topic modeling
#     )
#     generator.fit(texts[:1000])  # Use subset for faster testing

#     # Generate predictions
#     predicted_labels = generator.predict(texts[:100])
#     topic_keywords = generator.get_topic_keywords(n_words=8)

#     # Evaluate clustering
#     ari = adjusted_rand_score(true_labels[:100], predicted_labels)

#     print("\nNews Category Generation Results:")
#     print(f"Adjusted Rand Index: {ari:.2f}")
#     for topic, keywords in topic_keywords.items():
#         print(f"\nTopic {topic}: {', '.join(keywords)}")
#         print("Sample titles:")
#         for title in df[predicted_labels == topic]["title"].head(3):
#             print(f"- {title[:60]}...")

#     # Validation thresholds
#     assert ari > 0.2, "Categories not matching actual labels sufficiently"
#     assert len(topic_keywords) >= 5, "Insufficient distinct topics generated"


# # To run: pytest tests/test_category_generator.py -v -s
