from Backend.Facility import Facility
from Backend.Dormitory import Dormitory
from Backend.DormitoryCatalog import DormitoryCatalog
from Backend.AccountList import AccountList
from Backend.User import User
from fastapi import FastAPI
from Backend.Room import Room
from Backend.RoomCatalog import RoomCatalog

jia_jia = Dormitory("jia_jia", "soi hormai", "",
                    "0828932414", 8, 18, 100, False, "", "", "Arm")
sabaiplace = Dormitory("sabaiplace", "Vcon", "",
                       "4905293028", 8, 18, 9, "", "", 100, "ball")
boomboom_place = Dormitory("boomboom_place", "soi yigyig",
                           "", "0626250119", 8, 18, 100, False, "", "", "Tren")
jia_jia.add_facility(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0)
sabaiplace.add_facility(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
boomboom_place.add_facility(0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0)
jia_jia.add_roomlist(101, 6500, 1, "")
jia_jia.add_roomlist(102, 6500, 0, "")
jia_jia.add_roomlist(103, 5000, 1, "")
jia_jia.add_roomlist(104, 5000, 0, "")
jia_jia.add_roomlist(105, 5000, 0, "")
sabaiplace.add_roomlist(1101, 3000, 0, "")
sabaiplace.add_roomlist(1102, 8000, 1, "")
sabaiplace.add_roomlist(1103, 8000, 0, "")
boomboom_place.add_roomlist(1001, 7000, 0, "")
boomboom_place.add_roomlist(1002, 5000, 0, "")
boomboom_place.add_roomlist(1003, 5000, 1, "")
# print(jia_jia.get_room_list_id())


Dorcat = DormitoryCatalog()
Dorcat.add_dormitory_main(jia_jia)
Dorcat.add_dormitory_main(sabaiplace)
Dorcat.add_dormitory_main(boomboom_place)
# print(Dorcat.search_fac_dor("pets"))
# print(Dorcat.search_fac_dor("smoking"))
# print(Dorcat.search_maxmin_price(4000,6600))

account_list = AccountList()
arm = User("arm", "vor", "vorarm23@gmail.com",
           "armvor00", "armmee999", "0929349512")
ball = User("ball", "watchanon", "dragonball@gmail.com",
            "balllnwza", "dragonball123", "0839456376")
oak = User("oak", "chatlaong", "kingoak11@gmail.com",
           "oakoak22", "oak08293242", "0828944245")

account_list.add_account(arm)
account_list.add_account(ball)
account_list.add_account(oak)

print(account_list.account)

print(account_list.register("boom", "chatlaong",
      "boom@gmail.com", "boomboom", "oak08293242", "0828944245", "Owner"))

roomlist = RoomCatalog()


app = FastAPI()


@app.get("/Search_maxmin_price")
async def search_maxmin_price(minprice: int, maxprice: int):
    Dorm = Dorcat.search_maxmin_price(minprice, maxprice)

    return {"Dormitory": Dorm}


@app.post("/Register")
async def add_user(Name: str, Lastname: str, Email: str, User_name: str, Password: str, User_phone: str, Role: str):
    register = account_list.register(
        Name, Lastname, Email, User_name, Password, User_phone, Role)
    if (type(register) == str):
        return "unsuccess"
    return {"Status": register}


@app.get("/account list")
async def get_userlist():
    return {"Account": account_list.account}


@app.get("/View Detail")
async def get_detail(dormitory_name: str):
    dict = Dorcat.view_detail_dormitory(dormitory_name)
    return {"Detail": dict}
