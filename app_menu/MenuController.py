from app_menu.MenuView import MenuView
from app_iris.IrisController import IrisController

class MenuController:

    def __init__(self, iris_controller: IrisController):
        self._menu_view = MenuView(iris_controller)

    def init_gui(self):
        self._menu_view.init_menu()
