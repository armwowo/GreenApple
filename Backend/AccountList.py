from User import *

class AccountList:
    def __init__(self):
        self._account = []

    def check_user(self,user_name,password):
        for account in self._account:
            if account.get_username() == user_name and account.get_password() == password:
                return "Success"
            
        return "Not match"
    
    def register(self,name,lastname,email,user_name,password,user_phone):
        # Add a new user to the accountlist
        new_user = User(name,lastname,email,user_name,password,user_phone)
        self._account.append(new_user)
        return new_user
    
    def add_account(self,account):
        self._account.append(account)
    
    @property
    def account(self):
        return self._account