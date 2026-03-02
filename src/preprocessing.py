import re
import spacy

nlp = None  # global placeholder


def get_nlp():
    global nlp
    if nlp is None:
        nlp = spacy.load("en_core_web_sm")
    return nlp


def clean_text_basic(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def preprocess(
    text,
    remove_stopwords=True,
    lemmatize=True,
    keep_punctuation=False,
    pos_filter=None
):
    text = clean_text_basic(text)

    nlp_model = get_nlp()
    doc = nlp_model(text)

    tokens = []

    for token in doc:
        if not keep_punctuation and token.is_punct:
            continue

        if remove_stopwords and token.is_stop:
            continue

        if pos_filter and token.pos_ not in pos_filter:
            continue

        tokens.append(token.lemma_ if lemmatize else token.text)

    return " ".join(tokens)