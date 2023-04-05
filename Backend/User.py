import Backend.InstanceUser
class User:
    def __init__(self,name,lastname,email,user_name,password,user_phone):
        self._name = name
        self._lastname = lastname
        self._email = email
        self._username = user_name
        self._password = password
        self._userphone = user_phone
        self.__reservation = []
        self.__reserved = []
    def add_to_list(User):
        pass
    
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
    
    def add_reservation(self,reservation):
        self.__reservation.append(reservation)
        return "success"
    
    def add_reserved(self,room_reserved):
        self.__reserved.append(room_reserved)
        return "success"
    
    @property
    def reservation_list(self):
        return self.__reservation
    @property
    def reserved_list(self):
        return self.__reserved
    
def create_user(user_list):
    for key,value in Backend.InstanceUser.user_info.items() :
        new_user = User(name=Backend.InstanceUser.user_info[key]["name"],
                        lastname=Backend.InstanceUser.user_info[key]["last name"],
                        email=Backend.InstanceUser.user_info[key]["email"],
                        user_name=Backend.InstanceUser.user_info[key]["username"],
                        password=Backend.InstanceUser.user_info[key]["password"],
                        user_phone=Backend.InstanceUser.user_info[key]["user_phone"])
        
        user_list.append(new_user) #add new_user แต่ละตัวเข้า user_list
