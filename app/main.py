from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles # Import StaticFiles if you plan to serve static assets

from .schemas import PredictionRequest, PredictionResponse
from .model import sentiment_model

app = FastAPI(
    title="Sentiment Analysis Model API",
    description="A simple API for sentiment analysis using DistilBERT.",
    version="1.0.0"
)

# Configure Jinja2Templates to load templates from the "templates" directory
templates = Jinja2Templates(directory="app/templates")

# Mount a directory to serve static files (optional, but good practice if you have more assets)
# app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serves the sentiment analysis UI.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_model=PredictionResponse)
async def predict_sentiment(request: PredictionRequest):
    """
    Predicts the sentiment of the given text.
    """
    label, score = sentiment_model.predict(request.text)
    return PredictionResponse(text=request.text, prediction=label, confidence=score)