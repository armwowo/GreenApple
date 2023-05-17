from Backend.Reservation import Reservation

class Room:
    def __init__(self,room_id,room_rental):
        self.__room_id = room_id
        self.__room_rental = room_rental
        self.__room_status = True
        self.__reservation = []

    @property
    def room_id(self):
        return self.__room_id
    
    @property
    def room_status(self):
        return self.__room_status
    
    @property
    def reservation(self):
        return self.__reservation
    
    @property
    def room_rental(self):
        return self.__room_rental
    
    @property
    def check_out(self):
        n = -1
        for i in self.reservation:
            n += 1        
        if n >= 0 and self.room_status == False and self.reservation[n].payment_status == True:
            return self.reservation[n].check_out.strftime("%d-"+"%b-"+"%Y")
        return None
    
    def latest_reservation(self):
        n = -1
        for i in self.reservation:
            n += 1        
        if n >= 0:
            return self.reservation[n]
        return None
    
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

    @property
    def info(self):
        reservation_details = [{"room_id" : self.room_id,
                                "room_rental" : self.room_rental,
                                "room_status":self.__room_status,
                                "check out" : self.check_out }]
        return str(reservation_details)