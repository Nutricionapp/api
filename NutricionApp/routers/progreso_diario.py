from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from NutricionApp import database, schemas
from NutricionApp.repository import progreso_diario

router = APIRouter(
    prefix="/progreso_diario",
    tags=['ProgresoDiario']
)
get_db = database.get_db


@router.post('/', response_model=schemas.ShowProgresoDiario)
def create_progress(db: Session = Depends(get_db)):
    return progreso_diario.create(db)


@router.put("/porcentaje/{id_usuario}", status_code=status.HTTP_200_OK, response_model=schemas.ShowProgresoDiario)
def update_percentage(id_usuario: int, db: Session = Depends(get_db)):
    return progreso_diario.update(id_usuario, db)


@router.put("/extra/{id_usuario}/{calorias_extra}", status_code=status.HTTP_200_OK,
            response_model=schemas.ShowProgresoDiario)
def update_extra(id_usuario: int, calorias_extra: float, db: Session = Depends(get_db)):
    return progreso_diario.update_extra(id_usuario, calorias_extra, db)


@router.get('/{id_usuario}', response_model=schemas.ShowProgresoDiario)
def get_progress(id_usuario: int, db: Session = Depends(get_db)):
    return progreso_diario.show_progreso_usuario(id_usuario, db)
