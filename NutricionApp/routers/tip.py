from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from NutricionApp import database, schemas
from NutricionApp.repository import tip

router = APIRouter(
    prefix="/tip",
    tags=['Tips']
)
get_db = database.get_db


@router.post('/', response_model=schemas.Tip)
def create_tip(request: schemas.Tip, db: Session = Depends(get_db)):
    return tip.create(request, db)


@router.get('/{id_objetivo}', response_model=List[schemas.ShowTip])
def get_tips(id_objetivo: int, db: Session = Depends(get_db)):
    return tip.show(id_objetivo, db)
