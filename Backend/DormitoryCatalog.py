from Backend.Facility import Facility
from Backend.Dormitory import Dormitory

class DormitoryCatalog:
    def __init__(self):
        self.__boost_dormity = []
        self._Dormitory_listmain = []
    def check_facility():
        pass
    def save_to_dormitory_list():
        pass
    def check_price(self,max_price):
        pass
    def create_dormitory(self,dor_name,address,detail,phone,electric,warter,sevice_fee,internet,dorm_picture,term_of_service):
        pass
    def get_dormitory_list(self):#return ชื่อหอ
        temp_list = []
        for dorm in self._Dormitory_listmain:
            temp_list.append(dorm.get__dor_name())
        return temp_list
    
    def add_dormitory_main(self, dormitory):
        self._Dormitory_listmain.append(dormitory)

    def view_detail_dormitory(self,dormitory_name):
        for dor in self._Dormitory_listmain:
            if (dormitory_name == dor.get__dor_name()):
               return dor
        return "Not found"

    def search_fac_dor(self,facility):
        temp_list = []
        for dormitory in self._Dormitory_listmain:
            if dormitory.search_fac(facility) == True:
                temp_list.append(dormitory.get_dor_name())
            else :pass   
        return temp_list
    def search_maxmin_price(self,minp,maxp):
        temp_list = []
        for dormitory in self._Dormitory_listmain:
            if (minp <=min(dormitory.get_room_rental_list()) or maxp >= max(dormitory.get_room_rental_list())):
                self.add_dormitory(dormitory)
            else :pass
        return temp_list
    
    def search_dor_name(self,dor_name):
        temp_list = []
        for dormitory in self._Dormitory_listmain:
            if dormitory.get__dor_name() == dor_name:
                temp_list.append(dormitory.get__dor_name())
            else :pass
        return temp_list
            
    def get_dormitory_listmain(self):
        return self._Dormitory_listmain
    
    def cancel_dormitory(self,name):
        for dormitory in self._Dormitory_listmain:
            if dormitory.get__dor_name() == name:
                self._Dormitory_listmain.remove(dormitory)
                return "Dormitory has been removed."
        
        return "Not found."