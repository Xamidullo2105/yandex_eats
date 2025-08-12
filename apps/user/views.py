from apps.user.queries import UserQueries
from core.utils import restaurants


class UserViews:
    def ordering_food(self):
        print(restaurants)

        try:
            rest_id = int(input("Restoran raqamini tanlang: "))
        except ValueError:
            print("Noto'g'ri raqam kiritildi")
            return self.ordering_food()

        # rest_id dan restoran nomini aniqlash
        
        kitchens_map = {
            1: "Oqtepa",
            2: "Blissimo",
            3: "Evos"
        }
        kitchen_name = kitchens_map.get(rest_id)
        if not kitchen_name:
            print("Bunday restoran mavjud emas.")
            return self.ordering_food()

        foods = UserQueries.get_foods_by_kitchen(kitchen_name)
        if not foods:
            print("Bu restoranda hozircha ovqatlar mavjud emas.")
            return self.ordering_food()

        print(f"\n<< {kitchen_name} menyusi >>")
        for food in foods:
            print(f"{food['id']}. {food['food_name']} - {food['price']} so'm")

        try:
            food_id = int(input("Ovqat ID sini tanlang: "))
        except ValueError:
            print("Noto'g'ri raqam kiritildi")
            return self.ordering_food()

        UserQueries.insert_order(food_id)
        print("Buyurtma muvaffaqiyatli berildi ✅")


    def show_orders(self):
        orders = UserQueries.show_orders_query()
        
        if orders:
            for i in orders:
                print(i)
        else:
            print("No couriers found ❌")