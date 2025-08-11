from core.database import execute_query

class AdminQueries:
    @staticmethod
    def insert_courier(name, password, phone_number):
        query = """
            INSERT INTO couryers (name, password, phone_number)
            VALUES (%s, %s, %s)
        """
        params = (name, password, phone_number)
        execute_query(query, params)
        
    
    @staticmethod
    def insert_restoran(name, password):
        query = """
            INSERT INTO restorans (name, password)
            VALUES (%s, %s)
        """
        execute_query(query, (name, password))