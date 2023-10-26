from app_iris.IrisController import IrisController
from app_menu.MenuController import MenuController

if __name__ == "__main__":
    menu_controller = MenuController(IrisController())
    menu_controller.init_gui()
