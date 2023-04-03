from Facility import Facility
from Dormitory import Dormitory
from DormitoryCatalog import DormitoryCatalog

jia_jia = Dormitory("jia_jia","soi hormai","","0828932414",8,18,100,False,"","","Arm",1,1,1,1,1,1,1,1,1,1,1,1,1,1,0)
sabaiplace = Dormitory("sabaiplace","Vcon","","4905293028",8,18,9,"","",100,"ball",1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
boomboom_place = Dormitory("boomboom_place","soi yigyig","","0626250119",8,18,100,False,"","","Tren",0,1,1,1,1,1,1,1,1,1,1,1,1,1,0)


Dorcat = DormitoryCatalog()
Dorcat.add_dormitory_main(jia_jia)
Dorcat.add_dormitory_main(sabaiplace)
Dorcat.add_dormitory_main(boomboom_place)
print(Dorcat.search_dor_name("dgdf"))