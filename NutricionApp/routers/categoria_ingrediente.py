from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from NutricionApp import database, schemas
from NutricionApp.repository import categoria_ingrediente

router = APIRouter(
    prefix="/categoria_ingrediente",
    tags=['CategoriaIngrediente']
)
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowCategoriaIngrediente])
def get_categories(db: Session = Depends(get_db)):
    return categoria_ingrediente.get_all(db)


@router.post('/', response_model=schemas.ShowCategoriaIngrediente)
def create_category(request: schemas.CategoriaIngrediente, db: Session = Depends(get_db)):
    return categoria_ingrediente.create(request, db)


@router.get('/{id}', response_model=schemas.ShowCategoriaIngrediente)
def get_category(id: int, db: Session = Depends(get_db)):
    return categoria_ingrediente.show(id, db)
