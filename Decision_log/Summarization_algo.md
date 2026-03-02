# Why We Are Using Extractive Word Frequency Algorithm

## 1. Overview
The **Extractive Word Frequency Algorithm** is a simple, unsupervised method for text summarization. It selects sentences from the original text that contain the most frequently occurring significant words.  

Unlike **abstractive summarization**, it does not generate new sentences — it preserves the original text’s context and wording.  

---

## 2. Why This Algorithm?

### Advantages
1. **Simplicity & Efficiency**  
   - Easy to implement using tokenization and word counting.  
   - Low computational cost; works well on small to medium-sized datasets.  

2. **Captures Important Keywords**  
   - Highlights sentences containing **high-frequency significant words**, which usually reflect the core idea of the text.  
   - Avoids stop words and punctuation to focus on meaningful content.  

3. **Preserves Original Sentences**  
   - Extracted sentences are grammatically correct since they are taken verbatim from the text.  
   - Useful in applications where **context accuracy is critical**, such as news summarization or reviews.  

---

## 3. Comparison with Other Algorithms

| Algorithm | What it Captures | Where it Fails | Why Not Chosen Here |
|-----------|-----------------|----------------|-------------------|
| **Luhn / Word Frequency** | High-frequency words and sentences containing them | May miss semantic meaning beyond word counts | ✅ Matches our goal of simple extractive summarization |
| **LexRank / TextRank** | Sentence importance based on similarity to other sentences | Ignores rare but important words; computationally heavier due to graph creation | Overkill for small texts; less interpretable |
| **LSA (Latent Semantic Analysis)** | Latent topics via matrix factorization | Requires more data; complex; may produce less readable sentences | Not ideal for short or domain-specific texts |

---

## 4. What It Captures Well
- **Core keywords and concepts** appearing frequently in the text.  
- **Sentences representing main ideas** without altering meaning.  
- Works well for **structured or semi-structured content**, like product reviews, news articles, or reports.  

---

## 5. Limitations of Other Approaches
- **LexRank / TextRank**: Can overemphasize sentences that are similar to many others, ignoring rare but important details.  
- **LSA**: Focuses on latent semantic structure, which may ignore exact phrasing and produce less readable sentences.  
- **Abstractive methods** (like GPT-based summaries): Require large models, more computation, and can generate inaccurate or hallucinated content.  

---

## 6. Conclusion
The **Extractive Word Frequency Algorithm** provides a **balanced trade-off**: it is **simple, fast, interpretable, and preserves the original context**, making it ideal for summarizing texts like product reviews, news, and reports where **accuracy and clarity** are more important than generating new sentences.  