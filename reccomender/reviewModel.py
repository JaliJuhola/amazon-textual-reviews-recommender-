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

class ReviewModel:

    @staticmethod
    def retrain_model():
        # X should be dictionary and y should be label X input y output ???
        # add new value to split
        df = BaseDf.get_basedf()
        df = ReviewModel.add_categorizing(df)
        X_train, X_test, y_train, y_test = ReviewModel.split_test_data(df)
        # Including more stuff     X_train, X_train_1, X_test, y_train, y_test = split_test_data(df)
        print(X_train)
        print(y_train)
        # https://stackoverflow.com/questions/36182502/add-stemming-support-to-countvectorizer-sklearn
        vect = StemmedCountVectorizer(min_df=5, ngram_range=(1,2), analyzer="word", stop_words='english').fit(X_train)
        print("Countvectorizer created")
        X_train_vectorized = vect.transform(X_train)
        print("first part vectorized")
        # sklearn.naive_bayes: Naive Bayes discrete
        model = LogisticRegression()
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
    def get_model():
        return joblib.load('reviews_model.sav') 

    @staticmethod
    def get_prediction(model, review):
        vectorizer = CountVectorizer(vocabulary=pickle.load(open("vocabulary.pkl", "rb")))
        vector = vectorizer.transform(review)
        return model.predict(vector)
