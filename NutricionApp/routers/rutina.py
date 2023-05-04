from typing import List
from NutricionApp import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from NutricionApp.repository import rutina

router = APIRouter(
    prefix="/rutinas",
    tags=['Rutinas']
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowRutina)
def create_user(request: schemas.Rutina, db: Session = Depends(get_db)):
    return rutina.create(request, db)


@router.get('/{id_usuario}', status_code=200, response_model=List[schemas.ShowRutina])
def show(id_usuario: int, db: Session = Depends(get_db)):
    return rutina.show(id_usuario,db)

@router.get('/objetivo_actual/{id_usuario}',status_code=200,response_model=schemas.ShowRutina)
def show(id_usuario: int, db: Session = Depends(get_db)):
    return rutina.show_rutina_actual(id_usuario, db)