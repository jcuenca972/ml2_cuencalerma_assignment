import streamlit as st
from app_iris.IrisController import IrisController

class MenuView:

    def __init__(self, iris_controller: IrisController):
        self._iris_title = "KNN Demo"
        self._iris_controller = iris_controller

    def init_menu(self):
        label = """
        
        Student: José Manuel Cuenca Lerma
        Program: MBD A1
        
        Choose a ML Application:
        """
        page = st.sidebar.radio(label, (self._iris_title, 'Page 2'))

        if page == self._iris_title:
            self._iris_controller.init_gui()
        elif page == 'Page 2':
            st.write('Welcome to Page 2')
