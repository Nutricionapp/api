from typing import List
from NutricionApp import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from NutricionApp.repository import receta

router = APIRouter(
    prefix="/receta",
    tags=['Receta']
)
get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowReceta])
def get_recipes(db: Session = Depends(get_db)):
    return receta.get_all(db)

@router.post('/', response_model=schemas.ShowReceta)
def create_recipe(request: schemas.Receta, db: Session = Depends(get_db)):
    return receta.create(request, db)


@router.get('/{id}', response_model=schemas.ShowRecetaIngredientes)
def get_recipe(id: int, db: Session = Depends(get_db)):
    return receta.show(id, db)
