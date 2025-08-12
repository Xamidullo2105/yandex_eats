from core.database import execute_query

class AdminQueries:
    @staticmethod
    def insert_courier(name, password, email):
        query = """
            INSERT INTO couriers (name, password, email)
            VALUES (%s, %s, %s)
        """
        params = (name, password, email)
        execute_query(query, params)
        
    
    @staticmethod
    def insert_kitchen(name, password, email):
        query = """
            INSERT INTO kitchens (name, password, email)
            VALUES (%s, %s, %s)
        """
        execute_query(query, (name, password, email))
    
    
    @staticmethod
    def delete_courier_query(id):
        query = """
        DELETE FROM couriers WHERE id = %s 
        """
        execute_query(query, (id,))
    
    
    @staticmethod
    def delete_kitchen_query(id):
        query = """
        DELETE FROM couriers WHERE id = %s
        """
        execute_query(query, (id,))
    
    
    @staticmethod
    def show_courier_query():
        query = """
        SELECT * FROM couriers;
        """
        couriers = execute_query(query, fetch="all")
        return couriers
    
    
    @staticmethod
    def show_kitchen_query():
        query = """
        SELECT * FROM kitchens;
        """
        kitchens = execute_query(query, fetch="all")
        return kitchens