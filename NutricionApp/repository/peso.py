from fastapi import HTTPException, status
from sqlalchemy import desc
from sqlalchemy.orm import Session

from .. import models, schemas


def create(request: schemas.Peso, db: Session):
    new_peso = models.Peso(id_usuario=request.id_usuario,
                           peso=request.peso,
                           fecha_toma=request.fecha_toma)
    db.add(new_peso)
    db.commit()
    db.refresh(new_peso)
    return new_peso


def show(id: int, db: Session):
    pesos = db.query(models.Peso).filter(models.Peso.id_usuario == id).order_by(desc(models.Peso.fecha_toma)).all()
    if not pesos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El usuario con id {id} no existe o no tiene medidas asociadas")
    return pesos
