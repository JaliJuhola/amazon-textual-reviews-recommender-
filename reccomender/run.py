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

#user_id = "A35DQQH8W09HW"
#reccommendations = get_reccomendations(user_id, 7)
#print(get_reviews_by_reviewer_id(user_id))
#print(reccommendations)

#print(get_prediction_1_2_ngram(["One of the top 3 RPGs realease at this time (along with Bethesda's own Skyrim, and Witcher 3). The vastness of the open environment, and amount of choice and customization is just excellent. Some decisions are a little too black and white for my tastes, but pretty minor complaint. Occasional glitches exist - save your game frequently. Graphics are top notch. Voice acting is mostly top-notch. Plot isn't up to Witcher standards, but still far and away better than other games. If you don't get at least 200 hours of gameplay out of this you're either a responsible adult (I, sadly, am not) or you're just not taking in the full experience.", "I have been a huge fan of the Fallout series for a long time. I have every Fallout game. Although this game is different in many aspects of what I have come to love in Fallout, it still is an absolutely great game. The immersive stories, the endless mods, the ability to create your own settlement in the wasteland and the endless areas to explore. All of it comes together in a great way to make this game one to remember. I am already about 60 hours into the game and I feel like I have barely scratched the surface on the possibilities. Every time I get on to play I have a particular goal in mind that I plan to do then maybe play something else, or go outside. As I am playing I come across three other side quests, a new location and and cool new gun that just sucks me in. Everywhere you go on the map has something new for you to do. If you love open world formats, almost complete control on every aspect of your character, storylines that will suck you in and action that will leave you stunned then this game is an absolute must buy.", "First aspect is not of the game but Amazon I was excited to play this game release day and it never came... Got a tracking update and came a day late. All was made well by Amazon and was not that big of a deal but if you want a game the day of release you might want to pre order locally or Get a digital copy. Second the Game I do not have a ton of time in yet, but so far I would say it was worth getting during release. The beginning story line is a little narrow, but I expect options to open A LOT more as I play on. Many new aspects were put into this game including, in depth crafting, and building. The crafting makes useless objects like a toaster in FO3 useful in FO4. The building is a nice add but not the most refined. You can do more than make guns, like manage and build a community (houses, defenses, markets etc). The main fault with it, is item placement. It is sometimes difficult due limited camera movement, distance, and angles. Other than that I have not really experienced anything negative with the game. I think it is a step in the right direction from FO3 and would recommend to any fallout fan.", "The game is great, but I find my self more and more having to search online on how to get past certain glitches in various missions. It gets pretty annoying. Worse yet I'm late to playing the game, like 2 1/2 years late, so I don't know that Bethesda studios will be in any rush to push out anymore updates. I hear a game of the year bundle is coming out, maybe that will address more of the bugs, and I would suggest waiting on that because it includes all of the add-one. Otherwise it's a huge game, ton of hours of gameplay. Pretty much have to be jobless or an insomniac to put a dent in it."]))
