from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def get_all(db: Session):
    ingredientes = db.query(models.Ingrediente).order_by(models.Ingrediente.nombre_ingrediente).all()
    return ingredientes


def create(request: schemas.Ingrediente, db: Session):
    new_ingrediente = models.Ingrediente(nombre_ingrediente=request.nombre_ingrediente,
                                         cantidad_calorias=request.cantidad_calorias,
                                         id_categoria=request.id_categoria)
    db.add(new_ingrediente)
    db.commit()
    db.refresh(new_ingrediente)
    return new_ingrediente


def show(id: int, db: Session):
    ingrediente = db.query(models.Ingrediente).filter(models.Ingrediente.id_ingrediente == id).first()
    if not ingrediente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El ingrediente con id {id} no existe")
    return ingrediente
