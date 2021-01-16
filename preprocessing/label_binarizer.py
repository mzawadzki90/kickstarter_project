import pandas as pd
from sklearn.preprocessing import LabelBinarizer


class DataFrameLabelBinarizer:
    data_frame: pd.DataFrame
    column_to_encode: str

    def __init__(self, data_frame: pd.DataFrame, column_to_encode: str):
        self.data_frame = data_frame
        self.column_to_encode = column_to_encode

    def encode(self) -> pd.DataFrame:
        encoder = LabelBinarizer()
        encoder.fit(self.data_frame[self.column_to_encode])
        transformed = encoder.transform(self.data_frame[self.column_to_encode])
        ohe_df = pd.DataFrame(transformed)
        return pd.concat([self.data_frame, ohe_df], axis=1).drop([self.column_to_encode], axis=1)
