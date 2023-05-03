from Backend.Reservation import Reservation

class Room:
    def __init__(self,room_id,room_rental):
        self.__room_id = room_id
        self.__room_rental = room_rental
        self.__room_status = True
        self.__room_fac = None
        # self.__reservation = []
        self.__room_reserved = None

    @property
    def room_id(self):
        return self.__room_id
    
    @property
    def room_status(self):
        return self.__room_status
    
    @property
    def room_reserved(self):
        return self.__room_reserved
    @property
    def room_rental(self):
        return self.__room_rental
    
    def get_check_out(self):
        return self.__room_reserved.end

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
    
    def set_room_status(self,state):
        self.__room_status = state
        return self.__room_status
    
    def add_room_reserved(self,roomreserved):
        self.__room_reserved = roomreserved
    
    # def get_reservation(self,reservation_id):
    #     for reservation in self.__reservation:
    #         if reservation_id == reservation.id:
    #             return reservation
    #     return "Not found"
    @property
    def info(self):
        reservation_details = [{"room_id" : self.room_id,
                                "room_rental" : self.room_rental,
                                "room_status":self.__room_status,
                                "check out" : self.__room_reserved.end  }]
        return str(reservation_details)