import streamlit as st
from app_iris.IrisController import IrisController
from app_mobile.MobileController import MobileController

class MenuView:

    def __init__(self, iris_controller: IrisController, mobile_controller: MobileController):
        self._iris_title = "KNN Demo"
        self._mobile_title = "Neural Network Demo"
        self._iris_controller = iris_controller
        self._mobile_controller = mobile_controller

    def init_menu(self):
        label = """
        
        Student: José Manuel Cuenca Lerma
        Program: MBD A1
        
        Choose a ML Application:
        """
        page = st.sidebar.radio(label, (self._iris_title, self._mobile_title))

        if page == self._iris_title:
            self._iris_controller.init_gui()
        elif page == self._mobile_title:
            self._mobile_controller.init_gui()
