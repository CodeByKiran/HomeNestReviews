from transformers import pipeline

# Load once globally
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)


def get_sentiment(text, max_len=512):
    text = str(text)[:max_len]

    result = sentiment_pipeline(text)[0]

    stars = int(result["label"][0])
    confidence = result["score"]

    if stars <= 2:
        sentiment = "Negative"
    elif stars == 3:
        sentiment = "Neutral"
    else:
        sentiment = "Positive"

    return sentiment, stars, confidence