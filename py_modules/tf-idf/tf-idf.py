from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import os
import jieba



def buildTFIDF():
    folder = "../../news/sports"
    corpus = []
    count = 0
    """
    Read all "sports" news and use "jieba" to segment each article into
    a string of words seperated by "\\b" 
    """
    for file in os.listdir(folder):
        filepath = os.path.join(folder, file)
        f = open(filepath, 'r')
        article = f.read()
        segment_list = jieba.cut(article, cut_all=False)
        splitted = " ".join(segment_list)
        corpus.append(splitted)
        f.close()

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
    # print("index of `的` is : {}".format(vectorizer.vocabulary_.get('的')))
    # step 1
    tfidf_transformer = TfidfTransformer()
    # step 2
    tfidf_transformer.fit(X.toarray())
    # step 3
    # for idx, word in enumerate(vectorizer.get_feature_names()):
    #     print("{}\t{}".format(word, tfidf_transformer.idf_[idx]))
    # step 4
    tfidf = tfidf_transformer.transform(X)
    ndarray = tfidf.toarray()
    print(ndarray)
    print(ndarray.shape)

if __name__ == "__main__":
    buildTFIDF()