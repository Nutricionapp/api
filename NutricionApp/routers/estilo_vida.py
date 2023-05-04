from typing import List
from NutricionApp import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from NutricionApp.repository import estilo_vida

router = APIRouter(
    prefix="/estilo_vida",
    tags=['EstiloVida']
)
get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowEstilo])
def get_styles(db: Session = Depends(get_db)):
    return estilo_vida.get_all(db)
@router.post('/', response_model=schemas.ShowEstilo)
def create_style(request: schemas.EstiloVida, db: Session = Depends(get_db)):
    return estilo_vida.create(request, db)


@router.get('/{id}', response_model=schemas.ShowEstilo)
def get_style(id: int, db: Session = Depends(get_db)):
    return estilo_vida.show(id, db)
