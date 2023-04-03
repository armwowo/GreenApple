from Facility import Facility
from RoomCatalog import RoomCatalog

class Dormitory():
    def __init__(self,dor_name,address,detail,phone,electric,water,service_fee,internet,dormitory_picture,term_of_service,owner_name):
        self.__dor_name = dor_name
        self.__address = address
        self.__detail = detail
        self.__phone = phone
        self.__electric = electric
        self.__water = water
        self.__service_fee = service_fee
        self.__internet = internet
        self.__dormitory_picture = dormitory_picture
        self.__term_of_service = term_of_service
        self.__owner_name = owner_name
        self.__review = []
        #self.Fac = Facility(1,1,1,1,1,1,1,1,1,1,1,1,1,1,0) #test
        self.__Fac  = None
        self.__Roomlist = RoomCatalog()


    def get__dor_name(self):
        return self.__dor_name
    
    def get__address(self):
        return self.__address
    
    def get__detail(self):
        return self.__detail
    
    def get__phone(self):
        return self.__phone
    
    def get__electric(self):
        return self.__electric
    
    def get__water(self):
        return self.__water
    
    def get__service_fee(self):
        return self.__service_fee
    
    def get__internet(self):
        return self.__internet
    
    def get__dormitory_picture(self):
        return self.__dormitory_picture
    
    def get__term_of_service(self):
        return self.__term_of_service
    
    def get__owner_name(self):
        return self.__owner_name
    
    def get__review(self):
        return self.__review 
       
    def find_facility(self,facility):
        pass

    def check_room_status(self,):
        pass

    def get_room_catalog(self,):
        pass

    def get_facility(self):
        return self.__Fac

    def check_rental(self,):
        pass

    def create_room(self,ID,type,status,rental,room_facility):
        pass
    def add_facility(self,pets,ev_charger,salon,laudry,store,restaurant,security,cctv,finger_print,keycard,fitness,pool,lift,parking,smoking):
        self.__Fac = Facility(pets,ev_charger,salon,laudry,store,restaurant,security,cctv,finger_print,keycard,fitness,pool,lift,parking,smoking)

    # def search_fac(self, facility):
    #     search = "self.Fac.get_" + facility + "()"
    #     return eval(search)
    
    def add_roomlist(self,room_id,room_rental,room_status,room_fac):
        self.__Roomlist.create_room(room_id,room_rental,room_status,room_fac)
    def get_roomlist(self):
        return self.__Roomlist.get_room_list()
    def get_room_list_id (self):
        return self.__Roomlist.get_room_list_id()
    def get_room_rental_list(self):
        return self.__Roomlist.get_room_rental_list()

    def search_fac(self, facility):
        search = Dormitory.get_facility(self)
        # search = "self.__Fac.get_" + facility + "()"
        return eval("search."+"get_"+facility+"()")