# mlops-model-serving

[![CI/CD Pipeline](https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY>/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY>/actions/workflows/ci-cd.yml)

This project provides a robust and scalable solution for serving machine learning models, specifically a sentiment analysis model, via a RESTful API. It includes features like Dockerization, Prometheus metrics, and a CI/CD pipeline.

## Features

- **FastAPI Framework**: High-performance web framework for building APIs.
- **Sentiment Analysis Model**: Utilizes a pre-trained DistilBERT model from Hugging Face Transformers for sentiment analysis.
- **Dockerized**: Easy deployment and scaling using Docker.
- **Prometheus Metrics**: Exposes metrics for monitoring request rates, latency, and errors.
- **CI/CD Ready**: GitHub Actions workflow for automated building and pushing of Docker images.

## Project Structure

- **`.github/workflows/`**: Contains GitHub Actions workflow files (e.g., `ci-cd.yml` for automated Docker image builds).
- **`app/`**: Contains the main application code.
  - `__init__.py`: Initializes the `app` as a Python package.
  - `main.py`: Defines the FastAPI application, API endpoints, request handling, and Prometheus metrics integration.
  - `model.py`: Handles the loading and inference logic for the sentiment analysis model.
  - `schemas.py`: Defines Pydantic models for API request and response data validation.
  - `templates/`: HTML templates (e.g., for the root endpoint).
- **`data/`**: (Future Use) Intended for storing data files for model retraining.
- **`models/`**: (Future Use) Intended for storing pre-trained model files if not downloaded dynamically.
- **`notebooks/`**: (Optional) For Jupyter notebooks used for experimentation or model training.
- **`tests/`**: Contains unit and integration tests.
  - `test_api.py`: Test cases for the API endpoints.
- **`Dockerfile`**: Instructions for building the Docker image for the application.
- **`requirements.txt`**: Lists Python dependencies.

## Getting Started

### Prerequisites

- Python 3.9+
- Docker (for containerized deployment)
- Git

### Local Development Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd mlops-model-serving
    ```
    *Replace `<repository-url>` with the actual URL of your repository.*

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application locally:**
    FastAPI applications are run using an ASGI server like Uvicorn.
    ```bash
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ```
    The `--reload` flag enables auto-reloading when code changes are detected. The application will be available at `http://localhost:8000`.

### Running Tests

To run the automated tests (ensure you have `pytest` installed, or add it to `requirements.txt` and your testing setup):
```bash
pytest
```
*(Note: Add `pytest` to `requirements-dev.txt` or `requirements.txt` if you want to formalize it as a project dependency).*

## API Documentation

Once the application is running, interactive API documentation is available at:

-   **Swagger UI**: `http://localhost:8000/docs`
-   **ReDoc**: `http://localhost:8000/redoc`

These interfaces allow you to explore the API endpoints, view schemas, and test them directly in your browser.

### Endpoints

-   **`GET /`**: Serves a simple HTML landing page.
-   **`POST /predict`**: Accepts a JSON payload with a `text` field and returns the sentiment prediction (`POSITIVE` or `NEGATIVE`) and a confidence score.
    -   Request Body:
        ```json
        {
          "text": "This is a wonderful library!"
        }
        ```
    -   Response Body:
        ```json
        {
          "text": "This is a wonderful library!",
          "prediction": "POSITIVE",
          "confidence": 0.9998
        }
        ```
-   **`GET /metrics`**: Exposes Prometheus-compatible metrics for monitoring. Key metrics include:
    -   `inference_requests_total`: Total number of inference requests, labeled by prediction.
    -   `inference_latency_seconds`: Histogram of inference request latency.
    -   `inference_errors_total`: Total number of errors during inference.

## Docker Deployment

The application can be easily deployed using Docker.

1.  **Build the Docker image:**
    ```bash
    docker build -t mlops-model-serving .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -d -p 8000:8000 --name model-server mlops-model-serving
    ```
    -   `-d`: Run in detached mode.
    -   `-p 8000:8000`: Map port 8000 of the host to port 8000 of the container.
    -   `--name model-server`: Assign a name to the container.

    The application will be accessible at `http://localhost:8000`.

## CI/CD

This project uses GitHub Actions for CI/CD. The workflow in `.github/workflows/ci-cd.yml` automatically builds and pushes the Docker image to the GitHub Container Registry (`ghcr.io`) on every push or pull request to the `main` branch.

**Important:** To make the CI/CD badge at the top of this README work, replace `<YOUR_USERNAME>` and `<YOUR_REPOSITORY>` with your actual GitHub username and repository name.

## Model Information

The sentiment analysis functionality is powered by a pre-trained model from the Hugging Face Transformers library. By default, it uses `distilbert-base-uncased-finetuned-sst-2-english`, a smaller and faster version of BERT, fine-tuned for sentiment classification on the SST-2 dataset.

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

Please open an issue to discuss significant changes before starting work.

## License

Specify your project's license here (e.g., MIT, Apache 2.0). If not specified, assume it's proprietary.


![image](https://github.com/user-attachments/assets/4f063b9f-a626-4be4-978d-e22ea680a387)
