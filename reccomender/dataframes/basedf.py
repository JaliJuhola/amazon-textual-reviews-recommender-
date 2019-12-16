import gzip
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

class BaseDf:

    @staticmethod
    def parse(path):
        g = gzip.open(path, 'rb')
        for l in g:
            yield eval(l)

    @staticmethod
    def create_basedf():
        i = 0
        df = {}
        for d in BaseDf.parse("./data/reviews_Video_Games.json.gz"):
            df[i] = d
            i += 1
        df = pd.DataFrame.from_dict(df,  orient='index')
        df.drop('unixReviewTime', axis=1, inplace=True)
        df.drop('reviewTime', axis=1, inplace=True)
        df.drop('helpful', axis=1, inplace=True)
        df.drop('reviewerName', axis=1, inplace=True)
        df.overall = df.overall.astype('float')
        df = BaseDf.preprocessing_cleaning(df)
        df.to_pickle("./data/video_game_reviews_base")
        return pd.read_pickle("./data/video_game_reviews_base")

    @staticmethod
    def preprocessing_cleaning(df):
        # Clean links
        df['summary'] = df['summary'].apply(lambda x: re.split(r'http\S+|www.\S+', str(x))[0])
        df['reviewText'] = df['reviewText'].apply(lambda x: re.split(r'http\S+|www.\S+', str(x))[0])
        # clean non text related special characters
        df['summary'] = df['summary'].str.replace(r"[^a-zA-Z0-9 .]+", "").str.strip()
        df['reviewText'] = df['reviewText'].str.replace(r"[^a-zA-Z0-9 .]+", "").str.strip()
        return df


    @staticmethod
    def get_basedf(): 
        return pd.read_pickle("./data/video_game_reviews_base")

    @staticmethod
    def get_reviews_by_reviewer_id(reviewer_id):
        base_df = BaseDf.get_basedf()
        return base_df.query('reviewerID == "{reviewer_id}"'.format(reviewer_id=reviewer_id))

    @staticmethod
    def get_reviews_by_reviewer_id_predict(reviewer_id):
        base_df = pd.read_pickle("./data/video_game_reviews_base_predict")
        return base_df.query('reviewerID == "{reviewer_id}"'.format(reviewer_id=reviewer_id))

    @staticmethod
    def get_reviews_by_product_asin(asin_code, base_df):    
        return base_df.query('asin == "{asin_code}"'.format(asin_code=asin_code))
    @staticmethod
    def get_statistics_about_data():
        df = BaseDf.get_basedf()
        # Crosstab split according to overall score
        # pd.crosstab(index = df['overall'], columns="Total count")
        # Empty reviews
        #asd = df[df.reviewText.apply(lambda x: len(x)<30)]
        #asd2 = df.reviewText.apply(lambda x: len(x))
        #ct1 = pd.crosstab(index =df['overall'], columns="Total count")
        df['Positively_Rated'] = np.where(df['overall']>3, 1, 0)
        print(df['Positively_Rated'].value_counts())
        ct = pd.crosstab(index = df['Positively_Rated'], columns="Total count")
        ct.plot(kind="bar")
        plt.show()
        #ct1.plot()
        #df = df.head()
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        #print(df[df['Positively_Rated'] == 0].iloc[0]['reviewText'])

