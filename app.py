from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import base64

app = FastAPI()

class AddTwit(BaseModel):
    username: str
    password: str
    text: str

@app.put('/addtwit')
def addTwit(item: AddTwit):
    username = base64.b64decode(item.username)
    password = base64.b64decode(item.password)
    text = base64.b64decode(item.text)
    