import fastapi
from fastapi import FastAPI
from typing import Union
from typing import Optional
from Backend.Main import *

app = FastAPI()

@app.get("/login")
async def login(username: str,password:str):
    status = account_list.check_user(username,password)

    return {"Status" : status}

@app.get("/searchByName")
def search_by_name(name :str):
    list_dormitory = dormcat.search_dor_name(name)
    
    return {"Dormitory Catalog": list_dormitory}

@app.get("/assignRoom")
def assign_room(name: str):
    available_room = jia_jia._Roomlist.check_room_status()
    
    return {"Available Room": available_room}

@app.delete("/cancelDormitory")
def cancel_dormitory(name: str):
    return {"Status": dormcat.cancel_dormitory(name)}

@app.get("/getDormcatalog")
def get_dormitory_catalog():
    dormlist = dormcat._Dormitory_listmain
    return {"Dormitory Catalog": dormlist}

@app.post("/register")
def register(name: str, lastname: str, email: str, user_name: str, password: str, user_phone: str):
    return {"Status": account_list.register(name,lastname,email,user_name,password,user_phone)}

@app.get("/accountList")
def get_account_list():
    return {"Account List": account_list._account}

@app.get("/detailDormitory")
def get_detail_dormitory(name: str):
    return {"Detail": dormcat.view_detail_dormitory(name)}
