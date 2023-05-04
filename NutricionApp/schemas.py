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

class Estatura(BaseModel):
    estatura: int
    fecha_toma: date
    id_usuario: int
    class Config(): orm_mode = True

class Peso(BaseModel):
    peso: int
    fecha_toma: date
    id_usuario: int
    class Config(): orm_mode = True

class Receta(BaseModel):
    nombre_receta: str
    tipo_comdida: str
    preparacion: str
    class Config(): orm_mode=True

class ShowReceta(BaseModel):
    nombre_receta: str
    tipo_comida: str
    preparacion: str
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

class ShowAlergiaUsuario(BaseModel):
    ingredient: ShowIngrediente
    class Config(): orm_mode=True
class ShowAlergias(BaseModel):
    usuario: ShowUser
    ingredient: ShowIngrediente
    class Config(): orm_mode=True

class ShowEstaturaUsuario(BaseModel):
    estatura: int
    fecha_toma: date
    class Config(): orm_mode=True

class ShowPesoUsuario(BaseModel):
    peso: int
    fecha_toma: date
    class Config(): orm_mode = True

class ShowIngredienteUsado(BaseModel):
    nombre_ingrediente: str
    cantidad_calorias: float
    class Config(): orm_mode = True

class ShowRecetaIngredientes(BaseModel):
    nombre_receta: str
    tipo_comida: str
    ingredientes: List[ShowIngredienteUsado]
    preparacion: str
    class Config(): orm_mode=True