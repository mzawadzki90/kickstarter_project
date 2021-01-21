import re  # For preprocessing
from time import time  # To time our operations

import numpy as np
import pandas as pd
import spacy
from gensim.models import Word2Vec


class MeanEmbeddingVectorizer(object):
    word2vec: Word2Vec
    dim: int

    def __init__(self, word2vec: Word2Vec):
        self.word2vec = word2vec
        # if a text is empty we should return a vector of zeros
        # with the same dimensionality as all the other vectors
        self.dim = word2vec.vector_size

    def transform(self, data_frame: pd.DataFrame, column_to_encode: str) -> pd.DataFrame:
        data_frame[column_to_encode] = self.preprocess(data_frame, column_to_encode)
        data_frame[column_to_encode] = data_frame[column_to_encode].str.split()
        data_frame[column_to_encode] = data_frame[column_to_encode].apply(lambda x: [] if x is None else x)
        transformed = np.array([
            np.mean([self.word2vec[w] for w in words if w in self.word2vec]
                    or [np.zeros(self.dim)], axis=0)
            for words in data_frame[column_to_encode]
        ])
        return pd.concat([data_frame, pd.DataFrame(transformed)], axis=1).drop([column_to_encode], axis=1)

    def preprocess(self, data_frame: pd.DataFrame, column_to_encode: str) -> pd.DataFrame:
        # Cleaning
        # We are lemmatizing and removing the stopwords and non-alphabetic characters for each line
        nlp = spacy.load('en_core_web_sm', disable=['ner', 'parser'])  # disabling Named Entity Recognition for speed

        # Removes non-alphabetic characters
        brief_cleaning = (re.sub("[^A-Za-z']+", ' ', str(row)).lower() for row in data_frame[column_to_encode])

        # Taking advantage of spaCy .pipe() attribute to speed-up the cleaning process
        t = time()
        txt = [self.cleaning(doc) for doc in nlp.pipe(brief_cleaning, batch_size=5000, n_threads=-1)]
        # print('Time to clean up everything: {} mins'.format(round((time() - t) / 60, 2)))

        # Put the results in a DataFrame to remove missing values and duplicates:
        return pd.DataFrame({'clean': txt})

    def cleaning(self, doc):
        # Lemmatizes and removes stopwords
        # doc needs to be a spacy Doc object
        txt = [token.lemma_ for token in doc if not token.is_stop]
        # Word2Vec uses context words to learn the vector representation of a target word,
        # if a sentence is only one or two words long,
        # the benefit for the training is very small
        if len(txt) > 2:
            return ' '.join(txt)
