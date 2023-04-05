from ..Backend.DormitoryCatalog import DormitoryCatalog
from typing import Union

from fastapi import FastAPI,Body

app = FastAPI()


@app.get("/searchFacilities")
def get_dormitory_list():
    return DormitoryCatalog.get_dormitory_listmain()


@app.post("/searchFacilities")
async def searchFacilities(fac :str = Body(...)) -> list:
    list_dormitory = DormitoryCatalog().search_fac_dor(fac)
    return {"DormitoryCatalog": list_dormitory}

