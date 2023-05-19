from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from datetime import date


def create(request: schemas.ProgresoUsuario, db: Session):
    new_progreso = models.ProgresoDiario(fecha=request.fecha,
                                id_usuario=request.id_usuario,
                                 porcentaje_avance=request.porcentaje_avance)
    db.add(new_progreso)
    db.commit()
    db.refresh(new_progreso)
    return new_progreso

def show(id_usuario: int, db: Session):
    progreso = db.query(models.ProgresoDiario).filter(models.ProgresoDiario.id_usuario == id_usuario, models.ProgresoDiario.fecha == date.today()).order_by(models.ProgresoDiario.porcentaje_avance.desc()).first()
    if not progreso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El usuario {id_usuario} no tiene registrado progreso el día de hoy")
    return progreso

