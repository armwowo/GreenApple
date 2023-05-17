from Backend.Payment import *
from Backend.RoomReserved import RoomReserved
from Backend.User import User
from datetime import timedelta, date

class Reservation():
    reservation_id = 1000
    def __init__(self, user,check_in,check_out,room,dorm):#dor_name,room_id):
        type(self).reservation_id += 1
        self.__id = type(self).reservation_id
        self.__user = user
        self.__check_in = check_in
        self.__check_out = check_out
        self.__dorm_name = dorm
        self.__room = room
        self.__payment = None
        self.__payment_status = False

    @property
    def user(self):
        return self.__user
    @property
    def check_in(self):
        return self.__check_in
    @property
    def check_out(self):
        return self.__check_out
    @property
    def dor_name(self):
        return self.__dorm_name
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
    def payment_status(self):
        return self.__payment_status
    @property
    def id(self):
        return self.__id
    
    @property
    def info(self):
        return str([{"reservation id" :self.id,
                     "email":self.__user.email,
                     "dormitory":self.dor_name.name,
                     "room id":self.__room.room_id,
                     "check-in-date":self.__check_in.strftime("%d-"+"%b-"+"%Y"), "check-out-date":self.__check_out.strftime("%d-"+"%b-"+"%Y"),
                     "payment status":self.__payment_status}])

    def create_creditpayment(self,card_name,card_number):#หลังจากจองห้องเสร็จ
        self.__payment = CreditPayment(card_name,card_number)
        self.room.set_room_status(False)
        self.__payment_status = True
        return str([{"payment status":self.__payment_status}])