import re
from apps.auth.queries import AuthQueries


class AuthValidation(AuthQueries):
    def __init__(self):
        self.errors = []

    def check_email(self, email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if re.match(pattern, email):
            return True
        print("Invalid email format!")
        return False

    def check_password(self, password1, password2):
        if password1 != password2:
            print("Passwords do not match!")
            return False
        if len(password1) < 6:
            print("Password should be at least 6 characters!")
            return False
        return True
