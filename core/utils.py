from core.database import execute_query

main_menu = """
        ╔═════════════════════════╗
        ║       AUTH MENU         ║
        ╠═════════════════════════╣
        ║   1. Register           ║
        ║   2. Login              ║
        ║   3. Logout             ║
        ╚═════════════════════════╝
    """


user_menu = """
    1. Ordering food
    2. Show orders
    3. Logout
    """


restaurants = """
    << Restaurant List >>
    
    1. Oqtepa
    2. Blissimo
    3. Evos
    """


admin_menu = """
    1. Add couries
    2. Add kitchen
    3. Delete courier
    4. Delete kitchen
    5. Show courier
    6. Show kitchen
    7. Exit 
    """


courier_menu = """
    1. Get an order
"""


kitchen_menu = """
    1. Add food
    2. Order preparation
    3. Ready orders
    4. Unfinished order
"""

def get_user_option(menu: str, max_option: int):
    while True:
        print(menu)
        option = input("Enter your option: ")
        if not (1 <= int(option) <= max_option):
            print("Invalid option number!")
        else:
            return option


def execute_tables():
    from apps.auth.models import users_query, verification_codes_query
    from apps.courier.models import courier_query
    from apps.kitchen.models import kitchen_query, foods_query
    from apps.user.models import orders_query

    execute_query(query=users_query)
    execute_query(query=verification_codes_query)
    execute_query(query=courier_query)
    execute_query(query=kitchen_query)
    execute_query(query=foods_query)
    execute_query(query=orders_query)
