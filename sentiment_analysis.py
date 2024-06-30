from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from llama_index.core.tools import FunctionTool
from config import AZURE_KEY, AZURE_ENDPOINT

text_analytics_client = TextAnalyticsClient(endpoint=AZURE_ENDPOINT, credential=AzureKeyCredential(AZURE_KEY))

def analyze_sentiment_batch(texts, batch_size=10):
    results = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        documents = [{"id": str(j), "language": "en", "text": text} for j, text in enumerate(batch)]
        response = text_analytics_client.analyze_sentiment(documents=documents)
        results.extend([{"id": doc["id"], "sentiment": doc["sentiment"]} for doc in response])
    return results

sentiment_analysis_tool = FunctionTool.from_defaults(analyze_sentiment_batch, name="SentimentAnalysisTool", description="Analyze sentiment of financial news in batches")
