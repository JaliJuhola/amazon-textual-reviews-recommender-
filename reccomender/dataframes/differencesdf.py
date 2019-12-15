import pandas as pd


class DifferencesPivot():

    @staticmethod
    def save_differences_pivot(base_df):
        # Calculating difference dataframe
        difference_df = DifferencesPivot.add_differences_to_ratings(base_df)
        difference_df.review_score = difference_df.review_score.astype('float')
        difference_df.drop('reviewer_mean', axis=1, inplace=True)
        difference_df.difference_to_reviewer_mean = difference_df.difference_to_reviewer_mean.astype('float')
        difference_df.to_pickle("reccomender/data/video_game_reviews_difference")
        # Creating pivot
        video_game_differences_pivot = DifferencesPivot.create_pivot_difference(difference_df)
        video_game_differences_pivot.to_pickle("reccomender/data/video_game_reviews_difference_pivot")
        return DifferencesPivot.get_differences_pivot()

    @staticmethod
    def get_differences_df():
        return pd.read_pickle("reccomender/data/video_game_reviews_difference")
        
    @staticmethod
    def calculate_mean(base_df):
        return base_df.groupby(by="reviewerID",as_index=False)['overall'].mean()

    @staticmethod
    def add_differences_to_ratings(base_df):
        mean = DifferencesPivot.calculate_mean(base_df=base_df)
        rating_avg = pd.merge(base_df,mean,on='reviewerID')
        rating_avg['difference_to_reviewer_mean']=rating_avg['overall_x'] - rating_avg['overall_y']
        rating_avg.rename(columns={'overall_x':'review_score', 'overall_y':'reviewer_mean'}, inplace=True)
        return rating_avg

    @staticmethod
    def get_differences_pivot(): 
        return pd.read_pickle("reccomender/data/video_game_reviews_difference_pivot")

    @staticmethod
    def create_pivot_difference(differences_df):
        differences_pivot = differences_df.pivot_table(index='reviewerID', columns='asin', values='difference_to_reviewer_mean')
        # Replacing NaN values with videogames average score
        differences_pivot = differences_pivot.fillna(0)

        return differences_pivot
