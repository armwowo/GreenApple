from Backend.Facility import Facility
from Backend.Dormitory import Dormitory
from Backend.DormitoryCatalog import DormitoryCatalog
from Backend.AccountList import AccountList
from Backend.User import User
from Backend.Reservation import Reservation
from Backend.Room import Room

'''jia_jia.add_facility(1,1,1,1,1,1,1,1,1,1,1,1,1,1,0)
sabaiplace.add_facility(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
boomboom_place.add_facility(0,1,1,1,1,1,1,1,1,1,1,1,1,1,0)
jia_jia.add_roomlist(101,6500,1,"")
jia_jia.add_roomlist(102,6500,0,"")
jia_jia.add_roomlist(103,5000,1,"")
jia_jia.add_roomlist(104,5000,0,"")
jia_jia.add_roomlist(105,5000,0,"")
sabaiplace.add_roomlist(1101,3000,0,"")
sabaiplace.add_roomlist(1102,8000,1,"") 
sabaiplace.add_roomlist(1103,8000,0,"")
boomboom_place.add_roomlist(1001,7000,0,"")
boomboom_place.add_roomlist(1002,5000,0,"")
boomboom_place.add_roomlist(1003,5000,1,"")
print(jia_jia.get_room_list_id())'''

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
arm = User("arm","vor","vorarm23@gmail.com","arm","12345","0929349512")
ball = User("ball","watchanon","dragonball@gmail.com","balllnwza","dragonball123","0839456376")
oak = User("oak","chatlaong","kingoak11@gmail.com","oakoak22","oak08293242","0828944245")
account_list.add_account(arm)
account_list.add_account(ball)
account_list.add_account(oak)

room1 = Room(101,6500,room_status=1)
room2 = Room(102,6500,room_status=0)
room3 = Room(103,6500,room_status=1)

jia_jia._Roomlist.add_room(room1)
jia_jia._Roomlist.add_room(room2)
jia_jia._Roomlist.add_room(room3)

# print(account_list.check_user("arm","12345"))

#print(jia_jia._Roomlist.check_room_status())
#print(dormcat.cancel_dormitory(jia_jia))
#print(dormcat.get_dormitory_list())
#print(dormcat.cancel_dormitory(jia_jia))
#print(dormcat.get_dormitory_list())