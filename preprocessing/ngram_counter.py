import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


class NGramCounter:
    data_frame: pd.DataFrame
    column_to_encode: str
    ngram_length: int

    def __init__(self, data_frame: pd.DataFrame, column_to_encode: str, ngram_length: int):
        self.data_frame = data_frame
        self.column_to_encode = column_to_encode
        self.ngram_length = ngram_length

    def encode(self) -> pd.DataFrame:
        encoder = CountVectorizer(analyzer='char', ngram_range=(self.ngram_length, self.ngram_length))
        self.data_frame[self.column_to_encode] = self.data_frame[self.column_to_encode].fillna('')
        transformed = encoder.fit_transform(self.data_frame[self.column_to_encode].apply(lambda x: np.str_(x)))
        ohe_df = pd.DataFrame(transformed.todense(), columns=encoder.get_feature_names())
        return pd.concat([self.data_frame, ohe_df], axis=1).drop([self.column_to_encode], axis=1)
