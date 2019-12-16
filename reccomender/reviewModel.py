import pandas as pd
import numpy as np
import gzip
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.metrics import roc_curve, roc_auc_score, auc
from sklearn.externals import joblib
import pickle
from dataframes.basedf import BaseDf
from dataframes.electronicsdf import ElectronicsDF
from StemmedCountVectorizer import StemmedCountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
import time

class ReviewModel:

    @staticmethod
    def create_trainingset():
        #electronics_df = ReviewModel.add_categorizing(ElectronicsDF.get_electronicsdf())
        videogame_df = ReviewModel.add_categorizing(BaseDf.get_basedf())
        sorted_videogame_df = videogame_df.sort_values(by=['Positively_Rated'])
        sorted_videogame_df.drop(sorted_videogame_df.tail(118198).index, inplace=True)
        #frames = [electronics_df, videogame_df]
        #print(pd.concat(frames).shape)
        return sorted_videogame_df

    @staticmethod
    def save_prediction_basedf():
        df = BaseDf.get_basedf()
        df['predicted_score'] = ReviewModel.get_prediction_1_2_ngram(df['reviewText'])
        df.to_pickle("./data/video_game_reviews_base_predict")
        return df
        
    @staticmethod
    def get_prediction_basedf(): 
        return pd.read_pickle("./data/video_game_reviews_base_predict")

    @staticmethod
    def retrain_1_2_ngram_model():
        t1 = time.time()
        # X should be dictionary and y should be label X input y output ???
        # add new value to split
        df = ReviewModel.create_trainingset()
        X_train, X_test, y_train, y_test = ReviewModel.split_test_data(df)
        # Including more stuff     X_train, X_train_1, X_test, y_train, y_test = split_test_data(df)
        # https://stackoverflow.com/questions/36182502/add-stemming-support-to-countvectorizer-sklearn
        vect = StemmedCountVectorizer(min_df=6, ngram_range=(1,2), analyzer="word", stop_words='english', max_df=0.4).fit(X_train)
        print("Countvectorizer created")
        X_train_vectorized = vect.transform(X_train)
        print("first part vectorized")
        # sklearn.naive_bayes: Naive Bayes discrete
        model = MultinomialNB()
        print("Model created")
        model.fit(X_train_vectorized, y_train)
        print("model fitted")
        predictions = model.predict(vect.transform(X_test))
        print("Testing with first dataset")
        false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, predictions)
        roc_auc = auc(false_positive_rate, true_positive_rate)
        print('AUC score: ', roc_auc_score(y_test, predictions))
        joblib.dump(model, 'reviews_model_video_game.sav')
        pickle.dump(vect.vocabulary_,open("vocabulary_video_game.pkl","wb"))
        t2 = time.time()
        print("1_1_ngram_model_took {seconds}".format(seconds=str(t2-t1)))
        return model

    @staticmethod
    def retrain_1_3_ngram_model():
        t1 = time.time()
        # X should be dictionary and y should be label X input y output ???
        # add new value to split
        df = ReviewModel.create_trainingset()
        df = ReviewModel.add_categorizing(df)
        X_train, X_test, y_train, y_test = ReviewModel.split_test_data(df)
        # Including more stuff     X_train, X_train_1, X_test, y_train, y_test = split_test_data(df)
        # https://stackoverflow.com/questions/36182502/add-stemming-support-to-countvectorizer-sklearn
        vect = StemmedCountVectorizer(min_df=5, ngram_range=(1,3), analyzer="word", stop_words='english').fit(X_train)
        print("Countvectorizer created")
        X_train_vectorized = vect.transform(X_train)
        print("first part vectorized")
        # sklearn.naive_bayes: Naive Bayes discrete
        model = MultinomialNB()
        print("Model created")
        model.fit(X_train_vectorized, y_train)
        print("model fitted")
        predictions = model.predict(vect.transform(X_test))
        print("Testing with first dataset")
        false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, predictions)
        roc_auc = auc(false_positive_rate, true_positive_rate)
        print('AUC score: ', roc_auc_score(y_test, predictions))
        joblib.dump(model, 'reviews_model_1_3.sav')
        pickle.dump(vect.vocabulary_,open("vocabulary_1_3.pkl","wb"))
        t2 = time.time()
        print("1_3_ngram_model_took {seconds}".format(seconds=str(t2-t1)))
        return model

    @staticmethod
    def split_test_data(df):
        X_train, X_test, y_train, y_test = train_test_split(df['reviewText'], df['Positively_Rated'], random_state=0)
        # X_train, X_test, y_train, y_test = train_test_split(df['reviewText'], df['summary'] ,df['Positively_Rated'], random_state=0)
        return X_train, X_test, y_train, y_test

    @staticmethod
    def add_categorizing(df):
        # df.dropna(inplace=True)f
        # df = df[df['overall']!= 3]
        df['Positively_Rated'] = np.where(df['overall']>3, 1, 0)
        return df

    @staticmethod
    def get_1_2_ngram_model():
        return joblib.load('reviews_model_video_game.sav')

    @staticmethod
    def get_1_3_ngram_model():
        return joblib.load('reviews_model_1_3.sav') 
    
    @staticmethod
    def get_prediction_1_2_ngram(review):
        model = ReviewModel.get_1_2_ngram_model()
        vectorizer = StemmedCountVectorizer(vocabulary=pickle.load(open("vocabulary_video_game.pkl", "rb")), min_df=5, ngram_range=(1,2), analyzer="word", stop_words='english')
        feature_names = np.array(vectorizer.get_feature_names())
        sorted_coef_index = model.coef_[0].argsort()
        vector = vectorizer.transform(review)
        return model.predict(vector)

    @staticmethod
    def get_prediction_1_3_ngram(review):
        model = ReviewModel.get_1_3_ngram_model()
        vectorizer = StemmedCountVectorizer(vocabulary=pickle.load(open("vocabulary_1_3.pkl", "rb")), min_df=5, ngram_range=(1,3), analyzer="word", stop_words='english')
        feature_names = np.array(vectorizer.get_feature_names())
        sorted_coef_index = model.coef_[0].argsort()
        print('Smallest Coefs: \n{}\n'.format(feature_names[sorted_coef_index[:10]]))
        print('Largest Coefs: \n{}\n'.format(feature_names[sorted_coef_index[:-11:-1]]))
        vector = vectorizer.transform(review)
        return model.predict(vector)