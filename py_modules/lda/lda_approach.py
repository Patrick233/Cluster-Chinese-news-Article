from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import os
import jieba
from sklearn.decomposition import NMF, LatentDirichletAllocation


def build_word_bags():
    folder = "../../news/after_process"
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

    return corpus

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print "Topic %d:" % (topic_idx)
        print " ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]])

if __name__ == "__main__":
    no_top_words = 10
    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2)
    tf = tf_vectorizer.fit_transform(build_word_bags())
    tf_feature_names = tf_vectorizer.get_feature_names()

    lda = LatentDirichletAllocation(n_topics=no_top_words, max_iter=50, learning_method='online', learning_offset=50.,
                                    random_state=0).fit(tf)

    print("\n Fit LDA to data set")
    display_topics(lda, tf_feature_names, no_top_words)




