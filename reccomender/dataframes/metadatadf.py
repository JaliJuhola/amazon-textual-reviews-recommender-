import gzip
import pandas as pd
import matplotlib.pyplot as plt
import re
import json
from basedf import BaseDf

class MetadataDf:

    @staticmethod
    def parse(path):
        g = gzip.open(path, 'r')
        for l in g:
            yield json.loads(l)

    @staticmethod
    def create_metadata_df():
        i = 0
        df = {}
        for d in MetadataDf.parse("./data/meta_Video_Games.json.gz"):
            df[i] = d
            i += 1
        df = pd.DataFrame.from_dict(df,  orient='index')
        df.drop('tech2', axis=1, inplace=True)
        df.drop('similar_item', axis=1, inplace=True)
        df.drop('details', axis=1, inplace=True)
        df.drop('tech1', axis=1, inplace=True)
        df.drop('date', axis=1, inplace=True)
        df.drop('feature', axis=1, inplace=True)
        df.drop('price', axis=1, inplace=True)
        df.drop('also_view', axis=1, inplace=True)
        df.drop('also_buy', axis=1, inplace=True)
        df.drop('main_cat', axis=1, inplace=True)
        df.drop('rank', axis=1, inplace=True)
        df = MetadataDf.preprocessing_cleaning(df)
        #print(df.head())
        df.to_pickle("./data/video_game_reviews_meta")
        return pd.read_pickle("./data/video_game_reviews_meta")

    @staticmethod
    def preprocessing_cleaning(df):
        return df


    @staticmethod
    def get_metadata_df(): 
        return pd.read_pickle("./data/video_game_reviews_meta")

    @staticmethod
    def join_metadata_to_df(df):
        metadata_df = MetadataDf.get_metadata_df()
        return df.merge(metadata_df, on=["asin"], how="left").drop_duplicates(subset="asin")


