from Backend.DormitoryCatalog import DormitoryCatalog
from typing import Union
from Backend.Dormitory import Dormitory
from  Backend.Main import *

from fastapi import FastAPI,Body

app = FastAPI()


@app.get("/")
def read_root():
    return {"message" : "hello world"}

@app.get("/searchFacilities")
def get_dormitory_list():
    return Dorcat.get_dormitory_listmain()


@app.post("/add_dormitory")
async def add_dormitory(dormitory : dict = Body(...)):
    dor = Dormitory(dormitory["name"],dormitory["address"],dormitory["details"],dormitory["phone"],dormitory["electric"]
                    ,dormitory["water"],dormitory["service fees"],dormitory["internet"],dormitory["picture"],dormitory["term of service"]
                    ,dormitory["owner name"])
    DormitoryCatalog().add_dormitory_main(dor)

@app.get("/searchFacilities/")
def searchFacilities(fac :str):
    list_dormitory = Dorcat.search_fac_dor(fac)
    return {"DormitoryCatalog": list_dormitory}

@app.get("/view-reservation/{username}")
def viewReservation(username :str):
    account = account_list.find_data_user(username)
    return {"account": str(account.reservation)}
    # return account

# @app.get("/view-reservation")
# def viewReservation():
#     return {"Account List": account_list.get_account()}