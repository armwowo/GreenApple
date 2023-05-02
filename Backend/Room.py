from Backend.Reservation import Reservation

class Room:
    def __init__(self,room_id,room_rental):
        self.__room_id = room_id
        self.__room_rental = room_rental
        self.__room_status = True
        self.__room_fac = None
        # self.__reservation = []
        self.__room_reserve = None

    @property
    def room_id(self):
        return self.__room_id
    
    @property
    def room_status(self):
        return self.__room_status

    def get_name_dormitory(self):
        pass

    def get_room_id(self):
        return self.__room_id
    
    def get_room_rental(self):
        return self.__room_rental
    
    def get_room_status(self):
        return self.__room_status
    
    def set_room_status(self,state):
        self.__room_status = state
        return self.__room_status
    
    # def get_reservation(self,reservation_id):
    #     for reservation in self.__reservation:
    #         if reservation_id == reservation.id:
    #             return reservation
    #     return "Not found"
    
    def get_reservation_details(self):
        reservation_details = {"name": self.__name , 
                                "email" : self.__email , 
                                "phone_number" : self.__phone_number,
                                "room_id" : Room.room_id,
                                "room_rental" : Room.room_rental,
                                "check in" : self.__check_in  }
        return reservation_details