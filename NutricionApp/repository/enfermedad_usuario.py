from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def create(request: schemas.EnfermedadUsuario, db: Session):
    new_enfermedad = models.EnfermedadUsuario(id_usuario=request.id_usuario, id_enfermedad=request.id_enfermedad)
    db.add(new_enfermedad)
    db.commit()
    db.refresh(new_enfermedad)
    return new_enfermedad


def show(id: int, db: Session):
    enfermedad = db.query(models.EnfermedadUsuario).filter(models.EnfermedadUsuario.id_usuario == id).all()
    if not enfermedad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El usuario {id} no existe o no tiene enfermedades asociadas")
    return enfermedad
