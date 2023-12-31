from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

logins = {"admin": "admin"}

class LoginPageApp(App):
    pass

class LoginManager(ScreenManager):
    pass

class LoginScreen(Screen):
    def login(self, username, password):
        if username in logins and logins[username] == password:
            self.manager.current = "main"
            self.manager.get_screen("main").ids.greeting_label.text = f"Hello there, {username}!"
        else:
            self.manager.get_screen("login").ids.error_label.text = "Wrong username or password!"

class RegisterScreen(Screen):
    def check_password_requirements(self, password):
        special_characters = "!@#$%^&*()_+{}:\"<>?|[];',./`~"
        length = False
        has_number = False
        has_capital = False
        has_lowercase = False
        has_special = False

        if len(password) <= 8:
            self.manager.get_screen("register").ids.password_length_label.color = (1, 0, 0, 1)
        else:
            self.manager.get_screen("register").ids.password_length_label.color = (0, 1, 0, 1)
            length = True

        if not any(char.isdigit() for char in password):
            self.manager.get_screen("register").ids.number_label.color = (1, 0, 0, 1)
        else:
            self.manager.get_screen("register").ids.number_label.color = (0, 1, 0, 1)
            has_number = True

        if not any(char.isupper() for char in password):
            self.manager.get_screen("register").ids.capital_letter_label.color = (1, 0, 0, 1)
        else:
            self.manager.get_screen("register").ids.capital_letter_label.color = (0, 1, 0, 1)
            has_capital = True

        if not any(char.islower() for char in password):
            self.manager.get_screen("register").ids.lowercase_letter_label.color = (1, 0, 0, 1)
        else:
            self.manager.get_screen("register").ids.lowercase_letter_label.color = (0, 1, 0, 1)
            has_lowercase = True

        if not any(char in special_characters for char in password):
            self.manager.get_screen("register").ids.special_character_label.color = (1, 0, 0, 1)
        else:
            self.manager.get_screen("register").ids.special_character_label.color = (0, 1, 0, 1)
            has_special = True
            
        if length and has_number and has_capital and has_lowercase and has_special:
            return True
        
    def check_matching_passwords(self, password, confirm_password):
        if password != confirm_password:
            self.manager.get_screen("register").ids.matching_passwords_label.color = (1, 0, 0, 1)
        else:
            self.manager.get_screen("register").ids.matching_passwords_label.color = (0, 1, 0, 1)
            return True
 
    def register(self, username, password):
        if self.check_password_requirements(password):
            logins[username] = password
            self.manager.current = "login"
        else:
            self.manager.current = "register"

class MainScreen(Screen):
    pass

LoginPageApp().run()