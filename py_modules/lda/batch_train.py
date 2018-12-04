from sklearn.feature_extraction.text import CountVectorizer
import lda_approach
from sklearn.decomposition import NMF, LatentDirichletAllocation
import pickle



if __name__ == "__main__":
    topic_nums = [6]

    stop_words_path = "../../stop_words.txt"
    stop_words_f = open(stop_words_path, 'r')
    stop_words_content = stop_words_f.read()

    stop_words_list = stop_words_content.splitlines()
    stop_words_f.close()

    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words=stop_words_list)
    tf = tf_vectorizer.fit_transform(lda_approach.build_word_bags())
    tf_feature_names = tf_vectorizer.get_feature_names()

    for num in topic_nums:
        print ('Training model with {} topics'.format(num))
        model_name = 'lda_{}topics_0.5alpha.pickle'
        lda = LatentDirichletAllocation(n_topics=num,
                                        doc_topic_prior = 0.1,
                                        topic_word_prior = 0.5,
                                        max_iter=30,
                                        n_jobs= -1,
                                        verbose= 1,
                                        evaluate_every= 5,
                                        learning_method='online',
                                        learning_offset=50.,
                                        random_state=0).fit(tf)
        pickle.dump(lda, open(model_name.format(num), 'wb'))