# L04-01. Encapsulation - Lab
# 03. Profile

class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, string):
        if 5 <= len(string) <= 15:
            self.__username = string
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, string):
        if self.is_password_length_valid(string) \
            and self.is_password_contains_uppercase(string) \
                and self.is_password_contains_digit(string):
            self.__password = string
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    @staticmethod
    def is_password_length_valid(password):
        return len(password) >= 8

    @staticmethod
    def is_password_contains_uppercase(password):
        upper_letters = [char for char in password if char.isupper()]
        return True if upper_letters else False

    @staticmethod
    def is_password_contains_digit(password):
        digits = [char for char in password if char.isdigit()]
        return True if digits else False

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


# profile_with_invalid_password = Profile('My_username', 'My-password')

# profile_with_invalid_username = Profile('Too_long_username', 'Any')

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
