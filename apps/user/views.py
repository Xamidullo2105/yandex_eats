from apps.user.queries import UserQueries
from core.utils import restaurants


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



# class UserViews:
#     def ordering_food(self):
        
#         print(restaurants)

#         try:
#             rest_index = int(input("Restoran raqamini tanlang: "))
#             kitchen_name = restaurants[rest_index - 1]
#         except (ValueError, IndexError):
#             print("Noto'g'ri tanlov ❌")
#             return self.ordering_food()

#         foods = UserQueries.get_foods_by_kitchen(kitchen_name)
#         if not foods:
#             print("Bu restoranda ovqatlar hozircha yo'q :(")
#             return self.ordering_food()

#         print("\n<< Ovqatlar ro'yxati >>")
#         for food in foods:
#             print(f"{food['id']}. {food['food_name']} - {food['price']} so'm")

#         try:
#             food_id = int(input("Ovqat ID sini tanlang: "))
#             UserQueries.insert_order(food_id)
#             print("Buyurtma qabul qilindi ✅")

#         except ValueError:
#             print("Noto'g'ri ID kiritildi ❌")
#             return self.ordering_food()


# class UserViews:
#     def ordering_food(self):
        
#         print(restaurants)
        
#         try:
#             rest_id = int(input("Restoran raqamini tanlang: "))
#             option = get_user_option(menu=restaurants, max_option=3)
#             if option == "1":
#                 ...
#             elif option == "2":
#                 ...
#             elif option == "3":
#                 ...

#         except ValueError:
#             print("Noto'g'ri raqam kiritildi")
#             return self.ordering_food()

#         foods = UserQueries.get_foods_by_restaurant_id(rest_id)
#         if not foods:
#             print("Bu restoranda hozircha ovqatlar mavjud emas.")
#             return self.ordering_food()

#         print("\n<< Ovqatlar ro'yxati >>")
#         for food in foods:
#             print(f"{food['id']}. {food['name']} - {food['price']} so'm")

#         return True
