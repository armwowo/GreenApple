from Facility import Facility
from Dormitory import Dormitory

class DormitoryCatalog:
    def __init__(self):
        self.__boost_dormity = []
        self.__Dormitory_list = []
        self.__Dormitory_listmain = []
    def check_facility():
        pass
    def save_to_dormitory_list():
        pass
    def check_price(self,max_price):
        pass
    def create_dormitory(self,name,address,detail,phone,electric,warter,sevice_fee,internet,dorm_picture,term_of_service):
        pass
    def get_dormitory_list(self,name_dor):
        pass
    def add_dormitory_main(self, dormitory):
        self.__Dormitory_listmain.append(dormitory)

    def add_dormitory(self, dormitory):
        self.__Dormitory_list.append(dormitory.get__dor_name())

    def search_fac_dor(self,facility):
        self.__Dormitory_list = []
        for dormitory in self.__Dormitory_listmain:
            if dormitory.search_fac(facility) == True:
                self.add_dormitory(dormitory)
            else :pass
        return self.__Dormitory_list
    def search_maxmin_price(self,minp,maxp):
        self.__Dormitory_list = []
        for dormitory in self.__Dormitory_listmain:
            if (minp <=min(dormitory.get_room_rental_list()) or maxp >= max(dormitory.get_room_rental_list())):
                self.add_dormitory(dormitory)
            else :pass
        return self.__Dormitory_list
    
    def search_dor_name(self,dor_name):
        temp_list = []
        for dormitory in self.__Dormitory_listmain:
            if dormitory.get__dor_name() == dor_name:
                temp_list.append(dormitory.get__dor_name())
            else :pass   
        return temp_list
            
    def get_dormitory_listmain(self):
        return self.__Dormitory_listmain
