from Backend.Payment import *
from Backend.RoomReserved import RoomReserved
from Backend.User import User
from datetime import timedelta, date

class Reservation():
    reservation_id = 1000
    def __init__(self, user,check_in,room):#dor_name,room_id):
        type(self).reservation_id += 1
        self.__id = type(self).reservation_id
        self.__user = user
        # self.__email = email
        self.__check_in = check_in
        # self.__dor_name = dor_name
        # self.__room_id = room_id
        # self.__status = False
        self.__room_reserved = None
        self.__room = room
        self.__payment = None

    def get_detail_payment():
        pass

    def create_creditpayment(self,card_name,card_number):#หลังจากจองห้องเสร็จ
        self.__payment = CreditPayment(card_name,card_number)
        return self.__payment
    
    def create_roomreserved(self):#funcสร้างใบจองหลังจากจ่ายเงิน
        if(self.__payment.status):
            # self.__status = True
            date_end = self.__check_in + timedelta(days = 366)
            self.room.set_room_status(False)

            self.room_reserved = RoomReserved(self.check_in,date_end,self.room.room_id)

            self.room.add_room_reserved(self.room_reserved)
            self.user.reserved.append(self.room_reserved)
            return "create roomreserved"
        else: return "not paid"

    # def date_cal(self):
    #     self.check_in_date = date.split("-")
    #     year, month, day = [int(item) for item in self.check_in_date]
    #     d = date(year, month, day)

    
    @property
    def user(self):
        return self.__user
    @property
    def check_in(self):
        return self.__check_in
    @property
    def dor_name(self):
        return self.__dor_name
    @property
    def room_id(self):
        return self.__room_id
    @property
    def status(self):
        return self.__status
    @property
    def room(self):
        return self.__room
    @property
    def payment(self):
        return self.__payment
    @property
    def id(self):
        return self.__id
    
    @property
    def info(self):
        return str([{"reservation id" :self.id,
                     "name":self.__user.name,"room_id":self.__room.room_id,"check-in-date":self.__check_in}])
    # def __str__(self) -> str:
    #     return str([{"name" : self.__user.get_name()}])
    
    # def get_reservation_details(self):
    #     reservation_details = {"name": self.__name , 
    #                           "email" : self.__email , 
    #                           "phone_number" : self.__phone_number,
    #                           "room_id" : Room.room_id,
    #                           "room_rental" : Room.room_rental,
    #                            "check in" : self.__check_in  }
    #     return reservation_details
    