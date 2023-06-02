from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def get_all(db: Session):
    objetivos = db.query(models.Objetivo).all()
    return objetivos


def create(request: schemas.Objetivo, db: Session):
    new_objetivo = models.Objetivo(id_usuario=request.id_objetivo,
                                   nombre_objetivo=request.nombre_objetivo)
    db.add(new_objetivo)
    db.commit()
    db.refresh(new_objetivo)
    return new_objetivo


def show(id: int, db: Session):
    objetivo = db.query(models.Objetivo).filter(models.Objetivo.id_objetivo == id).first()
    if not objetivo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Ese tal objetivo {id} no existe")
    return objetivo
