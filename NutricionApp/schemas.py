from typing import List, Optional
from pydantic import BaseModel
from datetime import date


class Usuario(BaseModel):
    id_usuario: Optional[int]
    nombre_usuario: str
    fecha_nacimiento: date
    id_estilo_vida: int
    registro_completo: int
    class Config(): orm_mode=True

class EstiloVida(BaseModel):
    id_estilo: Optional[int]
    nombre_estilo: str
    class Config(): orm_mode=True

class Ingrediente(BaseModel):
    id_ingrediente: Optional[int]
    nombre_ingrediente: str
    cantidad_calorias: int
    id_categoria: int
    class Config(): orm_mode=True

class Alergia(BaseModel):
    id_usuario: int
    id_ingrediente: int
    class Config(): orm_mode=True

class CategoriaIngrediente(BaseModel):
    id_categoria: Optional[int]
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
    id_receta: Optional[int]
    nombre_receta: str
    tipo_comdida: str
    preparacion: str
    class Config(): orm_mode=True

class Enfermedad(BaseModel):
    id_enfermedad: Optional[int]
    nombre_enfermedad: str
    class Config(): orm_mode=True

class EnfermedadUsuario(BaseModel):
    id_usuario: int
    id_enfermedad: int
    class Config(): orm_mode=True
class ShowEnfermedadUsuario(BaseModel):
    enfermedades_u: Enfermedad
    class Config(): orm_mode=True

class ShowReceta(BaseModel):
    nombre_receta: str
    tipo_comida: str
    preparacion: str
    url_imagen: str
    class Config(): orm_mode=True
class ShowEstilo(BaseModel):
    id_estilo: Optional[int]
    nombre_estilo: str
    class Config(): orm_mode=True

class ShowUser(BaseModel):
    id_usuario: Optional[int]
    nombre_usuario:str
    estilo: ShowEstilo
    registro_completo: int
    class Config(): orm_mode=True

class ShowCategoriaIngrediente(BaseModel):
    nombre_categoria: str
    class Config(): orm_mode=True

class ShowIngrediente(BaseModel):
    id_ingrediente: Optional[int]
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
    id_ingrediente: int
    calorias_ingrediente: float
    class Config(): orm_mode = True

class ShowRecetaIngredientes(BaseModel):
    nombre_receta: str
    tipo_comida: str
    preparacion: str
    ingredientes_r: List[ShowIngredienteUsado]
    class Config(): orm_mode=True

class Objetivo(BaseModel):
    id_objetivo: Optional[int]
    nombre_objetivo: str
    class Config(): orm_mode = True

class Rutina(BaseModel):
    id_rutina: Optional[int]
    cantidad_comidas: int
    id_objetivo: int
    calorias_diarias: float
    vigente: int
    id_usuario: int
    class Config(): orm_mode = True

class ShowObjetivo(BaseModel):
    id_objetivo: Optional[int]
    nombre_objetivo: str
    class Config(): orm_mode = True

class ShowRutina(BaseModel):
    id_rutina: Optional[int]
    objetivo: ShowObjetivo
    cantidad_comidas: int
    calorias_diarias: int
    vigente: int
    class Config(): orm_mode = True

class ShowRutinas(BaseModel):
    id_rutina: Optional[int]
    cantidad_comidas: int
    objetivo: ShowObjetivo
    calorias_diarias: float
    vigente: int
    class Config(): orm_mode = True

class ProgresoUsuario(BaseModel):
    id_registro: Optional[int]
    fecha: date
    id_usuario: int
    porcentaje_avance: float
    class Config(): orm_mode=True

class ShowProgresoUsuario(BaseModel):
    fecha: date
    porcentaje_avance: float
    class Config(): orm_mode=True


