from sklearn.feature_extraction.text import CountVectorizer
import lda_approach
from sklearn.decomposition import NMF, LatentDirichletAllocation
import pickle
import numpy as np
import os
from sklearn.cluster import KMeans

stop_words_path = "../stop_words.txt"
stop_words_f = open(stop_words_path, 'r')
stop_words_content = stop_words_f.read()

stop_words_list = stop_words_content.splitlines()
stop_words_f.close()

tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words=stop_words_list)
tf = tf_vectorizer.fit_transform(lda_approach.build_word_bags())
tf_feature_names = tf_vectorizer.get_feature_names()


def get_class(x):
    """
    x: index
    """
    # Example
    distribution = [1882, 3380, 5324, 6946, 8786]
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
        print percent[k]
        totals[k] = total
    print (dic)
    # print (percent)
    print (totals)
    return percent, totals


def load_models(dir_name):
    for file_name in os.listdir(dir_name):
        print ("Evaluating model {}".format(file_name))
        if file_name.find('.pickle') != -1:
            print ("Loading lda model {}".format(file_name))
            lda = pickle.load(open("{}/{}".format(dir_name, file_name), 'rb'))
            lda_approach.display_topics(lda, tf_feature_names, 10)
            data = lda.transform(tf[:])
            print (data.shape)
            # print (data[-5:])
            print (np.sum(data[-1:]))
            kmeans(data)


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
        kmeans_purity(cluster.labels_)


if __name__ == "__main__":
    dir_name = './'
    load_models(dir_name)
