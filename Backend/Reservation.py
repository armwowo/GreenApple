from Backend.Room import Room
from Backend.Payment import Payment
from Backend.RoomReserved import RoomReserved

class Reservation(Room):
    def __init__(self,check_in,name,email,phone_number,Dor_name,room_id,room_rental,room_status,room_fac):
        Room.__init__(self,room_id,room_rental,room_status,room_fac)
        self.__check_in = check_in
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__dormitory_name  = Dor_name
        self.__payment = None
        Room.set_room_status(Room,False)

    def get_detail_payment():
        pass

    def create_payment(self,price,name,email,phone_number):
        self.__payment = Payment(price,name,email,phone_number)
        return "success"
    
    def create_room_reserved(self,date_reserved,end,room_id,room_rental,room_status,room_fac):
        if(self.__payment.payment_status):
            room_reserved = RoomReserved(date_reserved,end,room_id,room_rental,room_status,room_fac)
            return room_reserved
        else :return "You haven't paid yet"

    @property
    def check_in(self):
        return self.__check_in
    @property
    def name(self):
        return self.__name
    @property
    def email(self):
        return self.__email
    @property
    def phone_number(self):
        return self.__phone_number
    
    def get_reservation_details(self):
        reservation_details = {"name": self.__name , 
                              "email" : self.__email , 
                              "phone_number" : self.__phone_number,
                              "room_id" : self.room_id,
                              "room_rental" : self.room_rental,
                               "check_in" : self.__check_in  }
        return reservation_details
    # def create_room_reservation(self):
    #     reservation_detail = {"name": self.__name , 
    #                           "email" : self.__email , 
    #                           "phone_number" : self.__phone_number,
    #                           "room_id" : Room.room_id,
    #                           "room_rental" : Room.room_rental,
    #                            "check in" : self.__check_in  }
    #     Room.set_room_status(Room,False)
    #     return reservation_detail
        

