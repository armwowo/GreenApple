from Backend.Reservation import Reservation
from Backend.DormitoryCatalog import DormitoryCatalog
from Backend.Payment import *
from datetime import datetime

class System:
    def __init__(self,accountlist,dormcat):
        self.__reservation = []
        self.__accountlist = accountlist
        self.__dormcat = dormcat

    
    # def get_reservation(self,reservation_id):
    #     for reservation in self.__reservation:
    #         if reservation_id == reservation.id:
    #             return reservation
    #     return "Not found"

    def create_reservation(self,name,check_in_date,dor_name,room_id):#dor_name,room_id):#func การจองห้อง
        user = self.__accountlist.find_user(name)
        dorm = self.__dormcat.find_dormitory(dor_name)
        room = dorm.Roomlist.find_room(room_id)
        check_in = datetime.strptime(check_in_date,'%d/%m/%Y')
        reservation = Reservation(user,check_in,room)#dor_name,room_id)
        user.reservation.append(reservation)#add reservation in User
        self.__reservation.append(reservation)
        return reservation.info
    
    def add_room_reserved(self):
        pass
    
    def find_user(self,name):#ค้นหาหอ
        for user in self._account:
            if name == user.get_name():
                return user
        return "Not found"
    def find_room(self):
        pass
    # def get_reservation(self):
    #     temp_list = []
    #     for reservation in self.__reservation:

    # def create_creditpayment(self,reservation_id,card_name,card_number,card_expire,cvv):#หลังจากจองห้องเสร็จ
    #     self.get_reservation(reservation_id).__payment = CreditPayment(card_name,card_number,card_expire,cvv)
    #     return self.get_reservation(reservation_id).__payment
    
    @property
    def dormcat(self):
        return self.__dormcat
    @property
    def accountlist(self):
        return self.__accountlist
    @property
    def reservation(self):
        return self.__reservation