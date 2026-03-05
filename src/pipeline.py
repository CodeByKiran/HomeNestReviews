from preprocessing import preprocess
from topic_model import assign_topic
from sentiment import get_sentiment
from summarizer import abstractive_summary


def analyze_review(review_text, product_category=None):

    result = {}

    # Phase 2: Preprocessing
    cleaned_topics = preprocess(
        review_text,
        remove_stopwords=True
    )

    cleaned_sentiment = preprocess(
        review_text,
        remove_stopwords=False
    )

    result['cleaned_for_topics'] = cleaned_topics
    result['cleaned_for_sentiment'] = cleaned_sentiment

    # Phase 3: Topic Modeling
    result['dominant_topic'] = assign_topic(cleaned_topics)

    # Phase 4: Sentiment
    sentiment, stars, confidence = get_sentiment(cleaned_sentiment)

    result['sentiment'] = sentiment
    result['stars'] = stars
    result['confidence'] = confidence

    # Phase 5: Summarization
    result['summary'] = abstractive_summary(review_text)

    return result