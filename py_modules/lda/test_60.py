from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import os
import jieba
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.cluster import KMeans

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


def get_class(x):
    """
    x: index
    """
    # Example
    distribution = [99, 198, 297, 396, 495]
    x_class = 0
    for i in range(len(distribution)):
        if x > distribution[i]:
            x_class += 1
    return x_class


def kmeans_purity(labels):
    """
    labels: (n samples,)
    """
    dic = {}
    # Number of clusters
    n = 6
    for i in range(n):
        dic[i] = {}
    for i in range(len(labels)):
        cluster = labels[i]
        i_class = get_class(i)
        old_count = dic.get(cluster).get(i_class, 0)
        dic[cluster][i_class] = old_count + 1
    percent = {}
    totals = {}
    for k in dic:
        _max = 0
        total = 0.0
        for c in dic[k]:
            total += dic[k][c]
            _max = max(_max, dic[k][c])
        if total == 0:
            percent[k] = -1
        else:
            percent[k] = (_max + 0.0) / total
        print(percent[k])
        totals[k] = total
    print (dic)
    print (percent)
    print (totals)
    return percent, totals


def kmeans(data):
    if data.shape[1] == 6:
        assignment = np.arange(data.shape[0])
        for i in range(data.shape[0]):
            max_j = 0
            for j in range(data.shape[1]):
                if data[i][j] > data[i][max_j]:
                    max_j = j
            assignment[i] = max_j
        kmeans_purity(assignment)

    else:
        cluster = KMeans(n_clusters=6, random_state=34312, n_init=5, n_jobs=-1).fit(data)
        print (cluster.labels_.shape)
        print cluster.labels_
        kmeans_purity(cluster.labels_)


if __name__ == "__main__":
    topic_nums = [10]

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
        data = lda.transform(tf[:])
        kmeans(data)
        # display_topics(lda, tf_feature_names, 10)
        # display_docs(lda.transform(tf[:]), 594)

