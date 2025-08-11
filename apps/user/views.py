from apps.user.queries import UserQueries
from core.utils import get_user_option


class UserViews:
    def ordering_food(self):
        
        
        restaurants = """
        << Restoranlar ro'yxati >>
        
        1. Optepa
        2. Blissimo
        3. Evos
        """

        print(restaurants)
        try:
            rest_id = int(input("Restoran raqamini tanlang: "))
            option = get_user_option(menu=restaurants, max_option=3)
            if option == "1":
                ...
            elif option == "2":
                ...
            elif option == "3":
                ...

        except ValueError:
            print("Noto'g'ri raqam kiritildi")
            return self.ordering_food()

        foods = UserQueries.get_foods_by_restaurant_id(rest_id)
        if not foods:
            print("Bu restoranda hozircha ovqatlar mavjud emas.")
            return self.ordering_food()

        print("\n<< Ovqatlar ro'yxati >>")
        for food in foods:
            print(f"{food['id']}. {food['name']} - {food['price']} so'm")

        return True
