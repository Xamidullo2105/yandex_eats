from core.database import execute_query

class KitchenQueries:
    @staticmethod
    def insert_product(kitchen_name, food_name, price, quantity,):
        query = """
            INSERT INTO foods (kitchen_name, food_name, price, quantity)
            VALUES (%s, %s, %s, %s)
        """
        execute_query(query, (kitchen_name, food_name, price, quantity))
    
        
    @staticmethod
    def get_pending_orders(kitchen_name):
        query = """
            SELECT o.id, f.food_name, f.price, o.status
            FROM orders o
            JOIN foods f ON o.food_id = f.id
            WHERE o.status = 'pending'
            AND f.kitchen_name = %s
        """
        return execute_query(query, (kitchen_name,), fetch=True)

    
    @staticmethod
    def get_ready_orders(kitchen_name):
        query = """
            SELECT o.id, f.food_name, f.price, o.status
            FROM orders o
            JOIN foods f ON o.food_id = f.id
            WHERE o.status = 'ready'
            AND f.kitchen_name = %s
        """
        return execute_query(query, (kitchen_name,), fetch=True)
