import pandas as pd
from joblib import load
import os
from tensorflow.keras.models import load_model
from app_mobile.Mobile import Mobile
from typing import List

class MobileModel:

    def __init__(self):
        self._model_url = "{}{}{}{}{}".format(os.getcwd(), os.sep, "app_mobile", os.sep, "mobile_model.keras")
        self._transformer_url = "{}{}{}{}{}".format(os.getcwd(), os.sep, "app_mobile", os.sep, "feature_pipeline.joblib")
        self._model = load_model(self._model_url)
        self._feature_transformer = load(self._transformer_url)
        self._output_decoder = {
            0: "low cost",
            1: "medium cost",
            2: "high cost",
            3: "very high cost"
        }

    def _mobile_to_pandas(self, mobile_list: List[Mobile]):
        return pd.DataFrame([mobile.__dict__ for mobile in mobile_list])

    def prediction(self, mobile: Mobile):
        data = self._mobile_to_pandas([mobile])
        new_data_transformed = self._feature_transformer.transform(data)
        prediction = self._model.predict(new_data_transformed).argmax(axis=1)
        return self._output_decoder[prediction[0]]

