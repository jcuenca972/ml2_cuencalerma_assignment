import pickle
import os
from app_iris.Iris import Iris
import pandas as pd
import numpy as np
from typing import List

class IrisModel:

    def __init__(self):
        self._model_url = "{}{}{}{}{}".format(os.getcwd(), os.sep, "app_iris", os.sep, "iris_model.sav")
        self._model = pickle.load(open(self._model_url, 'rb'))

    def _iris_to_pandas(self, iris_data: List[Iris]):
        data = np.array(
            [[iris.sepal_length_cm, iris.sepal_width_cm,
              iris.petal_length_cm, iris.petal_width_cm] for iris in iris_data]
        )
        return pd.DataFrame(data)

    def prediction(self, iris: Iris):
        data = self._iris_to_pandas([iris])
        return self._model.predict(data)[0]
