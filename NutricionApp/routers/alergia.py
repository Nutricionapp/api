from typing import List
from NutricionApp import database, schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from NutricionApp.repository import alergia

router = APIRouter(
    prefix="/alergia",
    tags=['Alergia']
)
get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowAlergia])
def get_allergies(db: Session = Depends(get_db)):
    return alergia.get_all(db)

@router.post('/', response_model=schemas.ShowAlergia)
def create_allergy(request: schemas.Alergia, db: Session = Depends(get_db)):
    return alergia.create(request, db)

@router.get('/{id}', response_model=schemas.ShowAlergia)
def get_allergy(id: int, db: Session = Depends(get_db)):
    return alergia.show(id, db)
