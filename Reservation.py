from Room import Room

class Reservation(Room):
    def __init__(self,check_in,reservation_detail,calendar,room_id,room_rental,room_status,room_fac):
        Room.__init__(self,room_id,room_rental,room_status,room_fac)
        self.__check_in = check_in
        self.__reservation_detail = reservation_detail
        self.__calendar = calendar
    def get_detail_payment():
        pass
