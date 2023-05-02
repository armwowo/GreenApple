import fastapi
from fastapi import FastAPI,Body
from typing import Union
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from Backend.Main import *
from Backend.DormitoryCatalog import DormitoryCatalog

app = FastAPI()

origins = ["*"]  # replace this with your list of allowed origins

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
async def login(username: str,password:str):
    status = account_list.check_user(username,password)
    return JSONResponse(content={"Status": status})

@app.get("/searchByName")
def search_by_name(name :str):
    list_dormitory = Dorcat.search_dor_name(name)
    
    return {"Dormitory Catalog": list_dormitory}

@app.get("/assignRoom")
def assign_room(name: str):
    available_room = jia_jia._Roomlist.check_room_status()
    
    return {"Available Room": available_room}

@app.delete("/cancelDormitory")
def cancel_dormitory(name: str):
    return {"Status": Dorcat.cancel_dormitory(name)}

@app.get("/getDormcatalog")
def get_dormitory_catalog():
    dormlist = Dorcat._Dormitory_listmain
    return {"Dormitory Catalog": dormlist}

@app.post("/Register")
async def add_user(Name: str, Lastname: str, Email: str, User_name: str, Password: str, User_phone: str, Role: str):
    register = account_list.register(
        Name, Lastname, Email, User_name, Password, User_phone, Role)
    if (type(register) == str):
        return "unsuccess"
    return {"Status": register}

@app.get("/")
def read_root():
    return {"message" : "hello world"}

@app.get( "/getdata",tags=["data"])
async def get_dormitory_list():
    dic = []
    for dor in Dorcat.get_dormitory_listmain():
        dic.append({dor.get__dor_name():dor})
    return {"dor_list": dic}

@app.get( "/firstpagedata",tags=["data"])
async def dict_dor():
    list = []
    id = 0
    for dor in Dorcat.get_dormitory_listmain():
        list.append({"id":id,
            "name":dor.get__dor_name(),
                    "address":dor.get__address(),
                    "price":str(min(dor.get_room_rental_list()))+" - "+str(max(dor.get_room_rental_list()))
                    })
        id+=1
    return list


@app.post("/add_dormitory")
async def add_dormitory(dormitory : dict = Body(...)):
    dor = Dormitory(dormitory["name"],dormitory["address"],dormitory["details"],dormitory["phone"],dormitory["electric"]
                    ,dormitory["water"],dormitory["service_fees"],dormitory["internet"],dormitory["picture"],dormitory["term_of_service"]
                    ,dormitory["owner_name"])
    DormitoryCatalog().add_dormitory_main(dor)
    return dor
    

@app.get("/searchFacilities/")
def searchFacilities(fac :str):
    list_dormitory = Dorcat.search_fac_dor(fac)
    return {"DormitoryCatalog": list_dormitory}

@app.get("/view-reservation/{username}")
def viewReservation(username :str):
    account = account_list.find_data_user(username)
    return {"account": str(account.reservation)}
    # return account

@app.get("/searchByPrice/", tags=["Search"])
def search_by_price(minimum :int, maximum :int):
    return Dorcat.search_maxmin_price(minimum,maximum)