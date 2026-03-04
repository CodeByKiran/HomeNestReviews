import spacy
from transformers import pipeline
from heapq import nlargest

def extractive_summary(text, num_sentences=1):

    nlp = spacy.load('en_core_web_sm')

    doc = nlp(text)

    word_freq = {}

    for token in doc:

     if not token.is_stop and not token.is_punct:

        word_freq[token.text.lower()] = word_freq.get(token.text.lower(), 0) + 1

    sentence_scores = {}

    for sent in doc.sents:

        for word in sent:

            if word.text.lower() in word_freq:

                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[word.text.lower()]

    best = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    return ' '.join([s.text for s in best])



# Load pre-trained BART summarizer
summarizer = pipeline(task='text-generation', 
                      model="facebook/bart-large-cnn"
                      )

def abstractive_summary(text, min_len=20, max_len=60):
    # Handle very long reviews (BART token limit ~1024)
    text = ' '.join(text.split()[:900])
    
    if len(text.split()) < 30:
        return text  # Too short to summarize
    
    result = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return result[0]['summary_text']