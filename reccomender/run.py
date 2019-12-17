from dataframes.basedf import BaseDf
from dataframes.differencesdf import DifferencesPivot
from dataframes.cosinedf import CosineDF
from dataframes.electronicsdf import ElectronicsDF
import pandas as pd
import time
from reccomender import Reccommender
from reviewModel import ReviewModel
from dataframes.metadatadf import MetadataDf

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
    MetadataDf.create_metadata_df()
    end = time.time()
    print("Dataframes created in {seconds} seconds".format(seconds=str(end-start)))


def get_reccomendations(user_id, amount, cosine_differences):
    reccommendations_df = Reccommender.get_reccomendations_predict(user_id,amount,cosine_differences)
    with_metadata = MetadataDf.join_metadata_to_df(reccommendations_df)
    with_metadata['reviewerID'] = user_id
    return with_metadata.to_json(orient='records')

def get_reccomendations_predict(user_id, amount, cosine_differences, reviews_by_reviewer_id, differences_df):
    reccommendations_df = Reccommender.get_reccomendations_predict(user_id,amount,cosine_differences, reviews_by_reviewer_id=reviews_by_reviewer_id, differences_df=differences_df)
    with_metadata = MetadataDf.join_metadata_to_df(reccommendations_df)
    with_metadata['reviewerID'] = user_id
    return with_metadata.to_json(orient='records')

def retrain_1_2_ngram_model():
    ReviewModel.retrain_1_2_ngram_model()

def get_prediction_1_2_ngram(reviewText):
    return ReviewModel.get_prediction_1_2_ngram(reviewText)

def retrain_1_3_ngram_model():
    ReviewModel.retrain_1_3_ngram_model()

def get_prediction_1_3_ngram(reviewText):
    return ReviewModel.get_prediction_1_3_ngram(reviewText)

def get_reviews_by_reviewer_id(user_id):
    return MetadataDf.join_metadata_to_df(BaseDf.get_reviews_by_reviewer_id(user_id)).to_json(orient='records')
