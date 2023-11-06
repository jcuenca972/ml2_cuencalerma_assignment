from app_menu.MenuView import MenuView
from app_iris.IrisController import IrisController
from app_mobile.MobileController import MobileController

class MenuController:

    def __init__(self, iris_controller: IrisController, mobile_controller: MobileController):
        self._menu_view = MenuView(iris_controller, mobile_controller)

    def init_gui(self):
        self._menu_view.init_menu()
    
