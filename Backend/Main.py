from Backend.Facility import Facility
from Backend.Dormitory import Dormitory
from Backend.DormitoryCatalog import *
from Backend.User import User
from Backend.Reservation import Reservation
from Backend.Owner import Owner



# guygy = Owner("guy","gy","guy@gmail.com","guy123","132254","0987654321")
# account_list.add_account(guygy)


sabaiplace = Dormitory("Sabaiplace","ถ.ฉลองกรุง ลำปลาทิว ลาดกระบัง กรุงเทพมหานคร","","0993429897",8,18,9,"","",100,"ball")
sabaiplace.add_facility(1,1,1,1,1,1,1,1,1,1,1,0,0,1,1)
sabaiplace.add_roomlist(1101,4500,0,"")
sabaiplace.add_roomlist(1102,4500,1,"") 
sabaiplace.add_roomlist(1103,4500,0,"")

# print(jia_jia.get_room_list_id())


Dorcat = DormitoryCatalog()
Dorcat.add_dormitory_main(sabaiplace)

#test add_dormitory by Owner
# ju_ju = Dorcat.create_dormitory("ju_ju","soi hormai","","0828932414",8,18,100,False,"","","guy123")
# ju_ju.add_facility(0,0,0,0,0,1,1,1,1,0,1,0,0,0,0)
list = Dorcat.get_dormitory_listmain()
for i in list :
    print(i.get__dor_name())

#test search by facilities 
print(Dorcat.search_fac_dor([0,0,0,0,0,1,0,1,0,0,0,0,1,0,0]))
#print(Dorcat.search_fac_dor("parking"))

#test search by price 
# print(Dorcat.search_maxmin_price(3000,4000))

#test search by names    return dormitory names
# print(Dorcat.search_dor_name(boomboom_place.get__dor_name()))

arm = User("arm","vor","vorarm23@gmail.com","armvor00","armmee999","0929349512")
ball = User("ball","watchanon","dragonball@gmail.com","balllnwza","dragonball123","0839456376")
oak = User("oak","chatlaong","kingoak11@gmail.com","oakoak22","oak08293242","0828944245")
account_list.add_account(arm)


account_list.add_account(oak)


#check reservation
# Oakaccount = account_list.find_data_user("oakoak22")
# print(oak.reservation)
# print(oak.reservation)

## #test use case register
# print(account_list.register("ball","watchanon","dragonball@gmail.com","balllnwza","dragonball123","0839456376","User"))
# print(account_list.register("oodddak","chat","kingoak11@kmitl.ac.th","oak000","oak08293242","0828944245","Owner"))
# oak = account_list.find_data_user("balllnwza")
# print(oak.Role)
# print(account_list.register("oak","chatlaong","kingoak1@gmail.com","oakoak22","oak08293242","0828944245"))
# print(account_list.register("arm","vor","vorarm23@gmail.com","armvor00","armmee999","0929349512"))

# print(account_list.list_user_name())

#test use case login
# print(account_list.check_user("oak","oak08293242"))
# print(account_list.find_data_user("oak"))


#test view details dormitory
# print(Dorcat.view_detail_dormitory(jia_jia.get__dor_name()))