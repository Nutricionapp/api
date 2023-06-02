from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from NutricionApp import database, schemas
from NutricionApp.repository import estatura

router = APIRouter(
    prefix="/estatura",
    tags=['Estatura']
)
get_db = database.get_db


@router.post('/', response_model=schemas.ShowEstaturaUsuario)
def create_height(request: schemas.Estatura, db: Session = Depends(get_db)):
    return estatura.create(request, db)


@router.get('/{id_usuario}', response_model=List[schemas.ShowEstaturaUsuario])
def get_height(id_usuario: int, db: Session = Depends(get_db)):
    return estatura.show(id_usuario, db)
