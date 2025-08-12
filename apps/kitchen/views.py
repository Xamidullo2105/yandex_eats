from apps.kitchen.queries import KitchenQueries


class KitchenFunc(KitchenQueries):
    def __init__(self, kitchen_name=None, food_name=None, price=None, quantity=None):
        self.kitchen_name = kitchen_name
        self.food_name = food_name
        self.price = price
        self.quantity = quantity

    def add_foods(self):
        self.kitchen_name = input("Enter kitchen name: ")
        self.food_name = input("Enter food name: ")
        self.price = input("Enter food price: ")
        self.quantity = input("Enter food quantity: ")

        KitchenQueries.insert_product(self.kitchen_name, self.food_name, self.price, self.quantity)
        print(f"'{self.food_name}' successfully added ✅")