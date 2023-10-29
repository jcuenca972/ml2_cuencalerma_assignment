from general.GeneralView import GeneralView
from app_mobile.Mobile import Mobile
from app_mobile.MobileModel import MobileModel

class MobileController:

    def __init__(self):
        self._view = GeneralView()
        self._model = MobileModel()
        self._mobile = Mobile(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    def run_predict(self):
        self._view.update_prediction_value(
            self._model.prediction(self._mobile)
        )

    def init_gui(self):
        self._view.init_container()
        self._view.write_titles("Mobile Price Range Calculator",
                                "Select your values")

        self._mobile.blue, self._mobile.dual_sim, \
            self._mobile.four_g, self._mobile.three_g, \
            self._mobile.touch_screen, self._mobile.wifi = self._view.write_binary_select_inputs(
            "Has bluetooth?", "Has Dual Sim?", "Has 4G?", "Has 3G?",
            "Has Touch Screen?", "Has Wifi?")

        self._mobile.battery_power, self._mobile.clock_speed, \
            self._mobile.fc, self._mobile.int_memory, self._mobile.m_dep, \
            self._mobile.mobile_wt, self._mobile.n_cores, self._mobile.pc, \
            self._mobile.px_height, self._mobile.px_width, \
            self._mobile.ram, self._mobile.sc_h, self._mobile.sc_w, \
            self._mobile.talk_time = self._view.write_number_inputs(
            "Battery power (mAh)", "Clock speed", "Front Camera (Mpx)",
            "Internal Memory (GB)", "Mobile Depth (cm)", "Mobile Weight", "Number of Cores",
            "Primary Camera (Mpx)", "Resolution Height (px)", "Resolution Width (px)",
            "RAM (Mb)", "Screen Height (cm)", "Screen Widht (cm)", "Talking Time"
            )

        self.run_predict()
