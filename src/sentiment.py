
import pandas as pd
from transformers import pipeline
from tqdm import tqdm

class SentimentAnalyzer:
    def __init__(self, model_name="nlptown/bert-base-multilingual-uncased-sentiment"):
        self.pipeline = pipeline("sentiment-analysis", model=model_name)

    def predict(self, text, max_len=512):
        text = str(text)[:max_len]  # truncate long reviews
        result = self.pipeline(text)[0]
        stars = int(result["label"][0])
        confidence = result["score"]
        
        if stars <= 2:
            sentiment = "Negative"
        elif stars == 3:
            sentiment = "Neutral"
        else:
            sentiment = "Positive"

        return sentiment, stars, confidence

    def apply_to_dataframe(self, df, column="text_for_sentiment"):
        tqdm.pandas()
        results = df[column].progress_apply(lambda x: self.predict(x))
        df["sentiment"] = results.apply(lambda x: x[0])
        df["predicted_stars"] = results.apply(lambda x: x[1])
        df["confidence"] = results.apply(lambda x: x[2])
        return df