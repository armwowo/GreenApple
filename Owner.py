from User import User

class Owner(User):
    def __init__(self,name,lastname,email,user_name,password,user_phone,verified):
        User.__init__(self,name,lastname,email,user_name,password,user_phone)
        self._verified = verified
    def add_owner_tolList(owner):
        pass