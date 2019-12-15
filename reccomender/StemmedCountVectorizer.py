from sklearn.feature_extraction.text import CountVectorizer
import nltk.stem


english_stemmer = nltk.stem.SnowballStemmer('english')

class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        return super(StemmedCountVectorizer, self).build_analyzer()
        # return lambda doc: ([english_stemmer.stem(w) for w in analyzer(doc)])