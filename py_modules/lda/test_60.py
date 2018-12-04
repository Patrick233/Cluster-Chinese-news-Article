from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import os
import jieba
from sklearn.decomposition import NMF, LatentDirichletAllocation

def build_word_bags():
    folder = "./test_60"
    corpus = []
    count = 0
    """
    Read all "sports" news and use "jieba" to segment each article into
    a string of words seperated by "\\b" 
    """
    for file in sorted(os.listdir(folder)):
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

    return corpus

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print "Topic %d:" % (topic_idx)
        print " ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]])

def display_docs(doc_topic, doc_num):
    # print(doc_topic, type(doc_topic))
    for i in range(doc_num):
        print("{} (top topic: {})".format(i, np.argsort(doc_topic[i])[:-2:-1]))


if __name__ == "__main__":
    topic_nums = [6]

    stop_words_path = "../../stop_words.txt"
    stop_words_f = open(stop_words_path, 'r')
    stop_words_content = stop_words_f.read()

    stop_words_list = stop_words_content.splitlines()
    stop_words_f.close()

    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words=stop_words_list)
    tf = tf_vectorizer.fit_transform(build_word_bags())
    tf_feature_names = tf_vectorizer.get_feature_names()

    for num in topic_nums:
        print ('Training model with {} topics'.format(num))
        model_name = 'lda_{}topics_0.5alpha.pickle'
        lda = LatentDirichletAllocation(n_components=num,
                                        max_iter=100,
                                        n_jobs= -1,
                                        verbose= 1,
                                        evaluate_every= 5,
                                        learning_method='online',
                                        learning_offset=50.,
                                        random_state=0).fit(tf)

        print("\n Fit LDA to data set")
        display_topics(lda, tf_feature_names, 10)
        display_docs(lda.fit_transform(tf[:]), 60)

