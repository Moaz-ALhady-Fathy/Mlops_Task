from transformers import pipeline

class SentimentModel:
    def __init__(self):
        # Load a pre-trained sentiment analysis model from Hugging Face Transformers
        # This will download the model the first time it's run
        self.pipeline = pipeline("sentiment-analysis")

    def predict(self, text: str):
        # Perform prediction
        result = self.pipeline(text)[0]
        label = result['label']
        score = result['score']
        return label, score

# Global model instance to avoid reloading for each request
sentiment_model = SentimentModel()