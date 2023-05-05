class Room:
    def __init__(self,room_id,room_rental,room_status,room_fac):
        self.__room_id = room_id
        self.__room_rental = room_rental
        self.__room_status = room_status
        self.__room_fac = room_fac
        self.__reservation = []

    def get_name_dormitory():
        pass
    
    @property
    def reservation(self):
        return self.__reservation
    @property
    def room_id(self):
        return self.__room_id
    @property
    def room_rental(self):
        return self.__room_rental
    
    def get_room_status(self):
        return self.__room_status

    def set_room_status(self,state):
        self.__room_status = state
        return self.__room_status
    
    def get_room_id(self):
        return self.__room_id
    
    def latest_reservation(self):
        n = -1
        for i in self.reservation:
            n += 1        
        if n >= 0:
            return self.reservation[n]
        return None