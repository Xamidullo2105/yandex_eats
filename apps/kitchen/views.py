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
    
    
    def show_pending_orders(self, kitchen_name):
        orders = KitchenQueries.get_pending_orders(kitchen_name)
        
        if not orders:
            print("Sizda hozircha yangi buyurtma yo'q.")
            return
        
        print(f"\n{kitchen_name} oshxonasidagi PENDING buyurtmalar:")
        for order in orders:
            print(f"{order['id']}. {order['food_name']} - {order['price']} so'm (status: {order['status']})")

    
    def show_ready_orders(self, kitchen_name):
        orders = KitchenQueries.get_ready_orders(kitchen_name)
        
        if not orders:
            print("Tayyor buyurtmalar yo'q.")
            return
        
        print(f"{kitchen_name} oshxonasidagi READY buyurtmalar:")
        for order in orders:
            print(f"{order['id']}. {order['food_name']} - {order['price']} so'm (status: {order['status']})")
