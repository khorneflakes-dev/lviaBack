from fastapi import FastAPI, File, Form
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from bson.binary import Binary
import io

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:5000",
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])


client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]


class Modelos(BaseModel):
    nombre: str
    apellido: str
    instagram_url: str
    email: str
    telefono: int
    direccion: str
    ciudad: str
    pais: str
    departamento: str
    edad: int
    


@app.post("/formulario/")
async def create_item(datos: Modelos, foto: bytes = File(...)):
    foto_binaria = Binary(foto)
    item_dict = datos.dict()
    collection.insert_one(item_dict)
    item_dict['foto'] = foto_binaria
    return {"message": "Postulacion recibida."}