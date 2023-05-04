from Backend.Reservation import Reservation
from Backend.DormitoryCatalog import DormitoryCatalog
from Backend.Payment import *
from datetime import timedelta, datetime

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

    def create_reservation(self,email,check_in_date,dorm_name,room_id):#dor_name,room_id):#func การจองห้อง
        user = self.__accountlist.find_email(email)
        if user == False:
            return "user not found"
        dorm = self.__dormcat.find_dormitory(dorm_name)
        if dorm == False:
            return "dormitory not found"
        room = dorm.Roomlist.find_room(room_id)
        if room == False:
            return "room not found"
        
        check_in = datetime.strptime(check_in_date,'%d/%m/%Y')
        check_out = check_in + timedelta(days = 366)
        if room.room_status == True:
            reservation = Reservation(user,check_in,room,dorm,check_out)
        else : return "room not available"
        user.reservation.append(reservation)
        room.reservation.append(reservation)
        self.__reservation.append(reservation)
        return reservation.info
    
    def cancel_reservation(self,email,dorm_name,room_id,reservation_id):
        user = self.__accountlist.find_email(email)
        if user == False:
            return "user not found"
        dorm = self.__dormcat.find_dormitory(dorm_name)
        if dorm == False:
            return "dormitory not found"
        room = dorm.Roomlist.find_room(room_id)
        if room == False:
            return "room not found"        
        for reservation in room.reservation:
            if reservation.id == reservation_id:
                user.reservation.remove(reservation)
                room.reservation.remove(reservation)
                self.__reservation.remove(reservation)
                room.set_room_status(True)
                return "cancel reservation"
        else:return "not found reservation"
        
    def add_room_reserved(self):
        pass
    
    def find_user(self,name):#ค้นหาหอ
        for user in self.__accountlist:
            if name == user.name:
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