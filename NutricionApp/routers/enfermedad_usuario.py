from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from NutricionApp import database, schemas
from NutricionApp.repository import enfermedad_usuario

router = APIRouter(
    prefix="/enfermedad_usuario",
    tags=['EnfermedadUsuario']
)
get_db = database.get_db


@router.post('/', response_model=schemas.ShowEnfermedadUsuario)
def create_disease(request: schemas.EnfermedadUsuario, db: Session = Depends(get_db)):
    return enfermedad_usuario.create(request, db)


@router.get('/{id_usuario}', response_model=List[schemas.ShowEnfermedadUsuario])
def get_disease(id_usuario: int, db: Session = Depends(get_db)):
    return enfermedad_usuario.show(id_usuario, db)
