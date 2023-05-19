from typing import List
from NutricionApp import database, schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from NutricionApp.repository import progreso_usuario

router = APIRouter(
    prefix="/progreso_diario",
    tags=['Progreso Diario']
)
get_db = database.get_db

@router.post('/', response_model=schemas.ProgresoUsuario)
def create_progress(request: schemas.ProgresoUsuario, db: Session = Depends(get_db)):
    return progreso_usuario.create(request, db)

@router.get('/{id_usuario}', response_model=schemas.ShowProgresoUsuario)
def get_progress(id_usuario: int, db: Session = Depends(get_db)):
    return progreso_usuario.show(id_usuario, db)
