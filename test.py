from codextextpipe.data.model_io import (
    save_model,
    load_model,
    save_vectorizer,
    load_vectorizer,
)
from codextextpipe.core.recommender import ContentRecommender
from codextextpipe.pipeline import SuggestionPipeline
from codextextpipe.config import Config

# Load the configuration
config = Config.get()

# Sample text data
sample_texts = [
    # Education
    "Online learning platforms are transforming education.",
    "Teachers use AI tools to personalize lessons.",
    "Distance learning increased during the pandemic.",
    # Politics
    "The government passed a new environmental bill.",
    "Elections will be held next year amid rising tensions.",
    "A new policy was announced by the health minister.",
    # Technology
    "Quantum computing promises exponential speedup.",
    "New AI models are revolutionizing software development.",
    "Cybersecurity threats are growing in the tech world.",
    # Environment
    "Climate change is causing rising sea levels.",
    "Renewable energy is crucial for sustainability.",
    "Deforestation threatens biodiversity globally.",
    # Business
    "Stock markets surged after the merger announcement.",
    "Startups are attracting record venture capital funding.",
    "Remote work is reshaping corporate culture.",
    # Sports
    "The team won the championship after a tough season.",
    "The Olympic Games are scheduled for next summer.",
    "Athletes are training hard for the world cup."
]


# Initialize the pipeline using loaded config
pipeline = SuggestionPipeline(config=config)

# Fit the pipeline with the sample data
pipeline.fit(sample_texts)

# Save model and vectorizer
# save_model(pipeline.recommender, "models/recommender.pkl")
# save_vectorizer(pipeline.vectorizer, "models/vectorizer.pkl")

# Load saved model and vectorizer
# loaded_recommender = load_model("models/recommender.pkl")
# loaded_vectorizer = load_vectorizer("models/vectorizer.pkl")

# Create a new pipeline with loaded objects
# new_pipeline = SuggestionPipeline(config=config)
# new_pipeline.recommender = loaded_recommender
# new_pipeline.vectorizer = loaded_vectorizer

# Query for testing
query = "How is AI changing education?"
recommendations = pipeline.suggest(query, k=3)

# Display recommendations
print(f"Recommendations for the query '{query}':")
for rec in recommendations:
    print(rec)
