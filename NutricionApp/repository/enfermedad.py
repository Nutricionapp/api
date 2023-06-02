from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def get_all(db: Session):
    enfermedades = db.query(models.Enfermedad).all()
    return enfermedades


def create(request: schemas.Enfermedad, db: Session):
    new_enfermedad = models.Enfermedad(nombre_enfermedad=request.nombre_enfermedad)
    db.add(new_enfermedad)
    db.commit()
    db.refresh(new_enfermedad)
    return new_enfermedad


def show(id: int, db: Session):
    enfermedad = db.query(models.Enfermedad).filter(models.Enfermedad.id_enfermedad == id).first()
    if not enfermedad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"La enfermedad {id} no existe")
    return enfermedad
