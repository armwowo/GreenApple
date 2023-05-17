from Backend.DormitoryCatalog import DormitoryCatalog
from typing import Union
from Backend.Dormitory import Dormitory
from  Backend.Main import *
from fastapi import Depends,FastAPI,HTTPException,status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi import FastAPI,Body

SECRET_KEY = "87ccb4638d2228accb6b110a2f69b6bfd45a2fbd6c1c51f229a96f7a7545d8e3"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES =30


app = FastAPI()



origins = [
    "*",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message" : "hello world"}

@app.get( "/getuserdata",tags=["data"])
async def get_user_data(user:str):
    current_user = account_list.find_data_user(user)
    if current_user!=False:
        return {"Name":current_user.name,
                "Email":current_user.get_email(),
                "Username":current_user.get_username(),
                "Phone_number":current_user.userphone,
                "Reservation":current_user.reservation}
    else: {}

@app.get( "/getdatadorm",tags=["data"])
async def get_dormitory_list():
    return {"dor_list":dormcat.dormitory_listmain}



@app.get( "/firstpagedata",tags=["data"])
async def dict_dor():
    list = []
    id = 0
    for dor in dormcat.dormitory_listmain():
        list.append({"id":id,
            "name":dor.name,
                    "address":dor.address(),
                    "price":str(min(dor.get_room_rental_list()))+" - "+str(max(dor.get_room_rental_list()))
                    })
        id+=1
    return list

@app.get( "/userlist",tags=["data"])
async def userList():
    return {"account list":account_list.account}


@app.post("/add_dormitory")
async def add_dormitory(dormitory : dict = Body(...)):
    dor = Dormitory(dormitory["name"],dormitory["address"],dormitory["details"],dormitory["phone"],dormitory["electric"]
                    ,dormitory["water"],dormitory["service_fees"],dormitory["internet"],dormitory["picture"],dormitory["term_of_service"]
                    ,dormitory["owner_name"])
    DormitoryCatalog().add_dormitory_main(dor)
    return dor
    

@app.get("/searchFacilities/")
def searchFacilities(fac :str):
    list_dormitory = dormcat.search_fac_dor(fac)
    return {"DormitoryCatalog": list_dormitory}

@app.get("/view-reservation/{username}")
def viewReservation(username :str):
    account = account_list.find_data_user(username)
    return {"account": str(account.reservation)}

@app.get("/searchByPrice/", tags=["Search"])
def search_by_price(minimum :int, maximum :int):
    return dormcat.search_maxmin_price(minimum,maximum)

@app.post("/login")
async def login(username: str,password:str):
    status = account_list.check_user(username,password)
    if (type(status) == str):
        return "unsuccess"
    return {"Status": status}

@app.post("/Register")
async def add_user(Name: str, Lastname: str, Email: str, User_name: str, Password: str, User_phone: str, Role: str):
    register = account_list.register(
        Name, Lastname, Email, User_name, Password, User_phone, Role)
    print(register)
    if (type(register) == str):
        return "unsuccess"
    return register

@app.get( "/getuserdata",tags=["data"])
async def get_user_data(user:str):
    current_user = account_list.find_data_user(user)
    if current_user!=False:
        return {"Name":current_user.get_name(),
                "Email":current_user.get_email(),
                "Username":current_user.get_username(),
                "Phone_number":current_user.get_userphone(),
                "Reservation":current_user.reservation}
    else: {}

@app.post("/createReservations", tags=["Booking"])
def create_reservation(email:str,check_in_date:str,check_out_date:str,dorm_name:str,room_id:str):
    reservation = system.create_reservation(email,check_in_date,check_out_date,dorm_name,room_id)
    return reservation