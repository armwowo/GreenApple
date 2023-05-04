from Backend.Facility import Facility
from Backend.RoomCatalog import RoomCatalog
from Backend.Room import Room 

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

    @property
    def info(self):
        return str([{"name" :self.name,
                     "address":self.address,
                     "detail":self.detail,
                     "phone":self.phone}])

    @property
    def Roomlist(self):
        return self.__Roomlist
    @property
    def name(self):
        return self.__dor_name
    @property
    def detail(self):
        return self.__detail
    @property
    def address(self):
        return self.__address
    @property
    def phone(self):
        return self.__phone
    
    #def add_roomlist(self,roomlist):
        #self._Roomlist = roomlist

    def add_facility(self,pets,ev_charger,salon,laudry,store,restaurant,security,cctv,finger_print,keycard,fitness,pool,lift,parking,smoking):
        self.__Fac = Facility(pets,ev_charger,salon,laudry,store,restaurant,security,cctv,finger_print,keycard,fitness,pool,lift,parking,smoking)


    # def search_fac(self, facility):
    #     search = "self.Fac.get_" + facility + "()"
    #     return eval(search)
    
    def get_roomlist(self):
        return self.__Roomlist.get_room_list()
    def get_room_list_id (self):
        return self.__Roomlist.get_room_list_id()
    def get_room_rental_list(self):
        return self.__Roomlist.get_room_rental_list()
    
    def search_fac(self, facility):#พารามิเตอร์เป็น facility ทั้งหมด
        # search = Dormitory.get_facility(self)
        search = self.__Fac
        # search = "self.__Fac.get_" + facility + "()"
        for i in range(15):
            if facility[i] == 1 and search.list_facilities[i] ==1 :
                # print("1")
                pass
            elif facility[i] ==1 and search.list_facilities[i] ==0:
                return False
        return True
    
    def add_review(self,review):
        self.__review.append(review)
