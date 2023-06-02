from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from NutricionApp import database, schemas
from NutricionApp.repository import alergia

router = APIRouter(
    prefix="/alergia",
    tags=['Alergia']
)
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowAlergias])
def get_allergies(db: Session = Depends(get_db)):
    return alergia.get_all(db)


@router.post('/', response_model=schemas.ShowAlergias)
def create_allergy(request: schemas.Alergia, db: Session = Depends(get_db)):
    return alergia.create(request, db)


@router.get('/{id_usuario}', response_model=List[schemas.ShowAlergiaUsuario])
def get_allergy(id_usuario: int, db: Session = Depends(get_db)):
    return alergia.show(id_usuario, db)
