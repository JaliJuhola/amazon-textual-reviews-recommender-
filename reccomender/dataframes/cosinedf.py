import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class CosineDF:

    @staticmethod
    def save_cosine_differences(differences_pivot):
        cosine = cosine_similarity(differences_pivot)
        np.fill_diagonal(cosine, 0)
        dfa = pd.DataFrame(cosine,index=differences_pivot.index)
        dfa.columns=differences_pivot.index
        dfa.to_pickle("reccomender/data/video_game_reviews_cosines")
        return dfa

    @staticmethod
    def get_cosine_diffs():
        return pd.read_pickle("reccomender/data/video_game_reviews_cosines")