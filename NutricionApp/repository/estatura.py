from sqlalchemy.orm import Session
from sqlalchemy import desc
from .. import models, schemas
from fastapi import HTTPException, status


def create(request: schemas.Estatura, db: Session):
    new_estatura = models.Estatura(id_usuario=request.id_usuario,
                              estatura=request.estatura,
                              fecha_toma=request.fecha_toma)
    db.add(new_estatura)
    db.commit()
    db.refresh(new_estatura)
    return new_estatura

def show(id: int, db: Session):
    estaturas = db.query(models.Estatura).filter(models.Estatura.id_usuario == id).order_by(desc(models.Estatura.fecha_toma)).all()
    if not estaturas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El usuario con id {id} no existe o no tiene medidas asociadas")
    return estaturas

