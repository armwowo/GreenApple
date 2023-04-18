from Backend.Facility import Facility
from Backend.Dormitory import Dormitory
from Backend.DormitoryCatalog import DormitoryCatalog
from Backend.AccountList import AccountList
from Backend.User import User
from Backend.Reservation import Reservation



jia_jia = Dormitory("jia_jia","soi hormai","","0828932414",8,18,100,False,"","","Arm")
sabaiplace = Dormitory("sabaiplace","Vcon","","4905293028",8,18,9,"","",100,"ball")
boomboom_place = Dormitory("boomboom_place","soi yigyig","","0626250119",8,18,100,False,"","","Tren")
enjoyplaces = Dormitory("enjoyplaces","soi black dormitory","enjoyplace jaifdjaipejfjpwoer","070000000",8,18,150," - ","",100,"Oak")
jia_jia.add_facility(1,1,1,1,1,1,1,1,1,1,1,1,1,1,0)
sabaiplace.add_facility(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
boomboom_place.add_facility(0,1,1,1,1,1,1,1,1,1,1,1,1,1,0)
enjoyplaces.add_facility(0,0,0,0,0,0,1,1,0,1,0,0,0,1,0)
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
enjoyplaces.add_roomlist(111,4800,0,"1 Air conditioner , 1 Fan, 1 wardrobe,1 bed 5 feet , 1 table,3 chairs, 25 square meter")
enjoyplaces.add_roomlist(112,4800,0,"1 Air conditioner , 1 Fan, 1 wardrobe,1 bed 5 feet , 1 table,3 chairs, 25 square meter")
enjoyplaces.add_roomlist(113,4500,0,"1 Air conditioner , 1 Fan, 1 wardrobe,1 bed 5 feet , 1 table,3 chairs, 22 square meter")
enjoyplaces.add_roomlist(114,4500,0,"1 Air conditioner , 1 Fan, 1 wardrobe,1 bed 5 feet , 1 table,3 chairs, 22 square meter")
enjoyplaces.add_roomlist(115,4500,0,"1 Air conditioner , 1 Fan, 1 wardrobe,1 bed 5 feet , 1 table,3 chairs, 22 square meter")

# print(jia_jia.get_room_list_id())


Dorcat = DormitoryCatalog()
Dorcat.add_dormitory_main(jia_jia)
Dorcat.add_dormitory_main(sabaiplace)
Dorcat.add_dormitory_main(boomboom_place)
Dorcat.add_dormitory_main(enjoyplaces)

#test search by facilities 
# print(Dorcat.search_fac_dor("pets"))
# print(Dorcat.search_fac_dor("parking"))

#test search by price 
# print(Dorcat.search_maxmin_price(3000,4000))

#test search by names    return dormitory names
# print(Dorcat.search_dor_name(boomboom_place.get__dor_name()))


account_list = AccountList()

arm = User("arm","vor","vorarm23@gmail.com","armvor00","armmee999","0929349512")
ball = User("ball","watchanon","dragonball@gmail.com","balllnwza","dragonball123","0839456376")
oak = User("oak","chatlaong","kingoak11@gmail.com","oakoak22","oak08293242","0828944245")
account_list.add_account(arm)

Oreservation = Reservation("12-12-2566","oak",oak.get_email(),oak.get_userphone(),jia_jia.get__dor_name(),1101,6500,True,None)
account_list.add_account(oak)

oak.add_reservation(Oreservation)
Oreservation.create_payment(6500,"oak","kingoak11@gmail.com","0828983456")

Oreservation.create_room_reserved("11-11-2566","11-11-2567",1101,6500,True,None)


#check reservation
Oakaccount = account_list.find_data_user("oakoak22")
print(oak.reservation)
#print(oak.reservation)

#test use case register
# print(account_list.register("ball","watchanon","dragonball@gmail.com","balllnwza","dragonball123","0839456376"))
# print(account_list.register("oodddak","chat","kingoak11@kmitl.ac.th","oak000","oak08293242","0828944245"))
# print(account_list.register("oak","chatlaong","kingoak1@gmail.com","oakoak22","oak08293242","0828944245"))
# print(account_list.register("arm","vor","vorarm23@gmail.com","armvor00","armmee999","0929349512"))

print(account_list.list_user_name())

#test use case login
# print(account_list.check_user("oak","oak08293242"))
# print(account_list.find_data_user("oak"))


#test view details dormitory
# print(Dorcat.view_detail_dormitory(jia_jia.get__dor_name()))