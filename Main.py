import fastapi
from fastapi import FastAPI
from typing import Union
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from Backend.Main import *

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

@app.post("/Register")
async def add_user(Name: str, Lastname: str, Email: str, User_name: str, Password: str, User_phone: str, Role: str):
    register = account_list.register(
        Name, Lastname, Email, User_name, Password, User_phone, Role)
    if (type(register) == str):
        return "unsuccess"
    return {"Status": register}

@app.get("/accountList")
def get_account_list():
    return {"Account List": account_list._account}

@app.get("/detailDormitory")
def get_detail_dormitory(name: str):
    return {"Detail": dormcat.view_detail_dormitory(name)}