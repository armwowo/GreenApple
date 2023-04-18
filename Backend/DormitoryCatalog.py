from Backend.Facility import Facility
from Backend.Dormitory import Dormitory


class DormitoryCatalog:
    def __init__(self):
        self.__boost_dormity = []
        self.__Dormitory_listmain = []
    def check_facility():
        pass
    def save_to_dormitory_list():
        pass
    def check_price(self,max_price):
        pass
    def create_dormitory(self,dor_name,address,detail,phone,electric,warter,sevice_fee,internet,dormitory_picture,term_of_service):
        dormitory = Dormitory(self,dor_name,address,detail,phone,electric,warter,sevice_fee,internet,dormitory_picture,term_of_service)
        self.__Dormitory_listmain.append(dormitory)
        return dormitory

    def get_dormitory_list(self,dor_name):
        pass
    def add_dormitory_main(self, dormitory):
        self.__Dormitory_listmain.append(dormitory)


    def view_detail_dormitory(self,dormitory_name):
        dict = {}
        for dor in self.__Dormitory_listmain:
            if (dormitory_name == dor.get__dor_name()):
                dict.update( { "name":dor.get__dor_name(),
                "address":dor.get__address(),
                "detail": dor.get__detail(),
                "phone":dor.get__phone(),
                "electric":dor.get__electric(),
                "water":dor.get__water(),
                "service_fee":dor.get__service_fee(),
                "internet":dor.get__internet(),
                "dormitory picture":dor.get__dormitory_picture(),
                "term of service":dor.get__term_of_service(),
                "owner name":dor.get__owner_name(),
                "review": dor.get__review(),
                "facility": dor.get_facility(),
                "room list": dor.get_roomlist()})
        return dict

    def search_fac_dor(self,facility):
        temp_list = []
        for dormitory in self.__Dormitory_listmain:
            if dormitory.search_fac(facility) == True:
                temp_list.append(dormitory.get_dor_name())
            else :pass   
        return temp_list
    def search_maxmin_price(self,minp,maxp):
        temp_list = []
        for dormitory in self.__Dormitory_listmain:
            if ((minp <=min(dormitory.get_room_rental_list()) and min(dormitory.get_room_rental_list())<=maxp ) or 
                (maxp >= max(dormitory.get_room_rental_list()) and minp <= max(dormitory.get_room_rental_list()))):
                temp_list.append(dormitory.get__dor_name())
            else :pass
        return temp_list
    
    def search_dor_name(self,dor_name):
        temp_list = []
        for dormitory in self.__Dormitory_listmain:
            if dormitory.get__dor_name() == dor_name:
                temp_list.append(dormitory.get__dor_name())
            else :pass   
        return temp_list
            
    def get_dormitory_listmain(self):
        return self.__Dormitory_listmain
