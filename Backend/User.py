import Backend.InstanceUser
class User:
    def __init__(self,name,lastname,email,user_name,password,user_phone):
        self._name = name
        self._lastname = lastname
        self._email = email
        self._username = user_name
        self._password = password
        self._userphone = user_phone
        self._role = "User"
        self.__reservation = []
        self.__reserved = []
        # self.__canceled = []
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
        self.__reservation.append(reservation.get_reservation_details())
        return "add reservation to user"
    
    def get_reservation(self,reservation_id):
        for reservation in self.__reservation:
            if reservation_id == reservation.id:
                return reservation
        return "Not found"
    
    def add_reserved(self,room_reserved):
        self.__reserved.append(room_reserved)
        return "success"
    
    def set_Role(self,role):
        self._role = role
        return "success"

    @property
    def Role(self):
        return self._role
    
    @property
    def reservation(self):
        return self.__reservation
    @property
    def reserved(self):
        return self.__reserved
    
# def create_user(user_list):
#     for key,value in Backend.InstanceUser.user_info.items() :
#         new_user = User(name=Backend.InstanceUser.user_info[key]["name"],
#                         lastname=Backend.InstanceUser.user_info[key]["last name"],
#                         email=Backend.InstanceUser.user_info[key]["email"],
#                         user_name=Backend.InstanceUser.user_info[key]["username"],
#                         password=Backend.InstanceUser.user_info[key]["password"],
#                         user_phone=Backend.InstanceUser.user_info[key]["user_phone"])
        
#         user_list.append(new_user) #add new_user แต่ละตัวเข้า user_list
