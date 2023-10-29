from app_iris.IrisController import IrisController
from app_menu.MenuController import MenuController
from app_mobile.MobileController import MobileController

if __name__ == "__main__":
    menu_controller = MenuController(IrisController(), MobileController())
    menu_controller.init_gui()
