from core.database import execute_query


class AuthQueries:
    @staticmethod
    def get_user_by_email(email) -> dict | None:
        query = "SELECT * FROM users WHERE email = %s"
        params = (email,)

        user = execute_query(query=query, params=params, fetch="one")
        return user if user else None
    
    
    @staticmethod
    def get_kitchen_by_email(email) -> dict | None:
        query = "SELECT * FROM kitchens WHERE email = %s"
        params = (email,)
        kitchen = execute_query(query=query, params=params, fetch="one")
        return kitchen if kitchen else None


    @staticmethod
    def get_courier_by_user_id(email) -> dict | None:
        query = "SELECT * FROM couriers WHERE email = %s"
        params = (email,)
        courier = execute_query(query=query, params=params, fetch="one")
        return courier if courier else None
    
    
    @staticmethod
    def update_user_role(email, role) -> bool:
        query = "UPDATE users SET role = %s WHERE email = %s"
        params = (role, email)
        execute_query(query=query, params=params)
        return True


    @staticmethod
    def update_user_is_login(email) -> dict | bool:
        query = "UPDATE users SET is_login = %s WHERE email = %s"
        params = (True, email,)
        execute_query(query=query, params=params)
        return True

    @staticmethod
    def get_active_user() -> dict | None:
        """
        get current is_login user from database
        if not exists return None
        :return:
        """
        query = "SELECT * FROM users WHERE is_login = %s"
        params = (True,)

        user = execute_query(query=query, params=params, fetch="one")
        return user if user else None

    @staticmethod
    def add_user(params: tuple) -> None | bool:
        try:
            name, email, password = params
            existing = AuthQueries.get_user_by_email(email)
            if existing:
                print("❌ User already exists with this email")
                return False
            
            query = """INSERT INTO users (name, email, password)
                    VALUES (%s, %s, %s)
                    """

            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def get_verification_code(email, code) -> dict | None:
        try:
            query = "SELECT * FROM codes WHERE email = %s AND code = %s"
            params = (email, code,)

            verification_code = execute_query(query=query, params=params, fetch="one")
            return verification_code if verification_code else None
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def add_code(code, email) -> None | bool:
        try:
            query = """INSERT INTO codes (code, email)
                    VALUES (%s, %s)
                    """
            params = (code, email)
            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def update_user_status(status, email) -> None | bool:
        try:
            query = "UPDATE users SET is_active = %s WHERE email = %s"
            params = (status, email,)
            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def logout_all_users() -> None | bool:
        try:
            query = "UPDATE users SET is_login = False"
            execute_query(query=query)
            return True
        except Exception as e:
            print(e)
            return None
