import pickle
import os
from sklearn.decomposition import LatentDirichletAllocation


def train_lda_model(dtm, vectorizer, n_topics=8, top_n_words=10, print_output=True):
    """
    Train an LDA model and optionally print top words per topic.
    """

    lda_model = LatentDirichletAllocation(
        n_components=n_topics,
        max_iter=20,
        learning_method="online",
        random_state=42
    )

    lda_model.fit(dtm)

    perplexity = lda_model.perplexity(dtm)

    if print_output:
        words = vectorizer.get_feature_names_out()

        print(f"\n===== LDA Model with {n_topics} Topics =====")
        print(f"Perplexity: {perplexity:.2f}\n")

        for idx, topic in enumerate(lda_model.components_):
            top_words = [words[i] for i in topic.argsort()[-top_n_words:]]
            print(f"Topic {idx}: {', '.join(top_words)}")

    return lda_model, perplexity


# ---------------------------------------------------
# Load trained model and vectorizer
# ---------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "topic_model.pkl")

with open(MODEL_PATH, "rb") as f:
    lda_model, vectorizer = pickle.load(f)


# ---------------------------------------------------
# Human-readable topic labels
# ---------------------------------------------------

topic_labels = {
    0: "Product Defects",
    1: "Delivery Issues",
    2: "Customer Support",
    3: "Pricing & Value",
    4: "Product Quality",
    5: "Ease of Use",
    6: "Bedroom Furniture (Bed Frames)",
    7: "Home Comfort Products",
    8: "Warranty & Returns",
    9: "General Feedback"
}


# ---------------------------------------------------
# Assign topic to new review
# ---------------------------------------------------

def assign_topic(cleaned_text):
    """
    Assign dominant topic for a cleaned review
    """

    text_vector = vectorizer.transform([cleaned_text])

    topic_probs = lda_model.transform(text_vector)

    topic_index = topic_probs.argmax()

    return topic_labels.get(topic_index, f"Topic {topic_index}")