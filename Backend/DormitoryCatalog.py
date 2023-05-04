from Backend.Facility import Facility
from Backend.Dormitory import Dormitory

class DormitoryCatalog:
    def __init__(self):
        self.__boost_dormity = []
        self.__Dormitory_listmain = []
    
    @property
    def dormitory_listmain(self):
        return self.__Dormitory_listmain
    # def create_dormitory(self,dor_name,address,detail,phone,electric,warter,sevice_fee,internet,dormitory_picture,term_of_service,ownername):
    #     user = account_list.find_data_user(ownername)
    #     if(user):
    #         if user.Role == "Owner" and user.verified == True:
    #             for dor_in_list in self.__Dormitory_listmain:
    #                 if dor_in_list.get__dor_name() ==dor_name and dor_in_list.get__address() == address:
    #                     return "have this dormitory in database"
    #             dormitory = Dormitory(dor_name,address,detail,phone,electric,warter,sevice_fee,internet,dormitory_picture,term_of_service,ownername)
    #             self.add_dormitory_main(dormitory)
    #             return dormitory
    #         else: 
    #             return "not owner"
    #     else:
    #         return "username not found"
    def get_dormitory_list(self):#return ชื่อหอ
        temp_list = []
        for dorm in self.__Dormitory_listmain:
            temp_list.append(dorm.name)
        return temp_list
    
    def find_dormitory(self,name):#ค้นหาหอ
        for dorm in self.__Dormitory_listmain:
            # print (dorm.get__dor_name())
            if name == dorm.name:
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
        for dormitory in self.__Dormitory_listmain:
            if ((minp <=min(dormitory.get_room_rental_list()) and min(dormitory.get_room_rental_list())<=maxp ) or 
                (maxp >= max(dormitory.get_room_rental_list()) and minp <= max(dormitory.get_room_rental_list()))):
                temp_list.append(dormitory.name)
            else :pass
        if(temp_list == []) : return "Not Found"
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
        # if dor_name != None:
        #     return self.search_dor_name(dor_name)
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