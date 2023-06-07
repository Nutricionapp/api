from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def get_all(db: Session):
    recetas = db.query(models.Receta).all()
    return recetas


def create(request: schemas.Receta, db: Session):
    new_recipe = models.Receta(nombre_receta=request.nombre_receta,
                               tipo_comida=request.tipo_comdida,
                               preparacion=request.preparacion,
                               url_imagen=request.url_imagen,
                               cantidad_calorias=request.cantidad_calorias,
                               calificacion=request.calificacion,
                               id_autor=request.id_autor)
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


def show_tipo_comida(tipo_comida: str, db: Session):
    receta = db.query(models.Receta).filter(models.Receta.tipo_comida == tipo_comida).all()
    if not receta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No existen recetas para {tipo_comida}")
    return receta

def cambiar_preparacion(id_receta: int, preparacion: str, db: Session):
    receta = db.query(models.Receta).filter(models.Receta.id_receta==id_receta).first()
    if not receta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No existen recetas con id {id_receta}")
    receta.preparacion=preparacion
    db.add(receta)
    db.commit()
    return receta

