from core.database import execute_query


class UserQueries:
    @staticmethod
    def get_foods_by_kitchen(kitchen_name):
        query = """
            SELECT id, food_name, price
            FROM foods
            WHERE LOWER(kitchen_name) = LOWER(%s)
        """
        return execute_query(query, (kitchen_name,), fetch=True)
    
    
    @staticmethod
    def insert_order(food_id):
        query = "INSERT INTO orders (food_id, status) VALUES (%s, 'pending')"
        execute_query(query, (food_id,))
