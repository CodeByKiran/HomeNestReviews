Phase 3 – Topic Modeling Decision Log
# 1) What number of topics did you settle on and why? Show the perplexity plot.

We trained multiple LDA models with the number of topics ranging from 4 to 15 and evaluated them using perplexity (lower is better).

Observed trend:

  Perplexity consistently decreased as the number of topics increased.

  The reduction was significant between 4 and 10 topics.

  After 10–12 topics, the improvement began to show diminishing returns.

  Although 15 topics produced the lowest perplexity, interpretability declined beyond 10–12 topics.

  There was no sharp “elbow,” so the decision required balancing:

We selected 10 topics because:

It provided substantially lower perplexity than 8 topics.

Topics were still coherent and interpretable.

Topic fragmentation and overlap became noticeable at 12 topics.

It offered a good balance between granularity and clarity.

Thus, 10 topics achieved the best trade-off between model fit and interpretability.

# 2) Are any topics overlapping or hard to interpret? What would you do differently?

Yes, some overlap was observed:

Delivery-related phrases and “worked immediately” language appeared in similar clusters.

General praise terms such as “great product” and “highly recommend” appeared across multiple topics.

Some topics were dominated by product or brand names rather than customer concerns.

This indicates that:

The model sometimes grouped reviews by product identity rather than underlying themes.

Generic praise language diluted more issue-specific themes.

If improving further, we would:

Remove product names prior to modeling to avoid SKU-based clustering.

Increase min_df to remove rare, product-specific terms.

Filter generic praise phrases (e.g., “great product”, “highly recommend”).

Potentially refine stopword handling for overly common sentiment terms.

These adjustments would likely produce more issue-driven and business-focused topics.

# 3) Which topic is most valuable to HomeNest and why?

The most strategically valuable topics are:

Delivery & Immediate Functionality

This topic captures:

Shipping speed

Packaging condition

Whether products worked upon arrival

This is highly actionable because it directly impacts logistics performance, operational costs, and customer satisfaction.

Product Quality / Build Issues

This topic reflects:

Durability

Materials

Defects

Structural concerns

This is critical because it affects:

Return rates

Warranty costs

Brand reputation

Long-term customer trust

Both themes provide clear, actionable insights for operational and product improvement decisions.

# 4) What are the limitations of LDA?

LDA has several important limitations:

Ignores word order (Bag-of-Words assumption)
It does not understand sequence.
For example, “not good” and “good” are treated independently unless bigrams are explicitly included.

No contextual understanding
It cannot detect sarcasm, nuance, or intent.

Sensitive to preprocessing choices
Lemmatization, stopword removal, and n-gram settings significantly affect results.

Requires manual topic labeling
Human interpretation is necessary to assign meaningful labels.

Perplexity does not measure interpretability
A lower perplexity score does not guarantee clearer or more useful topics.

Topics can overlap
Because documents are mixtures of topics, boundaries are not always clean.

Despite these limitations, LDA is effective for high-level theme discovery and exploratory analysis in unlabeled datasets.