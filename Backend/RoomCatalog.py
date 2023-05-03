from Backend.Room import Room

class RoomCatalog():
    
    def __init__(self):
        #self.__Room = classRoom
        self.__room_list = []
    @property
    def room_list(self):
        return self.__room_list
    def get_room_rental_list(self):
        rental_list = []
        for room in self.__room_list:
            rental_list.append(room.get_room_rental())
        return rental_list
    
    def get_room_status_list(self):
        pass
    
    def add_room(self,room):
        self.__room_list.append(room)

    def edit_room(self,room_id,room_rental,room_status,room_fac):
        self.__room_list.room_id = room_id
        self.__room_list.room_rental = room_rental
        self.__room_list.room_status = room_status
        self.__room_list.room_fac = room_fac

    def get_room_list_id(self):
        list_id = []
        for id in self.__room_list:
            list_id.append(id.get_room_id())
        return list_id
    def save_to_room_list(self):
        pass

    def check_room_status(self):#แสดงห้องว่างพร้อมเช่า
        available_room = []
        for room in self.__room_list:
            if room.get_room_status() == 1:
                available_room.append(room)
        return available_room

    def find_room(self,room_id):#ค้นหาหอ
        for room in self.__room_list:
            if room_id == room.get_room_id():
                return room
        return "Not found"

    #def add_room สำหรับupdateเผิ่อมีห้องเพิ่ม 