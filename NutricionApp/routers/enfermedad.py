from typing import List
from NutricionApp import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from NutricionApp.repository import enfermedad

router = APIRouter(
    prefix="/enfermedad",
    tags=['Enfermedad']
)
get_db = database.get_db

@router.get('/',response_model=List[schemas.Enfermedad])
def get_diseases(db: Session = Depends(get_db)):
    return enfermedad.get_all(db)
@router.post('/', response_model=schemas.Enfermedad)
def create_disease(request: schemas.Enfermedad, db: Session = Depends(get_db)):
    return enfermedad.create(request, db)

@router.get('/{id}', response_model=schemas.Enfermedad)
def get_disease(id: int, db: Session = Depends(get_db)):
    return enfermedad.show(id, db)
