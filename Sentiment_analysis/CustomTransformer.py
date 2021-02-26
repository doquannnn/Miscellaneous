import re
from nltk.stem import PorterStemmer
from sklearn.base import BaseEstimator, TransformerMixin
class TextPreprocessing(BaseEstimator, TransformerMixin):
    def __init__(self):
        return None

    def preprocess_words(self, text):
        stemmer = PorterStemmer()
        words = text.split()

        stemmed_words = [stemmer.stem(word) for word in words]
        return ' '.join(stemmed_words)

    def extract_words(self, text):
        text = text.lower()

        url = r'((http://)*|(https://)*|(www\.)*|([^\s]+.com[^\s]+))'
        text = re.sub(url, '', text)
        text = re.sub('@[^\s]+', '', text)

        return text

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X.loc[:, 'text'].apply(lambda x: self.extract_words(x))
        X.loc[:, 'text'].apply(lambda x: self.preprocess_words(x))
        return X['text']