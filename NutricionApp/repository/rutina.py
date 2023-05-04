from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def create(request: schemas.Rutina, db: Session):
    new_routine = models.Rutina(cantidad_comidas=request.cantidad_comidas,
                              id_objetivo=request.id_objetivo,
                              calorias_diarias=request.calorias_diarias,
                              vigente=request.vigente,
                              id_usuario=request.id_usuario)
    db.add(new_routine)
    db.commit()
    db.refresh(new_routine)
    return new_routine


def show(id: int, db: Session):
    rutinas = db.query(models.Rutina).filter(models.Rutina.id_usuario == id).all()
    if not rutinas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El usuario {id} no existe o no tiene rutinas asociadas")
    return rutinas

def show_rutina_actual(id_usuario: int, db: Session):
    objetivo = db.query(models.Rutina).filter(models.Rutina.id_usuario == id_usuario,models.Rutina.vigente==1).first()
    if not objetivo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El usuario {id} no existe o no tiene objetivos actuales asociados")
    return objetivo
