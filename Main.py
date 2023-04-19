from fastapi import FastAPI
from typing import Union
from typing import Optional
from Backend.Main import *

app = FastAPI()

@app.get("/login", tags=["User"])
async def login(username: str,password:str):
    status = account_list.check_user(username,password)

    return {"Status" : status}

@app.get("/searchByName", tags=["Search"])
def search_by_name(name :str):
    list_dormitory = dormcat.search_dor_name(name)

    return {"Dormitory Catalog": list_dormitory}

@app.get("/assignRoom", tags=["Dormitory"])
def assign_room(name: str):
    dorm = dormcat.find_dormitory(name)
    #return dorm
    return {"Available Room": dorm._Roomlist.check_room_status()}

@app.delete("/cancelDormitory", tags=["Dormitory"])
def cancel_dormitory(name: str):
    return {"Status": dormcat.cancel_dormitory(name)}

@app.get("/getDormcatalog", tags=["Dormitory"])
def get_dormitory_catalog():
    dormlist = dormcat._Dormitory_listmain
    return {"Dormitory Catalog": dormlist}

@app.post("/register", tags=["User"])
def register(name: str, lastname: str, email: str, user_name: str, password: str, user_phone: str):
    return {"Status": account_list.register(name,lastname,email,user_name,password,user_phone)}

@app.get("/accountList", tags=["User"])
def get_account_list():
    return {"Account List": account_list._account}

@app.get("/detailDormitory", tags=["Dormitory"])
def get_detail_dormitory(name: str):
    return {"Detail": dormcat.find_dormitory(name)}
