from typing import Annotated, Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form, File, UploadFile
from pydantic import BaseModel
import shutil
import json


app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str
    password: str
    # image: Annotated[bytes, File()]
    
@app.post('/login', status_code=201)
async def login(user: User):
# async def login(username: str = Form(...), password: str = Form(...), image: UploadFile = File(...)):
    # guardar la imagen en el servidor
    
    # print(image.filename)
    return user


@app.post('/images')
async def load_images(file: UploadFile):
    return {'filename': file.filename}