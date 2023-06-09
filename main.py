from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from NutricionApp import models
from NutricionApp.database import engine
from NutricionApp.routers import estilo_vida, usuario, categoria_ingrediente, ingrediente, alergia, estatura, peso, \
    receta, enfermedad, enfermedad_usuario, rutina, objetivo, ingrediente_receta, progreso_diario, tip

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)
app.include_router(estilo_vida.router)
app.include_router(usuario.router)
app.include_router(categoria_ingrediente.router)
app.include_router(ingrediente.router)
app.include_router(alergia.router)
app.include_router(estatura.router)
app.include_router(peso.router)
app.include_router(receta.router)
app.include_router(enfermedad.router)
app.include_router(enfermedad_usuario.router)
app.include_router(rutina.router)
app.include_router(objetivo.router)
app.include_router(ingrediente_receta.router)
app.include_router(progreso_diario.router)
app.include_router(tip.router)
#
