from typing import List, Optional
from pydantic import BaseModel
from datetime import date


class Usuario(BaseModel):
    nombre_usuario: str
    fecha_nacimiento: date
    id_estilo_vida: int
    class Config(): orm_mode=True
class EstiloVida(BaseModel):
    nombre_estilo: str
    class Config(): orm_mode=True

class Ingrediente(BaseModel):
    nombre_ingrediente: str
    cantidad_calorias: int
    id_categoria: int
    class Config(): orm_mode=True

class Alergia(BaseModel):
    id_usuario: int
    id_ingrediente: int
    class Config(): orm_mode=True

class CategoriaIngrediente(BaseModel):
    nombre_categoria: str
    class Config(): orm_mode=True

class ShowEstilo(BaseModel):
    nombre_estilo: str
    class Config(): orm_mode=True
class ShowUser(BaseModel):
    nombre_usuario:str
    estilo: ShowEstilo
    class Config(): orm_mode=True

class ShowCategoriaIngrediente(BaseModel):
    nombre_categoria: str
    class Config(): orm_mode=True

class ShowIngrediente(BaseModel):
    nombre_ingrediente: str
    cantidad_calorias: int
    categoria: ShowCategoriaIngrediente
    class Config(): orm_mode=True

class ShowAlergia(BaseModel):
    usuario: ShowUser
    ingrediente: ShowIngrediente
    class Config(): orm_mode=True