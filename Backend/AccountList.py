from Backend.User import User
import re

class AccountList:
    def __init__(self):
        self.__account = []

    def find_user(self,name):#ค้นหาหอ
        for user in self.__account:
            if name == user.name:
                return user
        return "Not found"
    
    def check_user(self,user_name,password):
        for account in self.__account:
            if account.get_username() == user_name and account.get_password() == password:
                user  = account
                return user
            elif account.get_username() != user_name and account.get_password() == password:
                return "Invalid username"
            elif account.get_username() == user_name and account.get_password() != password:
                return "Invalid password"
        return "Not match"
    
    def register(self,name,lastname,email,user_name,password,user_phone):
        for account in self.__account:
            if account.get_username() == user_name and account.get_email() == email:
                return "have this account in the system"
            elif account.get_username() == user_name :
                return "This username already exists in the system."
            elif account.get_email() == email :
                return "This email already exists in the system."
        new_user = User(name,lastname,email,user_name,password,user_phone)
        self.__account.append(new_user)
        return "success"
    
    def add_account(self,account):
        self.__account.append(account)
    
    @property
    def account(self):
        return self.__account
