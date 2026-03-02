from sklearn.decomposition import LatentDirichletAllocation


def train_lda_model(dtm, vectorizer, n_topics=8, top_n_words=10, print_output=True):
    """
    Train an LDA model and optionally print top words per topic.

    Parameters:
    ----------
    dtm : sparse matrix
        Document-Term Matrix from CountVectorizer
    vectorizer : fitted CountVectorizer
    n_topics : int
        Number of topics
    top_n_words : int
        Number of top words to display per topic
    print_output : bool
        Whether to print topics

    Returns:
    -------
    lda_model : trained LDA model
    perplexity : float
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
