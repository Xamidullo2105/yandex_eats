from core.database import execute_query


class UserQueries:
    @staticmethod
    def get_foods_by_restaurant_id(restaurant_id):
        query = "SELECT * FROM foods WHERE restaurant_id = %s"
        params = (restaurant_id,)
        foods = execute_query(query=query, params=params, fetch="all")
        return foods if foods else None