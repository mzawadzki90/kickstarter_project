import numpy as np
import pandas as pd
from tensorflow import keras


class HashingTrick:
    data_frame: pd.DataFrame
    column_to_encode: str
    hashing_space: int

    def __init__(self, data_frame: pd.DataFrame, column_to_encode: str, hashing_space: int):
        self.data_frame = data_frame
        self.column_to_encode = column_to_encode
        self.hashing_space = hashing_space

    def encode(self) -> pd.DataFrame:
        self.data_frame[self.column_to_encode] = self.data_frame[self.column_to_encode].fillna('')
        self.data_frame[self.column_to_encode] = self.data_frame[self.column_to_encode].apply(lambda x: np.str_(x))
        df = pd.DataFrame(self.data_frame[self.column_to_encode].apply(
            lambda x: keras.preprocessing.text.hashing_trick(x, self.hashing_space)))
        print(df.sample(5))
        return pd.concat([self.data_frame, df], axis=1).drop([self.column_to_encode], axis=1)
