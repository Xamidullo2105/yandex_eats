from apps.admin.queries import AdminQueries


class AdminViews(AdminQueries):
    def __init__(self, role, name=None, password=None):
        if role not in ["couryer", "restoran"]:
            raise ValueError("Type must be 'couryer' or 'restoran'")
        self.name = name
        self.password = password
        self.type = role

    def add_couriers(self):
        self.name = input("Enter courier's name: ")
        self.password = input("Enter password: ")
        phone_number = input("Enter courier's phone number: ")

        AdminQueries.insert_courier(self.name, self.password, phone_number)
        print(f"'{self.name}' successfully added")

    
    def add_restorans(self):
        self.name = input("Enter restaurant's name: ")
        self.password = input("Enter password: ")

        AdminQueries.insert_restoran(self.name, self.password)
        print(f"'{self.name}' successfully added!")