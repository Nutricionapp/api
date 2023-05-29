from NutricionApp import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from NutricionApp.repository import usuario

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.Usuario, db: Session = Depends(get_db)):
    return usuario.create(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def show(id: int, db: Session = Depends(get_db)):
    return usuario.show(id,db)

@router.get('/correo/{correo}', status_code=200, response_model=schemas.ShowUser)
def show_by_email(correo: str, db: Session = Depends(get_db)):
    return usuario.show_by_email(correo,db)