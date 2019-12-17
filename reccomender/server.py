import cherrypy
from run import get_prediction_1_2_ngram, get_reccomendations, get_reviews_by_reviewer_id, get_reccomendations_predict
from dataframes.cosinedf import CosineDF
from dataframes.basedf import BaseDf
from dataframes.differencesdf import DifferencesPivot
class RecommenderRest(object):

    cosine_differences = CosineDF.get_cosine_diffs()

    @cherrypy.expose
    def index(self):
        return {"moi": "lol"}

    @cherrypy.tools.json_out()
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def predict(self):
        if cherrypy.request.method == 'OPTIONS':
            return []
        predictions = get_prediction_1_2_ngram(cherrypy.request.json['reviews'])
        return {'predictions': predictions.tolist()}

    @cherrypy.expose
    def recommend(self, reviewerID):
        if not reviewerID:
            return {'error': "reviewerID required"}
        # user_id = "A35DQQH8W09HW"
        reccommendations = get_reccomendations(reviewerID, 7, RecommenderRest.cosine_differences)
        return reccommendations

    @cherrypy.expose
    def recommend_predict(self, reviewerID):
        if not reviewerID:
            return {'error': "reviewerID required"}
        # user_id = "A35DQQH8W09HW"
        
        reccommendations = get_reccomendations_predict(reviewerID, 7, CosineDF.get_cosine_diffs_predict(), reviews_by_reviewer_id=BaseDf.get_reviews_by_reviewer_id_predict(reviewerID), differences_df=DifferencesPivot.get_differences_df_predict())
        return reccommendations

    @cherrypy.expose
    def reviews(self, reviewerID):
        if not reviewerID:
            return {'error': "reviewerID required"}
        # user_id = "A35DQQH8W09HW"
        user_reviews = get_reviews_by_reviewer_id(reviewerID)
        return user_reviews

    @cherrypy.expose
    def statistics(self):
        return {}
if __name__ == '__main__':
    conf = {
        '/': {
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'image/jpeg'), ('Access-Control-Allow-Origin', 'http://localhost:3000')],
            'server.socket_host': '127.0.0.1',
            'server.socket_port': 8880,
            'cors.expose.on': True,
        }
    }
cherrypy.quickstart(RecommenderRest())