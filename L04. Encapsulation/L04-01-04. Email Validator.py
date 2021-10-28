# L04-01. Encapsulation - Lab
# 04. Email Validator

class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return True if len(name) >= self.min_length else False

    def __is_mail_valid(self, mail):
        return True if mail in self.mails else False

    def __is_domain_valid(self, domain):
        return True if domain in self.domains else False

    def validate(self, email):
        idx_at = self.get_idx_at(email)
        idx_dot = self.get_idx_dot(email)

        name = email[:idx_at]
        mail = email[idx_at+1:idx_dot]
        domain = email[idx_dot+1:]

        if self.__is_name_valid(name) \
            and self.__is_mail_valid(mail) \
                and self.__is_domain_valid(domain):
            return True
        return False

    @staticmethod
    def get_idx_at(email):
        return email.find("@")

    @staticmethod
    def get_idx_dot(email):
        return email.rfind(".")


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
