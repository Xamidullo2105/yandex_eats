from apps.kitchen.queries import KitchenQueries


class KitchenFunc(KitchenQueries):
    def __init__(self, name=None, price=None, quantity=None):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_products(self):
        self.name = input("Enter product's name: ")
        self.price = input("Enter product's price: ")
        self.quantity = input("Enter product's quantity: ")

        KitchenQueries.insert_product(self.name, self.price, self.quantity)
        print(f"'{self.name}' successfully added!")