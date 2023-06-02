import datetime

from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
import random
from datetime import date


def create(db: Session):
    comidas=("Desayuno","Merienda","Almuerzo","Merienda","Cena")
    rutinas = db.query(models.Rutina).filter(models.Rutina.vigente == 1).all()
    for rutina in rutinas:
        finales=[0 for _ in range(5)]
        id_usuario=rutina.id_usuario
        calorias=rutina.calorias_diarias
        calorias/=5
        alergias = db.query(models.Alergia).filter(models.Alergia.id_usuario == id_usuario).all()
        alergias = set([x.id_ingrediente for x in alergias])
        for i in range(0,len(comidas)):
            recetas_validas = list()
            recetas_calorias = db.query(models.Receta).filter(models.Receta.cantidad_calorias<calorias+350,models.Receta.cantidad_calorias>calorias-350,models.Receta.tipo_comida == comidas[i]).all()
            id_recetas=[x.id_receta for x in recetas_calorias]
            for receta in id_recetas:
                ingredientes=db.query(models.IngredienteReceta).filter(models.IngredienteReceta.id_receta == receta).all()
                ingredientes=set([x.id_ingrediente for x in ingredientes])
                if len(alergias.intersection(ingredientes))==0: recetas_validas.append(receta)
            if len(recetas_validas)==0: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No se encontró {comidas[i]} pertinente para {id_usuario}")
            finales[i]=random.choice(recetas_validas)

        new_progreso = models.ProgresoDiario(fecha=str(date.today()),
                                  id_desayuno=finales[0],
                                  id_merienda1=finales[1],
                                  id_almuerzo=finales[2],
                                  id_merienda2=finales[3],
                                  id_cena=finales[4],
                                  calorias_extra=0,
                                  id_rutina=rutina.id_rutina,
                                  porcentaje=0)
        db.add(new_progreso)
        db.commit()
        db.refresh(new_progreso)
    return new_progreso

"""def update(id_rutina: int, db:Session):
    objetivo = db.query(models.Rutina).filter(models.Rutina.id_rutina == id_rutina).first()
    if not objetivo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El usuario {id} no existe o no tiene objetivos actuales asociados")
    objetivo.vigente=0
    db.add(objetivo)
    db.commit()
    return objetivo



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
    return objetivo"""