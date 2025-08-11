import logging
from apps.user.views import UserViews
from apps.auth.views import RegisterView, LogoutView, LoginView
from core.utils import main_menu, get_user_option, execute_tables
from core.utils import main_menu, get_user_option, execute_tables, user_menu, admin_menu, kitchen_menu, courier_menu
from apps.admin.views import AdminViews
from apps.kitchen.views import KitchenFunc

logging.basicConfig(level=logging.INFO, filename='logs.log')
logger = logging.getLogger(__name__)


class Menu:
    def main_menu(self):
        option = get_user_option(menu=main_menu, max_option=3)
        if option == "1":
            result = RegisterView().register()
            if not result:
                print("Something get wrong, try again later")
        elif option == "2":
            result = LoginView().login()
            if result == "user":
                return self.user_menu()
            elif result == "admin":
                return self.admin_menu()
            elif result == "courier":
                return self.courier_menu()
            elif result == "kitchen":
                return self.kitchen_menu()
            else:
                print("Invalid phone number or password")
        elif option == "3":
            return LogoutView().logout_all()
        return self.main_menu()

    def user_menu(self):
        option = get_user_option(menu=user_menu, max_option=3)
        if option == "1":
            UserViews().ordering_food()
        elif option == "2":
            ...
        elif option == "3":
            return LogoutView().logout_all()
        return self.user_menu()

    def admin_menu(self):
        option = get_user_option(menu=admin_menu, max_option=5)
        if option == "1":
            AdminViews().add_couriers()
        elif option == "2":
            AdminViews().add_restorans()
        elif option == "3":
            ...
        elif option == "4":
            ...
        elif option == "5":
            LogoutView().logout_all()
            return self.main_menu()
        return self.admin_menu()

    def kitchen_menu(self):
        option = get_user_option(menu=kitchen_menu, max_option=3)
        if option == "1":
            KitchenFunc().add_products()
        elif option == "2":
            ...
        elif option == "3":
            ...
        return self.admin_menu()

    def courier_menu(self):
        option = get_user_option(menu=courier_menu, max_option=1)
        if option == "1":
            ...
        return self.admin_menu()

if __name__ == '__main__':
    # execute_tables()
    LogoutView.logout_all_users()
    Menu().main_menu()
