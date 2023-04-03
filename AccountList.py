from User import User

class AccountList:
    def __init__(self):
        self._account = []
    
    def check_user(self,user_name,password):
        for account in self._account:
            if account.get_username() == user_name and account.get_password() == password:
                return "Success"

        return "Not match"

    def add_account(self,account):
        self._account.append(account)
