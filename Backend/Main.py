from Backend.Facility import Facility
from Backend.Dormitory import Dormitory
from Backend.DormitoryCatalog import DormitoryCatalog
from Backend.AccountList import AccountList
from Backend.User import User
from Backend.Reservation import Reservation
from Backend.Room import Room
from Backend.System import System
from datetime import date

sabaiplace = Dormitory("Sabaiplace","ถ.ฉลองกรุง ลำปลาทิว ลาดกระบัง กรุงเทพมหานคร","ห้องเช่า สบายเพลส เป็น ห้องพักตั้งอยู่ที่ ซอย ฉลองกรุง 31/1 หน้านิคมอุตสาหกรรมลาดกระบัง ใกล้พระจอมเกล้าลาดกระบัง และ สนามบิน สุวรรณภูมิ เป็นที่พักในอุดมคติสำหรับคนทำงานที่ นิคมลาดกระบัง นักเรียน นักศึกษา เทคโน พระจอมเกล้าลาดกระบัง คนทำงานที่สนามบิน สุวรรณภูมิ","0993429897",8,18,9,"","",100,"ball")
bankum = Dormitory("Bankhumkaow48","ซ.48 ถ.คุ้มเกล้า ลำปลาทิว ลาดกระบัง กรุงเทพมหานคร","บ้านพักสไตล์รีสอร์ต ให้เช่ารายเดือน (สัญญา12เดือน) กว้าง4*ลึก6เมตร ขนาดห้อง24ตรม.(ไม่รวมระเบียง) มีระเบียงด้านหน้าบ้าน พร้อมที่จอดรถยนต์ส่วนตัว ด้านข้างมีหลังคา ภายในห้องมี แอร์1ตัว(13000BTU) ห้องน้ำในตัว เครื่องทำน้ำอุ่น อ่างล้างจาน ห้ามเลี้ยงสัตว์ในห้องพัก ห้ามสูบบุหรี่ในห้องพัก","0897981157",7,18,7,"","","","apple")
applehouse = Dormitory("APPLEHOUSE","ซ.ฉลองกรุง 1 แยก 5 ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร","ห้องพักราคาสบายกระเป๋า อยู่ใกล้ สถาบันเทคโนโลยีเจ้าคุณทหารลาดกระบังและสนามบินสุวรรณภูมิ เหมาะสำหรับนักศึกษา Free Cable TV ทุกห้องมากกว่า 100 ช่อง Free ที่จอดรถจักรยาน, มอเตอร์ไซค์ในร่มระบบรักษาความปลอดภัย เข้า - ออก ด้วยระบบ Keycard และกล้อง CCTV ทั่วบริเวณบันทึก 24 ชม.บริการร้านมินิมาร์ทในโครงการ อาหารตามสั่ง มีบริการเครื่องซักผ้า ทุกชั้น!! เฟอนิเจอร์ครบชุด ภายในห้องมีเตียงพร้อมฟูก ขนาด 5 ฟุต โต๊ะเขียนหนังสือพร้อมเก้าอี้ 2 ชุด แอร์ ผ้าม่าน มุ้งลวด ตู้เสื้อผ้า โต๊ะวาง TV โต๊ะเครื่องแป้งพร้อมเก้าอี้สามารถพักได้ 2 คน สบายๆ ราคาสบายกระเป๋า!!","0897981157",7,18,7,"","","","apple")
adcha = Dormitory("Adchariya","ซ.เกกีงาม 1 ถ.ฉลองกรุง 1 ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร","หอพักหญิง สะอาด ทันสมัย มีที่จอดรดจักรยานและมอเตอร์ไซด์ในร่ม ภายในรั้วอาคารติดคณะวิศวะ พระจอมเกล้า ลาดกระบัง ซอยแรกสามารถเดินไปเรียนได้ใน 5 นาทีห่างจากสนามบินสุวรรณภูมิ 15 นาที ความปลอดภัย ปลอดภัยด้วยกล้องวงจรปิดทุกชั้น รอบอาคารและที่จอดรถจักรยานยนต์ ผู้เช่าจอดมอเตอร์ไซด์ในร่ม ภายในรั้วฟรี ห้องละ 1 คัน รั้วรอบอาคาร เข้าออกอาคารด้วยแสกนนิ้ว ไมโครเวฟส่วนกลาง","0897981157",7,18,7,"","","","apple")
bbcourt = Dormitory("BBCourt","ซ.ฉลองกรุง 1 ถ.ฉลองกรุง ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร","รายละเอียด","0897981157",7,18,7,"","","","apple")
aphouse = Dormitory("APHouse","ซ.เกกีงาม 1 ถ.ฉลองกรุง 1 ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร","รายละเอียด","0897981157",7,18,7,"","","","apple")
buri = Dormitory("BuriIris","ซ.ฉลองกรุง 1 แยก 5 ถ.ฉลองกรุง ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร","รายละเอียด","0897981157",7,18,7,"","","","apple")
allsmile = Dormitory("Allsmile","ถ.หลวงลาดกระบัง ทับยาว ลาดกระบัง กรุงเทพมหานคร","รายละเอียด","0897981157",7,18,7,"","","","apple")
rimnam = Dormitory("Rimnam","ซ.ลาดกระบัง 13/5 ถ.อ่อนนุช-ลาดกระบัง ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร","รายละเอียด","0897981157",7,18,7,"","","","apple")
nop = Dormitory("Noppakaow","ซ.ลาดกระบัง 52 แยก 6 ถ.ลาดกระบัง ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร","รายละเอียด","0897981157",7,18,7,"","","","apple")

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


sabaiplace1 = Room("104",1000)
sabaiplace2 = Room("105",500)
sabaiplace3 = Room("106",500)

bankum1 = Room("104",6000)
bankum2 = Room("105",4500)
bankum3 = Room("106",8000)

adcha1 = Room("104",2000)
adcha2 = Room("105",4000)
adcha3 = Room("106",4000)

bbcourt1 = Room("104",1000)
bbcourt2 = Room("105",400)
bbcourt3 = Room("106",3000)

applehouse1 = Room("104",2000)
applehouse2 = Room("105",10000)
applehouse3 = Room("106",5000)

buri1 = Room("104",4000)
buri2 = Room("105",4500)
buri3 = Room("106",5000)

aphouse1 = Room("104",3000)
aphouse2 = Room("105",4500)
aphouse3 = Room("106",5000)

allsmile1 = Room("104",6000)
allsmile2 = Room("105",4500)
allsmile3 = Room("106",5000)

rimnam1 = Room("104",8000)
rimnam2 = Room("105",4500)
rimnam3 = Room("106",1000)

nop1 = Room("104",4000)
nop2 = Room("105",4500)
nop3 = Room("106",3000)

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