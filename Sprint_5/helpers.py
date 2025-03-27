import random
class DateToTest:
    @staticmethod
    def generation_email(name, surname, number_kogort, domain):
        email = f"{name}_{surname}_{number_kogort}_{random.randint(100, 999)}@{domain}"
        return email
