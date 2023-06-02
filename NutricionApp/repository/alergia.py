from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def get_all(db: Session):
    alergias = db.query(models.Alergia).all()
    return alergias


def create(request: schemas.Alergia, db: Session):
    new_alergia = models.Alergia(id_usuario=request.id_usuario,
                                 id_ingrediente=request.id_ingrediente)
    db.add(new_alergia)
    db.commit()
    db.refresh(new_alergia)
    return new_alergia


def show(id_usuario: int, db: Session):
    alergia = db.query(models.Alergia).filter(models.Alergia.id_usuario == id_usuario).all()
    if not alergia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El usuario {id_usuario} no tiene registrada ninguna alergia")
    return alergia
