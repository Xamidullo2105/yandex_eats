import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apps.auth.queries import AuthQueries
from apps.auth.utils import AuthValidation
from core.config import EMAIL, EMAIL_PASSWORD


class RegisterView(AuthValidation, AuthQueries):
    def verify_code(self):
        email = input("Enter your email: ")
        code = input("Enter your verification code: ")

        verification_code = self.get_verification_code(email, code)
        if not verification_code:
            print("Invalid code")
            return self.verify_code()
        else:
            self.update_user_status(True, email)
            print("You can login now")
            return True

    def generate_code(self, email):
        while True:
            random_code = str(random.randint(1000, 9999)).strip()
            verification_code = self.get_verification_code(email, random_code)
            if not verification_code:
                self.add_code(random_code, email)
                return random_code

    def send_mail(self, receiver_email, subject, message):
        try:
            msg = MIMEMultipart()
            msg['From'] = EMAIL
            msg['To'] = receiver_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL, EMAIL_PASSWORD)
            server.sendmail(EMAIL, receiver_email, msg.as_string())
            server.quit()

            print("Email muvaffaqiyatli yuborildi")
            return True
        except Exception as e:
            print("Xatolik:", e)
    
    
    def register(self):
        name = input("Enter your full name: ")
        email = input("Enter your email: ")
        password1 = input("Enter your password: ")
        password2 = input("Confirm your password: ")

        while not self.check_email(email):
            email = input("Enter your email: ")

        while not self.check_password(password1, password2):
            password1 = input("Enter your password: ")
            password2 = input("Confirm your password: ")

        params = (name, email, password1)
        add_result = self.add_user(params)

        if add_result is False:
            print("Bu pochdata foydalanuvchi mavjud ❌")
            return
        elif add_result is None:
            print("Foydalanuvchi qo'shishda xato ❌")
            return

        code = self.generate_code(email)

        subject = "Your verification code"
        message = f"Your code: {code}"

        if self.send_mail(email, subject, message):
            print("Code yuborildi✅")
        
            self.verify_code()
        
        else:
            print("Kode yuborilmadi ❌.")


class LoginView(AuthQueries):
    admin_password = "a"
    admin_email = "a"
    
    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email == self.admin_email and password == self.admin_password:
            print("Welcome Admin")
            return "admin"

        user = self.get_user_by_email(email)
        if user and user['password'] == password:
            self.update_user_is_login(email=email)
            print(f"Welcome, {user['name']}")
            return "user" 

        kitchen = self.get_kitchen_by_email(email)
        if kitchen and kitchen['password'] == password:
            self.update_kitchen_is_login(email=email)
            print(f"Welcome Kitchen, {kitchen['name']}")
            return "kitchen"

        courier = self.get_courier_by_user_id(email)
        if courier and courier['password'] == password:
            self.update_courier_is_login(email=email)
            print(f"Welcome Courier, {courier['name']}")
            return "courier"

        return False



class LogoutView(AuthQueries):
    def logout_all(self):
        self.logout_all_users()
