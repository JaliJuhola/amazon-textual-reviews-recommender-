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
    #differences_pivot = DifferencesPivot.save_differences_pivot(baseDF)
    #cosine_diffs = CosineDF.save_cosine_differences(differences_pivot)
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
# retrain_1_4_ngram_model()
print(get_prediction_1_2_ngram(["When this game was first announced I believe it was going to be a good Assassin's Creed game and when I got it at the midnight launch I played it for 4 days and it was good but the news like IGN thought it was a bad game because of the glitches and the software update to fix the glitches was too much to handle and some Assassin's Creed fans thought it was bad too. After buying Assassin's Creed Unity again but this time on PS4, I thought it was well made game with a bigger map, new weapons, and new people to relate to. I personally didn't have any glitch problems with the game when it first came out. So me personally Assassin's Creed Unity is a good game."]))