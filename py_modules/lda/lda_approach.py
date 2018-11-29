from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import os
import jieba
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
import numpy as np
import lda


def build_word_bags():
    folder = "../../SportNews/after_process"
    corpus = []
    count = 0
    """
    Read all "sports" news and use "jieba" to segment each article into
    a string of words seperated by "\\b" 
    """
    for file in os.listdir(folder):
        try:
            filepath = os.path.join(folder, file)
            f = open(filepath, 'r')
            article = f.read()
            segment_list = jieba.cut(article, cut_all=False)
            splitted = " ".join(segment_list)
            corpus.append(splitted)
            f.close()
        except:
            continue

    """
    Build TF-IDF using CountVectorizer, splitting words by spaces
    """
    # step 1
    vectorizer = CountVectorizer(min_df=1, max_df=1.0, token_pattern='\\b\\w+\\b')
    # step 2
    vectorizer.fit(corpus)
    # step 3
    bag_of_words = vectorizer.get_feature_names()
    # print("Bag of words:")
    # print(bag_of_words)
    # print(len(bag_of_words))
    # step 4
    X = vectorizer.transform(corpus)
    # print("Vectorized corpus:")
    # print(X.toarray())
    # step 5
    return X

if __name__ == "__main__":
    doc_word_max = build_word_bags()
    model = lda.LDA(n_topics=5, n_iter=500, random_state=1)
    print("\n Fit LDA to data set")
    model.fit_transform(doc_word_max)

    print("\n Obtain the words with high probabilities")
    topic_word = model.topic_word_  # model.components_ also works


