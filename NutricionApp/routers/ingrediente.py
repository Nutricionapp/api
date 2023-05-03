from typing import List
from NutricionApp import database, schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from NutricionApp.repository import ingrediente

router = APIRouter(
    prefix="/ingrediente",
    tags=['Ingrediente']
)
get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowIngrediente])
def get_ingredients(db: Session = Depends(get_db)):
    return ingrediente.get_all(db)

@router.post('/', response_model=schemas.ShowIngrediente)
def create_ingredient(request: schemas.Ingrediente, db: Session = Depends(get_db)):
    return ingrediente.create(request, db)

@router.get('/{id}', response_model=schemas.ShowIngrediente)
def get_ingredient(id: int, db: Session = Depends(get_db)):
    return ingrediente.show(id, db)
