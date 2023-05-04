from typing import List
from NutricionApp import database, schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from NutricionApp.repository import peso

router = APIRouter(
    prefix="/peso",
    tags=['Peso']
)
get_db = database.get_db

@router.post('/', response_model=schemas.ShowPesoUsuario)
def create_weight(request: schemas.Peso, db: Session = Depends(get_db)):
    return peso.create(request, db)

@router.get('/{id_usuario}', response_model=List[schemas.ShowPesoUsuario])
def get_weight(id_usuario: int, db: Session = Depends(get_db)):
    return peso.show(id_usuario, db)
