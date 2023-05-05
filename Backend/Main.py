from Backend.Facility import Facility
from Backend.Dormitory import Dormitory
from Backend.DormitoryCatalog import DormitoryCatalog
from Backend.AccountList import AccountList
from Backend.User import User
from Backend.Reservation import Reservation
from Backend.Room import Room
from Backend.System import System
from datetime import date

sabaiplace = Dormitory("Sabaiplace","ถ.ฉลองกรุง ลำปลาทิว ลาดกระบัง กรุงเทพมหานคร","","0993429897",8,18,9,"","",100,"ball")
bankum = Dormitory("Bankhumkaow48","ซ.48 ถ.คุ้มเกล้า ลำปลาทิว ลาดกระบัง กรุงเทพมหานคร","","0897981157",7,18,7,"","","","apple")
applehouse = Dormitory("APPLEHOUSE","ซ.ฉลองกรุง 1 แยก 5 ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร","","0897981157",7,18,7,"","","","apple")
adcha = Dormitory("Adchariya","ซ.เกกีงาม 1 ถ.ฉลองกรุง 1 ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร","","0897981157",7,18,7,"","","","apple")
bbcourt = Dormitory("BBCourt","ซ.ฉลองกรุง 1 ถ.ฉลองกรุง ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร","","0897981157",7,18,7,"","","","apple")
aphouse = Dormitory("APHouse","ซ.เกกีงาม 1 ถ.ฉลองกรุง 1 ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร","","0897981157",7,18,7,"","","","apple")
buri = Dormitory("BuriIris","ซ.ฉลองกรุง 1 แยก 5 ถ.ฉลองกรุง ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร","","0897981157",7,18,7,"","","","apple")
allsmile = Dormitory("Allsmile","ถ.หลวงลาดกระบัง ทับยาว ลาดกระบัง กรุงเทพมหานคร","","0897981157",7,18,7,"","","","apple")
rimnam = Dormitory("Rimnam","ซ.ลาดกระบัง 13/5 ถ.อ่อนนุช-ลาดกระบัง ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร","","0897981157",7,18,7,"","","","apple")
nop = Dormitory("Noppakaow","ซ.ลาดกระบัง 52 แยก 6 ถ.ลาดกระบัง ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร","","0897981157",7,18,7,"","","","apple")

dormcat = DormitoryCatalog()
dormcat.add_dormitory_main(sabaiplace)
dormcat.add_dormitory_main(bankum)
dormcat.add_dormitory_main(adcha)
dormcat.add_dormitory_main(bbcourt)
dormcat.add_dormitory_main(aphouse)
dormcat.add_dormitory_main(buri)
dormcat.add_dormitory_main(applehouse)
dormcat.add_dormitory_main(allsmile)
dormcat.add_dormitory_main(rimnam)
dormcat.add_dormitory_main(nop)


sabaiplace1 = Room("104",4000)
sabaiplace2 = Room("105",4500)
sabaiplace3 = Room("106",5000)

bankum1 = Room("104",4000)
bankum2 = Room("105",4500)
bankum3 = Room("106",5000)

adcha1 = Room("104",4000)
adcha2 = Room("105",4500)
adcha3 = Room("106",5000)

bbcourt1 = Room("104",4000)
bbcourt2 = Room("105",4500)
bbcourt3 = Room("106",5000)

applehouse1 = Room("104",4000)
applehouse2 = Room("105",4500)
applehouse3 = Room("106",5000)

buri1 = Room("104",4000)
buri2 = Room("105",4500)
buri3 = Room("106",5000)

aphouse1 = Room("104",4000)
aphouse2 = Room("105",4500)
aphouse3 = Room("106",5000)

allsmile1 = Room("104",4000)
allsmile2 = Room("105",4500)
allsmile3 = Room("106",5000)

rimnam1 = Room("104",4000)
rimnam2 = Room("105",4500)
rimnam3 = Room("106",5000)

nop1 = Room("104",4000)
nop2 = Room("105",4500)
nop3 = Room("106",5000)

sabaiplace.Roomlist.add_room(sabaiplace1)
sabaiplace.Roomlist.add_room(sabaiplace2)
sabaiplace.Roomlist.add_room(sabaiplace3)

bankum.Roomlist.add_room(bankum1)
bankum.Roomlist.add_room(bankum2)
bankum.Roomlist.add_room(bankum3)

adcha.Roomlist.add_room(adcha1)
adcha.Roomlist.add_room(adcha2)
adcha.Roomlist.add_room(adcha3)

bbcourt.Roomlist.add_room(bbcourt1)
bbcourt.Roomlist.add_room(bbcourt2)
bbcourt.Roomlist.add_room(bbcourt3)

applehouse.Roomlist.add_room(applehouse1)
applehouse.Roomlist.add_room(applehouse2)
applehouse.Roomlist.add_room(applehouse3)

buri.Roomlist.add_room(buri1)
buri.Roomlist.add_room(buri2)
buri.Roomlist.add_room(buri3)

aphouse.Roomlist.add_room(aphouse1)
aphouse.Roomlist.add_room(aphouse2)
aphouse.Roomlist.add_room(aphouse3)

allsmile.Roomlist.add_room(allsmile1)
allsmile.Roomlist.add_room(allsmile2)
allsmile.Roomlist.add_room(allsmile3)

rimnam.Roomlist.add_room(rimnam1)
rimnam.Roomlist.add_room(rimnam2)
rimnam.Roomlist.add_room(rimnam3)

nop.Roomlist.add_room(nop1)
nop.Roomlist.add_room(nop2)
nop.Roomlist.add_room(nop3)


sabaiplace.add_facility(1,1,1,1,1,1,1,1,1,1,1,0,0,1,1)
bankum.add_facility(0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)
applehouse.add_facility(0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)
adcha.add_facility(0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)
bbcourt.add_facility(0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)
aphouse.add_facility(0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)
buri.add_facility(0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)
allsmile.add_facility(0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)
rimnam.add_facility(0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)
nop.add_facility(0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)

account_list = AccountList()
system = System(account_list,dormcat)
arm = User("arm","vor","vorarm23@gmail.com","arm","12345","0929349512")
ball = User("ball","watchanon","dragonball@gmail.com","balllnwza","dragonball123","0839456376")
oak = User("oak","chatlaong","kingoak11@gmail.com","oakoak22","oak08293242","0828944245")
account_list.add_account(arm)
account_list.add_account(ball)
account_list.add_account(oak)

print(sabaiplace1.room_status)
print(system.create_reservation("vorarm23@gmail.com","01/05/2023","01/05/2024","sabaiplace","104"))#สร้าง reservation
print(arm.reservation)
print(system.dormcat)
print(arm.get_reservation(1001).create_creditpayment("armcard","0946"))#สร้าง instance payment + จ่ายเงิน + เปลี่ยน status