# from Backend.Room import Room

# class RoomReserved(Room):#ใบจอง
#     def __init__(self,date_reserved,end,room_id,room_rental,room_status,room_fac ):
#         Room.__init__(self,room_id,room_rental,room_status,room_fac)
#         self.__date_reserved = date_reserved
#         self.__end  = end

class RoomReserved():
    def __init__(self,date_reserved,end,room_id,dorm_name):
        self.__date_reserved = date_reserved
        self.__end  = end
        self.__room_id = room_id
        self.__dorm_name = dorm_name
        
    def get_reservation():
        pass
    
    @property    
    def info(self):
        details = {"check-in-date":self.__date_reserved.strftime("%d-"+"%b-"+"%Y"),
                   "check-out-date":self.__end.strftime("%d-"+"%b-"+"%Y"),
                   "dormitory":self.__dorm_name.name,
                   "room id":self.__room_id}
        return details

    @property
    def end(self):
        return  self.__end
    @property
    def room_id(self):
        return  self.__room_id