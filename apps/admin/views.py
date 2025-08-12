from apps.admin.queries import AdminQueries


class AdminViews(AdminQueries):
    def __init__(self, role, name=None, password=None):
        if role not in ["courier", "kitchen"]:
            raise ValueError("Type must be 'courier' or 'kitchen'")
        self.name = name
        self.password = password
        self.role = role

    def add_couriers(self):
        self.name = input("Enter courier's name: ")
        self.password = input("Enter password: ")
        email = input("Enter courier's email: ")

        AdminQueries.insert_courier(self.name, self.password, email)
        print(f"'{self.name}' successfully added ✅")

    
    def add_kitchen(self):
        self.name = input("Enter kitchen's name: ")
        self.password = input("Enter password: ")
        email = input("Enter the email: ")

        AdminQueries.insert_kitchen(self.name, self.password, email)
        print(f"'{self.name}' successfully added ✅")
    
    
    def delete_courier(self):
        self.id = input("Enter courier id: ")
        
        AdminQueries.delete_courier_query(self.id)
        print(f"{self.id} courier with id deleted 🗑")
    
    
    def delete_kitchen(self):
        self.id = input("Enter kitchen id: ")
        
        AdminQueries.delete_kitchen_query(self.id)
        print(f"{self.id} courier with id deleted 🗑")
    
    
    def show_couriers(self):
        couriers = AdminQueries.show_courier_query()
        
        if couriers:
            for i in couriers:
                print(i)
        else:
            print("No couriers found ❌")
    
    
    def show_kitchens(self):
        kitchens = AdminQueries.show_kitchen_query()
        
        if kitchens:
            for i in kitchens:
                print(i)
        else:
            print("No kitchens found ❌")