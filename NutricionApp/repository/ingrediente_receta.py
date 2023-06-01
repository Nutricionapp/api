from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def create(request: schemas.IngredienteReceta, db: Session):
    new_ingrediente = models.IngredienteReceta(id_receta=request.id_receta,
                                               id_ingrediente=request.id_ingrediente,
                                               cantidad_ingrediente=request.cantidad_ingrediente)
    db.add(new_ingrediente)
    db.commit()
    db.refresh(new_ingrediente)
    return new_ingrediente

def show(id_receta: int, db: Session):
    ingrediente = db.query(models.IngredienteReceta).filter(models.IngredienteReceta.id_receta == id_receta).all()
    if not ingrediente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No hay ingredientes registrados para la receta {id}")
    return ingrediente
