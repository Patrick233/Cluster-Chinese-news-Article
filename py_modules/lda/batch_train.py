from sklearn.feature_extraction.text import CountVectorizer
import lda_approach
from sklearn.decomposition import NMF, LatentDirichletAllocation
import pickle

if __name__ == "__main__":
    topic_nums = [100, 200]

    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2)
    tf = tf_vectorizer.fit_transform(lda_approach.build_word_bags())
    tf_feature_names = tf_vectorizer.get_feature_names()

    for num in topic_nums:
        print ('Training model with {} topics'.format(num))
        model_name = 'lda_{}topics.pickle'
        lda = LatentDirichletAllocation(n_topics=num, max_iter=30,
                                        n_jobs= -1,
                                        verbose= 1,
                                        evaluate_every= 5,
                                        learning_method='online',
                                        learning_offset=50.,
                                        random_state=0).fit(tf)
        pickle.dump(lda, open(model_name.format(num), 'wb'))