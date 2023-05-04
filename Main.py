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

@app.post("/register", tags=["User"])
def register(name: str, lastname: str, email: str, user_name: str, password: str, user_phone: str,role:str):
    return {"Status": account_list.register(name,lastname,email,user_name,password,user_phone,role)}

# @app.get("/accountList", tags=["User"]) เอาไว้เช็คเฉยๆไม่จำเป็นต้องมีในหน้า website
# def get_account_list():
#     return {"Account List": account_list._account}
@app.get("/getUserInfo", tags=["User"])
def user_info(username:str):
    user = system.accountlist.find_user_username(username)
    if user != False:
        return user.info
    return "not found"


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
    if dorm != False:
        available_room = dorm.Roomlist.check_room_status()
        return {"Available Room": available_room}
    else: "not found dormitory"

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
def create_reservation(email:str,check_in_date:str,dorm_name:str,room_id:str):
    reservation = system.create_reservation(email,check_in_date,dorm_name,room_id)
    return reservation

@app.delete("/cancelReservations", tags=["Booking"])
def cancel_reservation(email:str,dorm_name:str,room_id:str,reservation_id:int):
    return (system.cancel_reservation(email,dorm_name,room_id,reservation_id))

# @app.get("/getReservations/"tags=["Booking"])
# async def get_reservation(room_id: str):
#     for reservation in system.reservation:
#         if reservation.room.room_id == room_id:
#             return reservation.info
#     return False
    


@app.post("/creditPayment", tags=["Booking"])
def credit_payment(email:str,card_name:str,card_number:str,reservation_id:int):
    user = system.accountlist.find_email(email)
    if user != False:
        reservation = user.get_reservation(reservation_id)
        if reservation != False:
            reservation.create_creditpayment(card_name,card_number)
            return "payment complete"
        else: return "not found reservation"
    else: return "invalid email"

# @app.post("/createRoomreserved", tags=["Booking"])
# def create_Roomreserved(email:str,reservation_id:int):
#     user = system.accountlist.find_email(email)
#     if user != False:
#         reserved = user.get_reservation(reservation_id)
#         if reserved != False:            
#             reserved.create_roomreserved()
#             return "create roomreserved"
#         else: return "not found reservation"
#     return "invalid email"

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

@app.get("/detailDormitory", tags=["Dormitory"]) #ต้องการให้แสดงผลจำนวนห้องพัก และ จำนวนห้องที่ว่างด้วย
def get_detail_dormitory(name: str):
    return {"Detail": dormcat.find_dormitory(name)}

@app.get("/getRoomlist", tags=["Dormitory"])
def get_roomlist(name:str):
    dorm = dormcat.find_dormitory(name)
    if dorm != False:
        room_list = dorm.Roomlist.get_room_info()
        return {"Room list": room_list}
    else: "not found dormitory"