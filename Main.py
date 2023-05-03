from Backend.Facility import Facility
from Backend.Dormitory import Dormitory
from Backend.DormitoryCatalog import DormitoryCatalog
from Backend.AccountList import AccountList
from Backend.User import User
from fastapi import FastAPI
from Backend.Room import Room
from Backend.RoomCatalog import RoomCatalog
from Backend.Review import Review

jia_jia = Dormitory("jia_jia", "soi hormai", "",
                    "0828932414", 8, 18, 100, "", "", 100, "Arm")
sabaiplace = Dormitory("sabaiplace", "Vcon", "",
                       "4905293028", 8, 18, 9, "", "", 100, "ball")
boomboom_place = Dormitory("boomboom_place", "soiyig", "",
                           "0622541587", 8, 18, 9, "", "", 100, "bass")
# jia_jia.add_facility(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0)
sabaiplace.add_facility(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
boomboom_place.add_facility(0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0)
# jia_jia.add_roomlist(101, 6500, 1, "")
# jia_jia.add_roomlist(102, 6500, 0, "")
# jia_jia.add_roomlist(103, 5000, 1, "")
# jia_jia.add_roomlist(104, 5000, 0, "")
# jia_jia.add_roomlist(105, 5000, 0, "")
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


# boomboom_place.add_review(4, "dsgdsgsgds")

# print(boomboom_place.review_list)

roomlist = RoomCatalog()


app = FastAPI()


@app.get("/Search_maxmin_price", tags=["Search"])
async def search_maxmin_price(minprice: int, maxprice: int):
    Dorm = Dorcat.search_maxmin_price(minprice, maxprice)

    return {"Dormitory": Dorm}


@app.post("/Register", tags=["User"])
async def add_user(Name: str, Lastname: str, Email: str, User_name: str, Password: str, User_phone: str, Role: str):
    register = account_list.register(
        Name, Lastname, Email, User_name, Password, User_phone, Role)
    # if (type(register) == str):
    #     return "unsuccess"
    # elif (register == True):
    #     return "success"
    return {"Status": register}


@app.get("/account list", tags=["User"])
async def get_userlist():
    return {"Account": account_list.account}


@app.get("/View Dor_Detail", tags=["Dormitory"])
async def get_dor_detail(dormitory_name: str):
    dict = Dorcat.view_detail_dormitory(dormitory_name)
    return {"Detail": dict}


@app.post("/review", tags=["Dormitory"])
async def add_review(dorname: str, rating: float, comment: str):
    for dor in Dorcat.dor_list:
        if dor.get__dor_name() == dorname:
            dor.add_review(rating, comment)
            return {"status": "success"}
    return {"status": "Unsuccess"}


@app.get("/review", tags=["Dormitory"])
async def get_review(dorname: str):
    for dor in Dorcat.dor_list:
        if dor.get__dor_name() == dorname:
            return {"Review": dor.review_list}
    return {"status": "Unsuccess"}


@app.put("/edit proflie", tags=["User"])
async def edit_profile(User_name: str, Password: str, Name: str, Lastname: str, Email: str, newUser_name: str, newPassword: str, User_phone: str):
    newprofile = account_list.edit_profile(
        User_name, Password, Name, Lastname, Email, newUser_name, newPassword, User_phone)
    return {"status": newprofile}


@app.get("/View Account_Detail", tags=["User"])
async def get_account_detail(username: str):
    dict = account_list.view_detail_account(username)
    return {"Detail": dict}
