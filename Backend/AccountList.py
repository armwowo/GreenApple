from Backend.User import User
import re
from Backend.Owner import Owner

class AccountList:
    def __init__(self):
        self.__account = []
    def check_user(self,user_name,password):
        # add conditions check_user 17/4
        for account in self.__account:
            if account.get_username() == user_name and account.get_password() == password:
                user  = account
                return user
            elif account.get_username() != user_name and account.get_password() == password:
                return "Invalid username"
            elif account.get_username() == user_name and account.get_password() != password:
                return "Invalid password"
        return "Not match"
    
    def register(self,name,lastname,email,user_name,password,user_phone,Role):
        # update conditions register 17/4
        pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:!]')
        check_number = r'^[0-9]'
        if re.fullmatch(pattern,email) and regex.search(password) == None and (re.match(check_number,user_phone )and len(user_phone)==10):
            for account in self.__account:
                if account.get_username() == user_name and account.get_email() == email:
                    return "have this account in the system"
                elif account.get_username() == user_name :
                    return "This username already exists in the system."
                elif account.get_email() == email :
                    return "This email already exists in the system."
            if( Role == "User"):new_user = User(name,lastname,email,user_name,password,user_phone)
            elif(Role == "Owner"):new_user = Owner(name,lastname,email,user_name,password,user_phone)
            self.__account.append(new_user)
            return "success"
        else : return "Invalid password or email"
        

    
    def add_account(self,account):
        self.__account.append(account)
    
    @property
    def account(self):
        if self.__account is None:
            return None
        return self.__account
    
    #test 
    def get_account(self):
        return self.__account

    def list_user_name(self):
        list_username = []
        for account in self.__account:
            list_username.append(account.get_username())
        return list_username
    def find_data_user (self,username):
        for account in self.account:
            if username == account.get_username():
                return account
            
        