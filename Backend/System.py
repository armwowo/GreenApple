from Backend.Reservation import Reservation
from Backend.DormitoryCatalog import DormitoryCatalog
from Backend.Payment import *
from datetime import timedelta, datetime

class System:
    def __init__(self,accountlist,dormcat):
        self.__reservation = []
        self.__accountlist = accountlist
        self.__dormcat = dormcat

    @property
    def dormcat(self):
        return self.__dormcat
    @property
    def accountlist(self):
        return self.__accountlist
    @property
    def reservation(self):
        return self.__reservation

    def create_reservation(self,email,check_in_date,check_out_date,dorm_name,room_id):#dor_name,room_id):#func การจองห้อง
        user = self.__accountlist.find_email(email)
        if user == False:
            return "user not found"
        dorm = self.__dormcat.find_dormitory(dorm_name)
        if dorm == False:
            return "dormitory not found"
        room = dorm.Roomlist.find_room(room_id)
        if room == False:
            return "room not found"
        
        check_in = datetime.strptime(check_in_date,'%d/%m/%Y')
        check_out = datetime.strptime(check_out_date,'%d/%m/%Y')
        if check_in > check_out:
            return "invalid checkout"
        if room.room_status == True:
            reservation = Reservation(user,check_in,check_out,room,dorm)
        elif room.room_status == False:
            if check_in < room.latest_reservation().check_out:
                return "room not available"
            elif check_in >= room.latest_reservation().check_out:
                reservation = Reservation(user,check_in,check_out,room,dorm)
        user.reservation.append(reservation)
        room.reservation.append(reservation)
        self.__reservation.append(reservation)
        return reservation.info
    
    def cancel_reservation(self,email,dorm_name,room_id,reservation_id):
        user = self.__accountlist.find_email(email)
        if user == False:
            return "user not found"
        dorm = self.__dormcat.find_dormitory(dorm_name)
        if dorm == False:
            return "dormitory not found"
        room = dorm.Roomlist.find_room(room_id)
        if room == False:
            return "room not found"        
        for reservation in room.reservation:
            if reservation.id == reservation_id:
                user.reservation.remove(reservation)
                room.reservation.remove(reservation)
                self.__reservation.remove(reservation)
                room.set_room_status(True)
                return "cancel reservation"
        else:return "not found reservation"
        
    def add_room_reserved(self):
        pass
    
    def find_user(self,name):#ค้นหาหอ
        for user in self.__accountlist:
            if name == user.name:
                return user
        return "Not found"
    
    def find_room(self):
        pass