import InstanceUser
class User:
    def __init__(self,name,lastname,email,user_name,password,user_phone):
        self._name = name
        self._lastname = lastname
        self._email = email
        self._username = user_name
        self._password = password
        self._userphone = user_phone

    def get_name(self):
        return self._name
    def get_lastname(self):
        return self._lastname
    def get_email(self):
        return self._email
    def get_username(self):
        return self._username
    def get_password(self):
        return self._password
    def get_userphone(self):
        return self._userphone
    

def create_user(user_list):
    for key,value in InstanceUser.User_info.items() :
        new_user = User(name=InstanceUser.User_info[key]["name"],
                        lastname=InstanceUser.User_info[key]["last name"],
                        email=InstanceUser.User_info[key]["email"],
                        user_name=InstanceUser.User_info[key]["username"],
                        password=InstanceUser.User_info[key]["password"],
                        user_phone=InstanceUser.User_info[key]["user_phone"])
        
        user_list.append(new_user)#add new_user แต่ละตัวเข้า user_list