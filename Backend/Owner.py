from Backend.User import User

class Owner(User):
    def __init__(self,name,lastname,email,user_name,password,user_phone):
        User.__init__(self,name,lastname,email,user_name,password,user_phone)
        self._verified = 0
        User.set_Role(self,"Owner")
    def add_owner_tolList(owner):
        pass
    @property
    def verified(self):return self._verified

    def change_status_verified(self):self._verified =1

