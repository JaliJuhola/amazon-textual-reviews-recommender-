from dataframes.basedf import BaseDf
from dataframes.differencesdf import DifferencesPivot
from dataframes.cosinedf import CosineDF
from dataframes.electronicsdf import ElectronicsDF
import pandas as pd
import time
from reccomender import Reccommender
from reviewModel import ReviewModel

def create_dataframes():
    start = time.time()
    baseDF = BaseDf.create_basedf()
    differences_pivot = DifferencesPivot.save_differences_pivot(baseDF)
    cosine_diffs = CosineDF.save_cosine_differences(differences_pivot)
    end = time.time()
    print("Dataframes created in {seconds} seconds".format(seconds=str(end-start)))

def create_prediction_dataframes():
    start = time.time()
    baseDf = ReviewModel.get_prediction_basedf()
    differences_pivot = DifferencesPivot.save_differences_pivot_predict(baseDf)
    cosine_diffs = CosineDF.save_cosine_differences_predict(differences_pivot)
    end = time.time()
    print("Dataframes created in {seconds} seconds".format(seconds=str(end-start)))


def get_reccomendations(user_id, amount):
    return Reccommender.get_reccomendations(user_id,amount)

def retrain_1_2_ngram_model():
    ReviewModel.retrain_1_2_ngram_model()

def get_prediction_1_2_ngram(reviewText):
    return ReviewModel.get_prediction_1_2_ngram(reviewText)

def retrain_1_3_ngram_model():
    ReviewModel.retrain_1_3_ngram_model()

def get_prediction_1_3_ngram(reviewText):
    return ReviewModel.get_prediction_1_3_ngram(reviewText)

#training_set = ReviewModel.create_trainingset()
#print(training_set)
#print(training_set.shape)
# retrain_1_4_ngram_model()
#retrain_1_3_ngram_model()
# create_dataframes()
#user_id = "A2HD75EMZR8QLN"
#print(get_reccomendations(user_id,3))
#print(BaseDf.get_reviews_by_reviewer_id(user_id))
# retrain_model()
#retrain_1_2_ngram_model()
# BaseDf.get_statistics_about_data()
rev_id = "A00263941WP7WCIL7AKWL"
print(BaseDf.get_reviews_by_reviewer_id(rev_id))
print(Reccommender.get_reccomendations_predict(rev_id, 10, reviews_by_reviewer_id=BaseDf.get_reviews_by_reviewer_id_predict(rev_id), differences_df=DifferencesPivot.get_differences_df_predict()))
print(Reccommender.get_reccomendations_predict(rev_id, 10))
print(get_prediction_1_2_ngram(["good product"]))
