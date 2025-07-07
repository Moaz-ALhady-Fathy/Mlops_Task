import logging
from transformers import pipeline

logger = logging.getLogger(__name__)

class SentimentModel:
    def __init__(self):
        logger.info("Loading sentiment analysis model...")
        # Load a pre-trained sentiment analysis model from Hugging Face Transformers
        self.pipeline = pipeline("sentiment-analysis")
        logger.info("Sentiment analysis model loaded successfully.")

    def predict(self, text: str):
        logger.debug(f"Performing inference for text: '{text[:50]}...'")
        result = self.pipeline(text)[0]
        label = result['label']
        score = result['score']
        logger.debug(f"Inference complete: Label='{label}', Score={score:.4f}")
        return label, score

sentiment_model = SentimentModel()