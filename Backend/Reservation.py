from Backend.Payment import *
from Backend.RoomReserved import RoomReserved
from Backend.User import User
from datetime import date

class Reservation():
    def __init__(self, name,check_in,room):#dor_name,room_id):
        self.__name = name
        # self.__email = email
        self.__check_in = check_in
        # self.__dor_name = dor_name
        # self.__room_id = room_id
        # self.__status = False
        self.__room = room
        self.__payment = None
        self.__id = 1

    def get_detail_payment():
        pass

    def create_creditpayment(self,card_name,card_number,card_expire,cvv):#หลังจากจองห้องเสร็จ
        self.__payment = CreditPayment(card_name,card_number,card_expire,cvv)
        return self.__payment
    
    def create_roomreserved(self):#func สร้างใบจองหลังจากจ่ายเงิน
        if(self.__payment.status):
            # self.__status = True
            date_end = self.check_in
            self.room.set_room_status(False)
            room_reserved = RoomReserved(self.check_in,date_end,self.room.room_id)
            return "create roomreserved"
        else: return "error"


    # def date_cal(self):
    #     self.check_in_date = date.split("-")
    #     year, month, day = [int(item) for item in self.check_in_date]
    #     d = date(year, month, day)

    
    @property
    def name(self):
        return self.__name
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
    
    # def get_reservation_details(self):
    #     reservation_details = {"name": self.__name , 
    #                           "email" : self.__email , 
    #                           "phone_number" : self.__phone_number,
    #                           "room_id" : Room.room_id,
    #                           "room_rental" : Room.room_rental,
    #                            "check in" : self.__check_in  }
    #     return reservation_details
    