from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    recetas = db.query(models.Receta).all()
    return recetas

def create(request: schemas.Receta, db: Session):
    new_recipe = models.Receta(nombre_receta=request.nombre_receta,
                               tipo_comida=request.tipo_comdida,
                               preparacion=request.preparacion)
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe


def show(id: int, db: Session):
    receta = db.query(models.Receta).filter(models.Receta.id_receta == id).first()
    if not receta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"La receta {id} no existe")
    return receta