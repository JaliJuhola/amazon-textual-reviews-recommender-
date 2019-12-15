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
from StemmedCountVectorizer import StemmedCountVectorizer
from sklearn.naive_bayes import MultinomialNB

class ReviewModel:

    @staticmethod
    def retrain_1_1_ngram_model():
        # X should be dictionary and y should be label X input y output ???
        # add new value to split
        df = BaseDf.get_basedf()
        df = ReviewModel.add_categorizing(df)
        X_train, X_test, y_train, y_test = ReviewModel.split_test_data(df)
        # Including more stuff     X_train, X_train_1, X_test, y_train, y_test = split_test_data(df)
        # https://stackoverflow.com/questions/36182502/add-stemming-support-to-countvectorizer-sklearn
        vect = StemmedCountVectorizer(min_df=5, ngram_range=(1,1), analyzer="word", stop_words='english').fit(X_train)
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
        joblib.dump(model, 'reviews_model.sav')
        pickle.dump(vect.vocabulary_,open("vocabulary.pkl","wb"))
        return model

    @staticmethod
    def retrain_1_4_ngram_model():
        # X should be dictionary and y should be label X input y output ???
        # add new value to split
        df = BaseDf.get_basedf()
        df = ReviewModel.add_categorizing(df)
        X_train, X_test, y_train, y_test = ReviewModel.split_test_data(df)
        # Including more stuff     X_train, X_train_1, X_test, y_train, y_test = split_test_data(df)
        # https://stackoverflow.com/questions/36182502/add-stemming-support-to-countvectorizer-sklearn
        vect = StemmedCountVectorizer(min_df=5, ngram_range=(1,4), analyzer="word", stop_words='english').fit(X_train)
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
        joblib.dump(model, 'reviews_model_1_4.sav')
        pickle.dump(vect.vocabulary_,open("vocabulary_1_4.pkl","wb"))
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
    def get_1_1_ngram_model():
        return joblib.load('reviews_model.sav')

    def get_1_4_ngram_model():
        return joblib.load('reviews_model_1_4.sav') 

    @staticmethod
    def get_prediction_1_1_ngram(review):
        model = ReviewModel.get_1_1_ngram_model()
        vectorizer = StemmedCountVectorizer(vocabulary=pickle.load(open("vocabulary.pkl", "rb")), min_df=5, ngram_range=(1,1), analyzer="word", stop_words='english')
        feature_names = np.array(vectorizer.get_feature_names())
        sorted_coef_index = model.coef_[0].argsort()
        print('Smallest Coefs: \n{}\n'.format(feature_names[sorted_coef_index[:10]]))
        print('Largest Coefs: \n{}\n'.format(feature_names[sorted_coef_index[:-11:-1]]))
        vector = vectorizer.transform(review)
        return model.predict(vector)

    @staticmethod
    def get_prediction_1_4_ngram(review):
        model = ReviewModel.get_1_4_ngram_model()
        vectorizer = StemmedCountVectorizer(vocabulary=pickle.load(open("vocabulary_1_4.pkl", "rb")), min_df=5, ngram_range=(1,4), analyzer="word", stop_words='english')
        feature_names = np.array(vectorizer.get_feature_names())
        sorted_coef_index = model.coef_[0].argsort()
        print('Smallest Coefs: \n{}\n'.format(feature_names[sorted_coef_index[:10]]))
        print('Largest Coefs: \n{}\n'.format(feature_names[sorted_coef_index[:-11:-1]]))
        vector = vectorizer.transform(review)
        return model.predict(vector)