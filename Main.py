import fastapi
from Backend.AccountList import AccountList
from Backend.User import User
from fastapi import FastAPI
from typing import Union
from typing import Optional

app = FastAPI()

account_list = AccountList()
arm = User("arm","vor","vorarm23@gmail.com","arm","12345","0929349512")
ball = User("ball","watchanon","dragonball@gmail.com","balllnwza","dragonball123","0839456376")
oak = User("oak","chatlaong","kingoak11@gmail.com","oakoak22","oak08293242","0828944245")
account_list.add_account(arm)
account_list.add_account(ball)
account_list.add_account(oak)

@app.get("/login")
async def login(username: str,password:str):
    status = account_list.check_user(username,password)

    return {"Status" : status}