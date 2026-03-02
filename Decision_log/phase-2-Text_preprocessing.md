# Q)Which tokenizer did you choose (NLTK or spaCy) and why?

selected spaCy for tokenization.

Reasoning:

spaCy provides context-aware tokenization, handling contractions and edge cases more accurately than rule-based tokenizers.

It integrates tokenization, lemmatization, and POS tagging in a single pipeline.

# Q)Did you use stemming or lemmatization for topic modeling? Why?

I have Choosen lemmatization over stemming.

Comparison:
Technique	      Output Example	     
Stemming	     “caring” → “car”	 ----> meaning Changed 
Lemmatization	“caring” → “care”	 ----> preserves Context 


Two text versions were created:

# text_for_topics

  Lowercased

  Stopwords removed

  Lemmatized

  Punctuation removed

# text_for_sentiment

   Minimal cleaning

   Stopwords kept

   No lemmatization

   Punctuation preserved

This separation ensures preprocessing aligns with the downstream modeling objective.