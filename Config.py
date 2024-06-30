import os

AZURE_KEY = os.environ.get("AZURE_KEY")
AZURE_ENDPOINT = os.environ.get("AZURE_ENDPOINT")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
MLFLOW_TRACKING_URI = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000")  # Local MLflow tracking server by default
