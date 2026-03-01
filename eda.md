# Exploratory Data Analysis (EDA) Report

## 1. Introduction

This report presents the exploratory data analysis performed on a customer reviews dataset containing 5,000 records.  
The objective of this analysis is to understand the dataset structure, data quality, rating distribution, textual characteristics, and temporal trends before designing the NLP pipeline.

A thorough EDA ensures that modeling decisions are data-driven rather than assumption-driven.

---

## 2. Dataset Overview

### 2.1 Dataset Size

- Total Records: **5,000**
- Total Columns: **7**
- Memory Usage: ~239 KB

### 2.2 Column Summary

| Column Name         | Data Type | Description |
|--------------------|-----------|-------------|
| review_id          | int64     | Unique identifier for each review |
| product_category   | string    | Product category |
| product_name       | string    | Product name |
| review_text        | string    | Customer review text |
| star_rating        | int64     | Rating provided (1–5) |
| review_date        | string    | Date of review (needs datetime conversion) |
| verified_purchase  | bool      | Indicates verified purchase |

### 2.3 Statistical Summary (Numeric Columns)

- Mean Rating: **3.89**
- Standard Deviation: **1.33**
- Median Rating: **4**
- Minimum Rating: **1**
- Maximum Rating: **5**

The average rating is close to 4, indicating generally positive feedback across the dataset.

---

## 3. Data Quality Assessment

### 3.1 Missing Values

All columns contain 5,000 non-null values.

✔ No missing values were detected.

---

### 3.2 Duplicate Review IDs

No duplicate `review_id` values were found.

✔ Each review is uniquely identified.

---

### 3.3 Data Type Observations

- `review_date` is stored as a string and should be converted to datetime format for time-series analysis.
- All other columns have appropriate data types.

Overall, the dataset is structurally clean.

---

## 4. Target Variable Analysis (Star Ratings)

### 4.1 Rating Distribution

| Rating | Count | Percentage |
|--------|--------|------------|
| 5 | 2319 | 46.38% |
| 4 | 1202 | 24.04% |
| 3 | 615 | 12.30% |
| 2 | 352 | 7.04% |
| 1 | 512 | 10.24% |

### 4.2 Class Imbalance

Imbalance Ratio (max class / min class):

2319 / 352 ≈ **6.59**

Since the imbalance ratio exceeds 5, the dataset is moderately imbalanced.

### 4.3 Observations

- Nearly half of the dataset consists of 5-star reviews.
- Positive reviews (4 and 5 stars) dominate.
- 2-star reviews are the least represented class.
- The mean rating of 3.89 confirms a positive skew.

### 4.4 Modeling Implications

- A sentiment model may become biased toward predicting positive sentiment.
- Accuracy alone would not be a reliable metric.
- Recommended strategies:
  - Use Macro F1-score
  - Apply class weighting
  - Use stratified train-test splits
  - Consider oversampling minority classes

---

## 5. Text Analysis

### 5.1 Review Length Analysis

Two features were derived:

- `review_length_char`
- `review_length_word`

Average review length was computed per product category.

Observations:

- Review length varies across product categories.
- Some categories contain more descriptive reviews.
- Longer reviews may benefit summarization models.
- Very short reviews may lack sufficient context for advanced NLP tasks.

Review length variability impacts:
- Token limits in transformer models
- Training cost
- Summarization effectiveness

---

### 5.2 Most Frequent Words (Before Cleaning)

Analysis of the top 10 and top 50 most frequent words revealed:

- Stopwords dominate the frequency list.
- Case-sensitive duplicates exist.
- HTML tags are present.
- Punctuation tokens appear as separate tokens.
- Numeric tokens are included.
- Product names frequently occur.

### Interpretation

This indicates that the raw text contains substantial noise.

Preprocessing steps required:

- Lowercasing
- Stopword removal
- HTML tag removal
- Punctuation cleaning
- Numeric filtering
- Case normalization

Without cleaning, models may learn irrelevant patterns and reduce generalization performance.

---

## 6. Temporal Analysis

### 6.1 Monthly Review Distribution

- Average reviews per month: **208.33**
- Standard Deviation: **13.42**
- Coefficient of Variation (CV): < 0.1

### 6.2 Observations

- Monthly review volume remains relatively stable.
- No strong seasonal spikes observed.
- No major surges during specific months.
- Low coefficient of variation indicates consistent activity.

### 6.3 Implications

- No significant seasonality detected.
- Time-based modeling may not be essential.
- Low risk of temporal concept drift.

---

## 7. Key Findings

1. The dataset is clean with no missing values or duplicate IDs.
2. The rating distribution is positively skewed.
3. The dataset is moderately imbalanced.
4. Text data contains noise requiring preprocessing.
5. Review length varies across categories.
6. Review volume remains stable over time.

---

## 8. Implications for NLP Pipeline

Based on EDA findings, the following steps are required before modeling:

### Data Preparation
- Convert `review_date` to datetime
- Normalize text to lowercase
- Remove HTML tags
- Remove punctuation
- Remove numeric tokens
- Remove stopwords
- Handle case duplicates

### Modeling Considerations
- Use stratified splitting
- Evaluate with Macro F1-score
- Apply class weighting
- Consider excluding extremely short reviews for summarization tasks

---

## Conclusion

The dataset is structurally clean but moderately imbalanced and textually noisy.  
Proper preprocessing and evaluation strategies are necessary to ensure robust sentiment and NLP model performance.

This EDA provides a strong foundation for building the next phase of the NLP pipeline.