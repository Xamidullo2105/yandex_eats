from core.database import execute_query

class KitchenQueries:
    @staticmethod
    def insert_product(name, price, quantity):
        query = """
            INSERT INTO products (name, price, quantity)
            VALUES (%s, %s, %s)
        """
        execute_query(query, (name, price, quantity))
    