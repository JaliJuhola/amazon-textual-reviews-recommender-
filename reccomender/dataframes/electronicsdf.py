import gzip
import pandas as pd
import matplotlib.pyplot as plt
import re

class ElectronicsDF:

    @staticmethod
    def parse(path):
        g = gzip.open(path, 'rb')
        for l in g:
            yield eval(l)

    @staticmethod
    def create_electronicsdf():
        i = 0
        df = {}
        for d in ElectronicsDF.parse("reccomender/data/reviews_Electronics_5.json.gz"):
            df[i] = d
            i += 1
        df = pd.DataFrame.from_dict(df,  orient='index')
        df.drop('unixReviewTime', axis=1, inplace=True)
        df.drop('reviewTime', axis=1, inplace=True)
        df.drop('helpful', axis=1, inplace=True)
        df.drop('reviewerName', axis=1, inplace=True)
        df.overall = df.overall.astype('float')
        df = ElectronicsDF.preprocessing_cleaning(df)
        df.to_pickle("reccomender/data/electronics_reviews_base")
        return pd.read_pickle("reccomender/data/electronics_reviews_base")

    @staticmethod
    def preprocessing_cleaning(df):
        # Clean links
        df['reviewText'] = df['reviewText'].str.replace(r"[^a-zA-Z0-9 .]+", "").str.strip()
        df['summary'] = df['summary'].str.replace(r'http\S+|www.\S+', "").str.strip()
        # clean non text related special characters
        df['summary'] = df['summary'].str.replace(r"[^a-zA-Z0-9 .]+", "").str.strip()
        df['reviewText'] = df['reviewText'].str.replace(r"[^a-zA-Z0-9 .]+", "").str.strip()
        return df

    @staticmethod
    def get_electronicsdf(): 
        return pd.read_pickle("reccomender/data/electronics_reviews_base")

    @staticmethod
    def get_reviews_by_reviewer_id(reviewer_id):
        base_df = ElectronicsDF.create_electronicsdf()
        return base_df.query('reviewerID == "{reviewer_id}"'.format(reviewer_id=reviewer_id))

    @staticmethod
    def get_reviews_by_product_asin(asin_code, base_df):    
        return base_df.query('asin == "{asin_code}"'.format(asin_code=asin_code))
    @staticmethod
    def get_statistics_about_data():
        df = ElectronicsDF.get_electronicsdf()
        # Crosstab split according to overall score
        # print(pd.crosstab(index = df['overall'], columns="Total count"))
        # Empty reviews
        asd = df[df.reviewText.apply(lambda x: len(x)<30)]
        asd2 = df.reviewText.apply(lambda x: len(x))
        ct1 = pd.crosstab(index = asd2, columns="Total count")
        ct = pd.crosstab(index = df['overall'], columns="Total count")
        df = df.head()
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        #print(df[df['Positively_Rated'] == 0].iloc[0]['reviewText'])