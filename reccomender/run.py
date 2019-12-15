from dataframes.basedf import BaseDf
from dataframes.differencesdf import DifferencesPivot
from dataframes.cosinedf import CosineDF
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

def retrain_model():
    ReviewModel.retrain_model()

# create_dataframes()
#user_id = "A2HD75EMZR8QLN"
#print(get_reccomendations(user_id,3))
#print(BaseDf.get_reviews_by_reviewer_id(user_id))
retrain_model()
