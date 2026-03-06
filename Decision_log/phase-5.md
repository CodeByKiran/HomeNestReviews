Phase 5 – Decision Log
# 1. For short reviews (under 30 words), is summarization even useful? What did you do with them?

For very short reviews (less than 30 words), summarization is generally not useful because the review is already concise and contains minimal information.

Example review:

"Great product. Works perfectly."

A summarizer might produce:

"Great product."

This does not significantly reduce the length or improve clarity.

Decision

Reviews with less than 30 words were not summarized.
Instead, the original review text was used as the summary.

Reasoning

Avoid unnecessary computation

Prevent loss of important information

Improve overall pipeline efficiency

Implementation Logic
if len(review.split()) < 30:
    summary = review
else:
    summary = summarizer(review)


# 2. Did the abstractive model ever produce a summary that was factually wrong or added information not in the review?

Yes. Abstractive models sometimes hallucinate, meaning they generate information that is not present in the original review.

Example

Original Review

"The sofa looks good but delivery was delayed by 3 days."

Abstractive Summary

"The sofa looks great but delivery was late due to shipping issues."

Problem

The original review did not mention shipping issues, but the model introduced additional information.

This is a known limitation of abstractive models such as BART or T5.

Impact

Can introduce misleading insights

Reduces trust in automated summaries

Risky for customer feedback analytics



# 3. Which approach would you recommend to HomeNest for a production system and why?

For a production system, Extractive Summarization is recommended.

Recommended Approach: Extractive Summarization
Accuracy

Extractive summarization selects sentences directly from the original review, ensuring no additional information is introduced.

Speed

Extractive methods such as TextRank or TF-IDF scoring are significantly faster than transformer-based abstractive models.

Cost

Abstractive models require:

High compute resources

Longer inference time

Higher infrastructure cost

Extractive approaches can run efficiently on standard CPU systems.

Reliability

Because the sentences are taken directly from the original review, hallucination risks are eliminated.

Final Recommendation

Use:

Extractive summarization as the default method

Abstractive summarization only for very long reviews (>100 words) if deeper compression is required.

# 4. How would you evaluate summarization quality at scale without reading all summaries manually?

Manually evaluating thousands of summaries is not scalable. Instead, automated evaluation metrics can be used.

One commonly used metric is ROUGE (Recall-Oriented Understudy for Gisting Evaluation).

ROUGE measures the overlap between generated summaries and reference summaries.

Common ROUGE Metrics
ROUGE-1

Measures unigram (word) overlap between the generated summary and the reference summary.

ROUGE-2

Measures bigram overlap, capturing phrase-level similarity.

ROUGE-L

Measures the Longest Common Subsequence (LCS) between summaries, capturing sentence-level structure similarity.

Example

Reference Summary

"Delivery was late but the sofa quality is good."

Generated Summary

"The sofa quality is good but delivery was delayed."

ROUGE calculates the degree of similarity between the two summaries.

Higher ROUGE scores indicate better summarization quality.




# Final Summary

Short reviews	            ---  Skip summarization and keep original review
Abstractive issues          ---	 Possible hallucination
Production recommendation	---  Extractive summarization
Evaluation method           ---	 ROUGE metrics