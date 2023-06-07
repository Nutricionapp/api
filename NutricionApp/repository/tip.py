from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def create(request: schemas.Tip, db: Session):
    new_tip = models.Tip(id_tip=request.id_tip,
                         id_objetivo=request.id_objetivo,
                         tip=request.tip)
    db.add(new_tip)
    db.commit()
    db.refresh(new_tip)
    return new_tip


def show(id_objetivo: int, db: Session):
    tips = db.query(models.Tip).filter(models.Tip.id_objetivo == id_objetivo).all()
    if not tips:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No se encontraron tips para el objetivo con id {id_objetivo}")
    return tips
