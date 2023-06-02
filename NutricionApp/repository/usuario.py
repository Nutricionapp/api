from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def create(request: schemas.Usuario, db: Session):
    new_user = models.Usuario(nombre_usuario=request.nombre_usuario,
                              fecha_nacimiento=request.fecha_nacimiento,
                              id_estilo_vida=request.id_estilo_vida,
                              registro_completo=request.registro_completo,
                              correo=request.correo,
                              sexo=request.sexo)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session):
    user = db.query(models.Usuario).filter(models.Usuario.id_usuario == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user


def show_by_email(correo: str, db: Session):
    user = db.query(models.Usuario).filter(models.Usuario.correo == correo).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the email {correo} is not available")
    return user
