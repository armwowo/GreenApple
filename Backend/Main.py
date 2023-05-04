from Backend.Facility import Facility
from Backend.Dormitory import Dormitory
from Backend.DormitoryCatalog import DormitoryCatalog
from Backend.AccountList import AccountList
from Backend.User import User
from Backend.Reservation import Reservation
from Backend.Room import Room
from Backend.System import System
from datetime import date

jia_jia = Dormitory("jia_jia","soi hormai","","0828932414",8,18,100,False,"","","Arm")
sabaiplace = Dormitory("sabaiplace","Vcon","","4905293028",8,18,9,"","",100,"ball")
boomboom_place = Dormitory("boomboom_place","soi yigyig","","0626250119",8,18,100,False,"","","Tren")

dormcat = DormitoryCatalog()
dormcat.add_dormitory_main(jia_jia)
dormcat.add_dormitory_main(sabaiplace)
dormcat.add_dormitory_main(boomboom_place)
# print(Dorcat.search_fac_dor("pets"))
# print(Dorcat.search_fac_dor("smoking"))
#print(Dorcat.search_maxmin_price(4000,6600))'''

account_list = AccountList()
system = System(account_list,dormcat)
arm = User("arm","vor","vorarm23@gmail.com","arm","12345","0929349512")
ball = User("ball","watchanon","dragonball@gmail.com","balllnwza","dragonball123","0839456376")
oak = User("oak","chatlaong","kingoak11@gmail.com","oakoak22","oak08293242","0828944245")
account_list.add_account(arm)
account_list.add_account(ball)
account_list.add_account(oak)

room1 = Room("101",6500)
room2 = Room("102",6000)
room3 = Room("103",6000)

room4 = Room("104",4000)
room5 = Room("105",4500)
room6 = Room("106",5000)

room7 = Room("107",6500)
room8 = Room("108",4000)
room9 = Room("109",5500)

jia_jia.Roomlist.add_room(room1)
jia_jia.Roomlist.add_room(room2)
jia_jia.Roomlist.add_room(room3)
sabaiplace.Roomlist.add_room(room4)
sabaiplace.Roomlist.add_room(room5)
sabaiplace.Roomlist.add_room(room6)
boomboom_place.Roomlist.add_room(room7)
boomboom_place.Roomlist.add_room(room8)
boomboom_place.Roomlist.add_room(room9)

# print(dormcat.find_dormitory(jia_jia))

jia_jia.add_facility(1,1,1,0,0,1,1,1,1,0,1,0,0,0,0)
boomboom_place.add_facility(1,0,0,0,0,1,1,1,1,0,1,0,0,0,0)
sabaiplace.add_facility(0,1,1,0,0,1,1,1,1,0,1,0,0,0,0)

# print(jia_jia.Roomlist.check_room_status())
# # print(jia_jia.get_room_rental_list())
# # print(dormcat.search_maxmin_price(4000,9000))
# # print(dormcat.search_dormitories(4000,8500,[1,1,1,0,0,1,1,1,1,0,1,0,0,0,0]))
# print(arm.reservation)
print(room1.room_status)
print(system.create_reservation("vorarm23@gmail.com","01/05/2023","jia_jia","101"))#สร้าง reservation
print(arm.reservation)
# print(room1.info)

# print(system.create_reservation("oak","01-05-66","jia_jia","102"))
# # # print(system.dormcat.find_dormitory("jia_jia").Roomlist.find_room("101"))
# # print(arm.get_reservation(1))
# # print(system.accountlist.find_user(arm).reservation)
# print(arm.get_reservation(1001))
print(arm.get_reservation(1001).create_creditpayment("armcard","0946"))#สร้าง instance payment + จ่ายเงิน + เปลี่ยน status

#  print(oak.get_reservation(2).create_creditpayment("armcard","0946"))

# print(arm.get_reservation(1001).create_creditpayment("armcard","0946").pay())#จ่ายเงิน

# # print(account_list.find_user("arm"))

# print(arm.get_reservation(1001).create_roomreserved())#สร้าง roomreserved และให้ add ไปที่ room ,roomไม่ว่าง
# print(room1.room_reserved.end)
# print(arm.info)

# print(ball.info)
# print(jia_jia.Roomlist.check_room_status())
# print(room1.room_reserved.room_id)

# print(system.accountlist.find_user("oak"))

# print(room1.create_reservation(arm,"01-05-66"))
# reservation1 = room1.get_reservation(1)

# print(reservation1.create_creditpayment("armcard","11045","2022-02-05","112"))


# print()

# date_entry = input('Enter a date in YYYY-MM-DD format')
# year, month, day = map(int, date_entry.split('-'))
# date1 = datetime.date(year, month, day)
# print(date1)
#print(jia_jia._Roomlist.check_room_status())
#print(dormcat.cancel_dormitory(jia_jia))
#print(dormcat.get_dormitory_list())
#print(dormcat.cancel_dormitory(jia_jia))
#print(dormcat.get_dormitory_list())