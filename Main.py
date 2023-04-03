from Facility import Facility
from Dormitory import Dormitory
from DormitoryCatalog import DormitoryCatalog
from AccountList import AccountList
from User import User,create_user

'''jia_jia = Dormitory("jia_jia","soi hormai","","0828932414",8,18,100,False,"","","Arm",1,1,1,1,1,1,1,1,1,1,1,1,1,1,0)
sabaiplace = Dormitory("sabaiplace","Vcon","","4905293028",8,18,9,"","",100,"ball",1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
boomboom_place = Dormitory("boomboom_place","soi yigyig","","0626250119",8,18,100,False,"","","Tren",0,1,1,1,1,1,1,1,1,1,1,1,1,1,0)



Dorcat = DormitoryCatalog()
Dorcat.add_dormitory_main(jia_jia)
Dorcat.add_dormitory_main(sabaiplace)
Dorcat.add_dormitory_main(boomboom_place)
print(Dorcat.search_fac_dor("pets"))
print(Dorcat.search_fac_dor("smoking"))'''

'''
arm = User("arm","vor","vorarm23@gmail.com","armvor00","armmee999","0929349512")
ball = User("ball","watchanon","dragonball@gmail.com","balllnwza","dragonball123","0839456376")
oak = User("oak","chatlaong","kingoak11@gmail.com","oakoak22","oak08293242","0828944245")

account_list.add_account(arm)
account_list.add_account(ball)
account_list.add_account(oak)'''


account_list = AccountList()
create_user(user_list = account_list._account)

print(account_list.check_user("tuplnwza2","tup00203294"))
