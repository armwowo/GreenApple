from Backend.Room import Room
from Backend.Payment import Payment

class RoomReserved(Room):
    def __init__(self,date_reserved,end,room_id,room_rental,room_status,room_fac ):
        Room.__init__(self,room_id,room_rental,room_status,room_fac)
        self.__date_reserved = date_reserved
        self.__end  = end
    def get_reservation():
        pass
    
    def get_details_roomreserved(self):
        details = {"start reserved":self.__date_reserved,
                   "end reserved":self.__end,
                   "room id":self.__room_id}
        return details

    @property
    def end(self):
        return  self.__end