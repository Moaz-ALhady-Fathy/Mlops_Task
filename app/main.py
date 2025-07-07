import logging
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from prometheus_client import generate_latest, Counter, Histogram # Import Prometheus metrics
from starlette.responses import Response # For custom metrics endpoint

from .schemas import PredictionRequest, PredictionResponse
from .model import sentiment_model

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Sentiment Analysis Model API",
    description="A simple API for sentiment analysis using DistilBERT.",
    version="1.0.0"
)

templates = Jinja2Templates(directory="app/templates")

# Prometheus Metrics
INFERENCE_REQUESTS_TOTAL = Counter(
    'inference_requests_total',
    'Total number of inference requests',
    ['prediction_label'] # Label to count by sentiment (e.g., positive, negative)
)
INFERENCE_LATENCY_SECONDS = Histogram(
    'inference_latency_seconds',
    'Latency of inference requests in seconds'
)
INFERENCE_ERRORS_TOTAL = Counter(
    'inference_errors_total',
    'Total number of inference errors'
)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    logger.info("UI requested.")
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_model=PredictionResponse)
async def predict_sentiment(request: PredictionRequest):
    logger.info(f"Prediction request received for text: '{request.text[:50]}...'")
    with INFERENCE_LATENCY_SECONDS.time(): # Measure latency
        try:
            label, score = sentiment_model.predict(request.text)
            INFERENCE_REQUESTS_TOTAL.labels(prediction_label=label).inc() # Increment counter with label
            logger.info(f"Prediction successful: Label='{label}', Confidence={score:.4f} for text: '{request.text[:50]}...'")
            return PredictionResponse(text=request.text, prediction=label, confidence=score)
        except Exception as e:
            INFERENCE_ERRORS_TOTAL.inc() # Increment error counter
            logger.error(f"Prediction failed for text: '{request.text[:50]}...': {e}", exc_info=True)
            raise HTTPException(status_code=500, detail="Internal server error during prediction.")

@app.get("/metrics")
async def metrics():
    """
    Exposes Prometheus metrics.
    """
    return Response(generate_latest(), media_type="text/plain")