from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def get_all(db: Session):
    estilos = db.query(models.EstiloVida).all()
    return estilos


def create(request: schemas.EstiloVida, db: Session):
    new_style = models.EstiloVida(nombre_estilo=request.nombre_estilo,
                                  multiplicador=request.multiplicador)
    db.add(new_style)
    db.commit()
    db.refresh(new_style)
    return new_style


def show(id: int, db: Session):
    estilo = db.query(models.EstiloVida).filter(models.EstiloVida.id_estilo == id).first()
    if not estilo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El estilo de vida {id} no existe")
    return estilo
