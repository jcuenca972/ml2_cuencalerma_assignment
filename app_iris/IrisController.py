from general.GeneralView import GeneralView
from app_iris.Iris import Iris
from app_iris.IrisModel import IrisModel


class IrisController:

    def __init__(self):
        self._view = GeneralView()
        self._model = IrisModel()
        self._iris = Iris(0, 0, 0, 0)

    def run_predict(self):
        self._view.update_prediction_value(self._model.prediction(self._iris))

    def init_gui(self):
        self._view.init_container()
        self._view.write_titles("k-nearest neighbors applied on Iris Dataset",
                                "Select your values")
        self._iris.sepal_length_cm, self._iris.sepal_width_cm, \
            self._iris.petal_length_cm, self._iris.petal_width_cm = self._view.write_number_inputs(
            "Sepal Length cm", "Sepal Width cm",
            "Petal Length cm", "Petal Width cm"
        )
        self.run_predict()
