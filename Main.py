from Backend.DormitoryCatalog import DormitoryCatalog
from typing import Union
from Backend.Dormitory import Dormitory
from  Backend.Main import *
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI,Body

app = FastAPI()
origins = [
    "*",  # Replace with the appropriate origin of your React application
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)

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
# @app.get("/view-reservation")
# def viewReservation():
#     return {"Account List": account_list.get_account()}