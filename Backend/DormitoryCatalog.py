from Backend.Facility import Facility
from Backend.Dormitory import Dormitory

class DormitoryCatalog:
    def __init__(self):
        self.__boost_dormity = []
        self.__Dormitory_listmain = []
    
    @property
    def dormitory_listmain(self):
        return self.__Dormitory_listmain

    def get_dormitory_list(self):#return ชื่อหอ
        temp_list = []
        for dorm in self.__Dormitory_listmain:
            temp_list.append(dorm.name)
        return temp_list
    
    def find_dormitory(self,name):#ค้นหาหอ
        for dorm in self.__Dormitory_listmain:
            if name.lower() == dorm.name.lower():
                return dorm
        return False
    
    def add_dormitory_main(self, dormitory):
        self.__Dormitory_listmain.append(dormitory)

    def search_fac_dor(self,facility):
        temp_list = []
        for dormitory in self.__Dormitory_listmain:
            if dormitory.search_fac(facility) == True:
                temp_list.append(dormitory.name)
            else :pass   
        return temp_list
    
    def search_maxmin_price(self,minp,maxp):
        temp_list = []
        id = 0
        for dormitory in self.__Dormitory_listmain:
            if ((minp <=min(dormitory.get_room_rental_list()) and min(dormitory.get_room_rental_list())<=maxp ) or 
                (maxp >= max(dormitory.get_room_rental_list()) and minp <= max(dormitory.get_room_rental_list()))):
                temp_list.append({"id":id,
                            "name":dormitory.name,
                            "address":dormitory.address,
                            "price":str(min(dormitory.get_room_rental_list()))+" - "+str(max(dormitory.get_room_rental_list()))
                            })
            else :pass
            id+=1
        if(temp_list == []) : return None
        return temp_list
    
    def search_dor_name(self,dor_name):
        temp_list = []
        for dormitory in self.__Dormitory_listmain:
            if dormitory.name == dor_name:
                temp_list.append(dormitory.name)
            else :pass
        if temp_list == []:
            return "Not Found"
        return temp_list
    
    def search_dormitories(self,minp,maxp,facility):
        temp_list = []
        for j in self.search_maxmin_price(minp,maxp):
            print(j)
            for k in self.search_fac_dor(facility):
                print(k)
                if j == k:
                    temp_list.append(j)
        return temp_list
    
    def cancel_dormitory(self,name):
        for dormitory in self.__Dormitory_listmain:
            if dormitory.name == name:
                self.__Dormitory_listmain.remove(dormitory)
                return "Dormitory has been removed."
        
        return "Not found."