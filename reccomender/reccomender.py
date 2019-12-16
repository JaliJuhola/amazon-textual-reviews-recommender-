from dataframes.basedf import BaseDf
from dataframes.differencesdf import DifferencesPivot
from dataframes.cosinedf import CosineDF
from functools import reduce
import pandas as pd
import time




class Reccommender:

    @staticmethod
    def get_similar_users(user_id, amount, cosine_diffs):
        similar_users = cosine_diffs[user_id]
        similar_users_list = (similar_users.sort_values(ascending=False).drop(similar_users.index[0])[:amount+1])
        return similar_users_list.loc[lambda x : x.index !=user_id]

    @staticmethod
    def weighted_sums(series):
        return series['difference_to_reviewer_mean'] + series['similarity_score']

    def get_scores_by_asin(similar_user_reviews):
        similar_user_reviews['weighted_score'] = similar_user_reviews['difference_to_reviewer_mean'] * similar_user_reviews['similarity_score']
        similar_user_reviews = similar_user_reviews[['reviewerID', 'asin', 'weighted_score']]
        scores_by_product = similar_user_reviews.groupby(['asin']).sum()
        return scores_by_product

    @staticmethod        
    def get_reccomendations(user_id, amount, cosine_diffs):
        start = time.time()
        reviewed_product_by_user = BaseDf.get_reviews_by_reviewer_id(user_id)['asin'].tolist()
        similar_users = Reccommender.get_similar_users(user_id, amount, cosine_diffs)
        base_df = DifferencesPivot.get_differences_df()
        base_df = base_df[~base_df['asin'].isin(reviewed_product_by_user)]
        similar_user_reviews = base_df[base_df['reviewerID'].isin(similar_users.index.tolist())]
        similar_user_reviews_with_similarity = similar_user_reviews.merge(similar_users, left_on='reviewerID', right_index=True)
        similar_user_reviews_with_similarity.rename(columns={ similar_user_reviews_with_similarity.columns[5]: "similarity_score" }, inplace = True)
        scores_by_asin = Reccommender.get_scores_by_asin(similar_user_reviews_with_similarity)
        end=time.time()
        n_reccommended_products = scores_by_asin.nlargest(amount, 'weighted_score')
        print("reccomendation took {seconds} seconds".format(seconds=(end-start)))
        return n_reccommended_products.reset_index()

    @staticmethod        
    def get_reccomendations_predict(user_id, amount, cosine_diffs, reviews_by_reviewer_id=pd.DataFrame(), differences_df=pd.DataFrame()):
        start = time.time()
        if reviews_by_reviewer_id.empty:
            reviewed_product_by_user = BaseDf.get_reviews_by_reviewer_id(user_id)['asin'].tolist()
        else:
            reviewed_product_by_user = reviews_by_reviewer_id['asin'].tolist()
        similar_users = Reccommender.get_similar_users(user_id, 70, cosine_diffs)
        if differences_df.empty:
            differences_df = DifferencesPivot.get_differences_df()
        differences_df = differences_df[~differences_df['asin'].isin(reviewed_product_by_user)]
        similar_user_reviews = differences_df[differences_df['reviewerID'].isin(similar_users.index.tolist())]
        similar_user_reviews_with_similarity = similar_user_reviews.merge(similar_users, left_on='reviewerID', right_index=True)
        similar_user_reviews_with_similarity.rename(columns={ similar_user_reviews_with_similarity.columns[5]: "similarity_score" }, inplace = True)
        scores_by_asin = Reccommender.get_scores_by_asin(similar_user_reviews_with_similarity)
        end=time.time()
        n_reccommended_products = scores_by_asin.nlargest(amount, 'weighted_score').reset_index()
        print("reccomendation took {seconds} seconds".format(seconds=(end-start)))
        return n_reccommended_products.reset_index()