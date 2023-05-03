import fastapi
from fastapi import FastAPI
from typing import Union
from typing import Optional
from Backend.Main import *
from pydantic import BaseModel
from datetime import datetime
app = FastAPI()

@app.get("/login", tags=["User"])
async def login(username: str,password:str):
    status = account_list.check_user(username,password)

    return {"Status" : status}

@app.get("/searchByName", tags=["Search"])
def search_by_name(name :str):
    list_dormitory = dormcat.search_dor_name(name)
    
    return {"Dormitory Catalog": list_dormitory}

# @app.get("/searchFacilities/", tags=["Search"])
# def search_facilities(facilities :str):
#     list_dormitory = dormcat.search_fac_dor(facilities)

#     return {"DormitoryCatalog": list_dormitory}

@app.get("/searchByPrice/", tags=["Search"])
def search_by_price(minimum :int, maximum :int):
    list_dormitory = dormcat.search_maxmin_price(minimum,maximum)
    
    return {"DormitoryCatalog": list_dormitory}
    
# @app.get("/searchByFilter", tags=["Search"])
# def search_by_filter(min_price :int, max_price :int,facility :list):
#     list_dormitory = dormcat.search_dormitories(min_price, max_price, facility)
    
#     return {"Dormitory Catalog": list_dormitory}

@app.get("/availableRoom", tags=["Dormitory"])
def available_room(name: str):
    dorm = dormcat.find_dormitory(name)
    #return dorm
    return {"Available Room": dorm.Roomlist.check_room_status()}

# @app.post("/reservationRoom", tags=["Booking"])
# def reservation(name:str,check_in:str,dor_name:str,room_id:str):
#     return (system.create_reservation(name,check_in,dor_name,room_id))

# class ReservationRequest(BaseModel):
#     name: str
#     check_in_date: str
#     dorm_name: str
#     room_id: str

# class ReservationResponse(BaseModel):
#     user_name: str
#     check_in_date: str
#     dorm_name: str
#     room_id: str

@app.post("/createReservations", tags=["Booking"])
def create_reservation(name:str,check_in_date:str,dorm_name:str,room_id:str):
    reservation = system.create_reservation(name,check_in_date,dorm_name,room_id)
    return reservation

# @app.get("/getReservations/"tags=["Booking"])
# async def get_reservation(room_id: str):
#     for reservation in system.reservation:
#         if reservation.room.room_id == room_id:
#             return reservation.info
#     return False
    


@app.post("/creditPayment", tags=["Booking"])
def credit_payment(name:str,card_name:str,card_number:str,reservation_id:int):
    user = system.accountlist.find_user(name)
    user.get_reservation(reservation_id).create_creditpayment(card_name,card_number).pay()
    return "payment complete"

@app.post("/createRoomreserved", tags=["Booking"])
def create_Roomreserved(name:str,reservation_id:int):
    user = system.accountlist.find_user(name)
    reserved = (user.get_reservation(reservation_id).create_roomreserved())
    return reserved

# @app.get("/debitPayment", tags=["Booking"])
# def debit_payment(card_name,card_number,card_expire,cvv):
#     return(arm.get_reservation(1).create_debitpayment(card_name,card_number,card_expire,cvv))
    

@app.delete("/cancelDormitory", tags=["Dormitory"])
def cancel_dormitory(name: str):
    return {"Status": dormcat.cancel_dormitory(name)}

@app.get("/getDormcatalog", tags=["Dormitory"])
def get_dormitory_catalog():
    dormlist = dormcat.dormitory_listmain
    return {"Dormitory Catalog": dormlist}

@app.post("/register", tags=["User"])
def register(name: str, lastname: str, email: str, user_name: str, password: str, user_phone: str):
    return {"Status": account_list.register(name,lastname,email,user_name,password,user_phone)}

# @app.get("/accountList", tags=["User"]) เอาไว้เช็คเฉยๆไม่จำเป็นต้องมีในหน้า website
# def get_account_list():
#     return {"Account List": account_list._account}

@app.get("/detailDormitory", tags=["Dormitory"]) #ต้องการให้แสดงผลจำนวนห้องพัก และ จำนวนห้องที่ว่างด้วย
def get_detail_dormitory(name: str):
    return {"Detail": dormcat.find_dormitory(name)}