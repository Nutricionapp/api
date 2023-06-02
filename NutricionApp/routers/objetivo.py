from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from NutricionApp import database, schemas
from NutricionApp.repository import objetivo

router = APIRouter(
    prefix="/objetivo",
    tags=['Objetivo']
)
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowObjetivo])
def get_goals(db: Session = Depends(get_db)):
    return objetivo.get_all(db)


@router.post('/', response_model=schemas.ShowObjetivo)
def create_goal(request: schemas.Objetivo, db: Session = Depends(get_db)):
    return objetivo.create(request, db)


@router.get('/{id_objetivo}', response_model=schemas.ShowObjetivo)
def get_goal(id_objetivo: int, db: Session = Depends(get_db)):
    return objetivo.show(id_objetivo, db)
