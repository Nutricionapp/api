from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    categorias = db.query(models.CategoriaIngrediente).all()
    return categorias

def create(request: schemas.CategoriaIngrediente, db: Session):
    new_categoria = models.CategoriaIngrediente(nombre_categoria=request.nombre_categoria)
    db.add(new_categoria)
    db.commit()
    db.refresh(new_categoria)
    return new_categoria


def show(id: int, db: Session):
    categoria = db.query(models.CategoriaIngrediente).filter(models.CategoriaIngrediente.id_categoria == id).first()
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"La categoría {id} no existe")
    return categoria
