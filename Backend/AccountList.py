from Backend.User import User
import re
from Backend.Owner import Owner


class AccountList:
    def __init__(self):
        self.__account = []

    def check_user(self, user_name, password):
        for account in self.__account:
            if account.get_username() == user_name and account.get_password() == password:
                return "Success"

        return "Not match"

    def register(self, name, lastname, email, user_name, password, user_phone, Role):
        # update conditions register 17/4
        pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:!]')
        check_number = r'^[0-9]'
        if re.fullmatch(pattern, email) and regex.search(password) == None and (re.match(check_number, user_phone) and len(user_phone) == 10):
            for account in self.__account:
                if account.get_username() == user_name and account.get_email() == email:
                    return "have this account in the system"
                elif account.get_username() == user_name:
                    return "This username already exists in the system."
                elif account.get_email() == email:
                    return "This email already exists in the system."
            if (Role == "User"):
                new_user = User(name, lastname, email,
                                user_name, password, user_phone)
                self.__account.append(new_user)
                return new_user
            elif (Role == "Owner"):
                new_user = Owner(name, lastname, email,
                                 user_name, password, user_phone)
                self.__account.append(new_user)
                print(new_user)
                return new_user
            return "Un Successful"
        else:
            return "Invalid password or email"

    def add_account(self, account):
        self.__account.append(account)

    @property
    def account(self):
        return self.__account
