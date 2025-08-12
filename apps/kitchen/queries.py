from core.database import execute_query

class KitchenQueries:
    @staticmethod
    def insert_product(kitchen_name, food_name, price, quantity,):
        query = """
            INSERT INTO foods (kitchen_name, food_name, price, quantity)
            VALUES (%s, %s, %s, %s)
        """
        execute_query(query, (kitchen_name, food_name, price, quantity))
    