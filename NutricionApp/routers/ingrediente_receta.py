from typing import List
from NutricionApp import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from NutricionApp.repository import ingrediente_receta

router = APIRouter(
    prefix="/ingrediente_receta",
    tags=['IngredienteReceta']
)
get_db = database.get_db

@router.post('/', response_model=schemas.IngredienteReceta)
def add_ingredient(request: schemas.IngredienteReceta, db: Session = Depends(get_db)):
    return ingrediente_receta.create(request, db)

@router.get('/{id_receta}', response_model=List[schemas.ShowIngredienteReceta])
def get_ingredients(id_receta: int, db: Session = Depends(get_db)):
    return ingrediente_receta.show(id_receta, db)
