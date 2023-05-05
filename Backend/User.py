import Backend.InstanceUser
class User:
    # user_id = 0
    def __init__(self,name,lastname,email,user_name,password,user_phone):
        # type(self).user_id += 1
        # self.__id = type(self).user_id
        self.__name = name
        self.__lastname = lastname
        self.__email = email
        self.__username = user_name
        self.__password = password
        self.__userphone = user_phone
        self.__role = "User"
        self.__reservation = []
        # self.__reserved = []
        # self.__canceled = []

    @property
    def name(self):
        return self.__name
    @property
    def id(self):
        return self.__id
    
    @property
    def lastname(self):
        return self.__lastname
    
    @property
    def username(self):
        return self.__username
    
    @property
    def email(self):
        return self.__email
    
    @property
    def userphone(self):
        return self.__userphone
    
    @property
    def Role(self):
        return self.__role
    
    @property
    def reservation(self):
        return self.__reservation
    @property
    def reserved(self):
        return self.__reserved
    
    def reservation_info(self):
        temp_lst = []
        for i in self.reservation:
            temp_lst.append(i.info)
        return temp_lst
    
    @property
    def info(self):
        return str([{"name" :self.name,
                     "email":self.email,
                     "role":self.Role,
                     "reservation":self.reservation_info()}])
    
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def get_email(self):
        return self.__email
    
    def add_reservation(self,reservation):
        self.__reservation.append(reservation.get_reservation_details())
        return "add reservation to user"
    
    def get_reservation(self,reservation_id):
        for reservation in self.__reservation:
            if reservation_id == reservation.id:
                return reservation
        return False
    
    def add_reserved(self,room_reserved):
        self.__reserved.append(room_reserved)
        return "add room_reserved"
    
    def set_Role(self,role):
        self._role = role
        return "success"
    
# def create_user(user_list):
#     for key,value in Backend.InstanceUser.user_info.items() :
#         new_user = User(name=Backend.InstanceUser.user_info[key]["name"],
#                         lastname=Backend.InstanceUser.user_info[key]["last name"],
#                         email=Backend.InstanceUser.user_info[key]["email"],
#                         user_name=Backend.InstanceUser.user_info[key]["username"],
#                         password=Backend.InstanceUser.user_info[key]["password"],
#                         user_phone=Backend.InstanceUser.user_info[key]["user_phone"])
        
#         user_list.append(new_user) #add new_user แต่ละตัวเข้า user_list