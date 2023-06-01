from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from NutricionApp.database import Base
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__='USUARIO'
    id_usuario=Column(Integer,primary_key=True,index=True,autoincrement=True)
    nombre_usuario=Column(String)
    fecha_nacimiento=Column(Date)
    id_estilo_vida=Column(Integer,ForeignKey('ESTILO_VIDA.id_estilo'))
    registro_completo=Column(Integer)
    correo=Column(String)
    sexo=Column(String)
    estilo=relationship("EstiloVida",back_populates="people")
    alergias=relationship("Alergia",back_populates="usuario")
    estaturas=relationship("Estatura",back_populates="usuario_e")
    pesos=relationship("Peso",back_populates="usuario_p")
    enfermedades=relationship("EnfermedadUsuario",back_populates="usuarios_e")
    rutinas_p=relationship("Rutina",back_populates="persona")
    progreso=relationship("ProgresoDiario",back_populates="usuario_pr")

class Ingrediente(Base):
    __tablename__='INGREDIENTE'
    id_ingrediente=Column(Integer,primary_key=True,index=True,autoincrement=True)
    nombre_ingrediente=Column(String)
    cantidad_calorias=Column(Integer)
    id_categoria=Column(Integer,ForeignKey('CATEGORIA_INGREDIENTE.id_categoria'))
    categoria=relationship("CategoriaIngrediente",back_populates="ingrediente")
    alergia=relationship("Alergia",back_populates="ingredient")
    receta=relationship("IngredienteReceta",back_populates="ingredientes")

class Estatura(Base):
    __tablename__='ESTATURA'
    id_estatura=Column(Integer,primary_key=True,index=True,autoincrement=True)
    estatura=Column(String)
    fecha_toma=Column(Date)
    id_usuario=Column(Integer,ForeignKey('USUARIO.id_usuario'))
    usuario_e=relationship("Usuario",back_populates="estaturas")

class Peso(Base):
    __tablename__ = 'PESO'
    id_peso = Column(Integer, primary_key=True, index=True, autoincrement=True)
    peso = Column(String)
    fecha_toma = Column(Date)
    id_usuario = Column(Integer, ForeignKey('USUARIO.id_usuario'))
    usuario_p = relationship("Usuario", back_populates="pesos")

class Alergia(Base):
    __tablename__='ALERGIA'
    id_usuario=Column(Integer,ForeignKey('USUARIO.id_usuario'),primary_key=True,index=True)
    id_ingrediente=Column(Integer,ForeignKey('INGREDIENTE.id_ingrediente'),primary_key=True,index=True)
    usuario=relationship("Usuario",back_populates='alergias')
    ingredient=relationship("Ingrediente",back_populates='alergia')

class IngredienteReceta(Base):
    __tablename__='INGREDIENTE_RECETA'
    id_receta=Column(Integer,ForeignKey('RECETA.id_receta'),primary_key=True,index=True)
    id_ingrediente=Column(Integer,ForeignKey('INGREDIENTE.id_ingrediente'),primary_key=True,index=True)
    cantidad_ingrediente=Column(Float)
    calorias_ingrediente=Column(Float)
    recetas=relationship("Receta",back_populates="ingredientes_r")
    ingredientes=relationship("Ingrediente",back_populates="receta")

class Enfermedad(Base):
    __tablename__='ENFERMEDAD'
    id_enfermedad=Column(Integer,primary_key=True,index=True,autoincrement=True)
    nombre_enfermedad=Column(String)
    usuarios=relationship("EnfermedadUsuario",back_populates="enfermedades_u")

class EnfermedadUsuario(Base):
    __tablename__='ENFERMEDAD_USUARIO'
    id_usuario=Column(Integer,ForeignKey('USUARIO.id_usuario'),primary_key=True,index=True)
    id_enfermedad=Column(Integer,ForeignKey('ENFERMEDAD.id_enfermedad'),primary_key=True,index=True)
    usuarios_e=relationship("Usuario",back_populates="enfermedades")
    enfermedades_u=relationship("Enfermedad",back_populates="usuarios")

class Objetivo(Base):
    __tablename__='OBJETIVO'
    id_objetivo=Column(Integer,primary_key=True,index=True,autoincrement=True)
    nombre_objetivo=Column(String)
    rutinas=relationship("Rutina",back_populates="objetivo")

class Rutina(Base):
    __tablename__='RUTINA'
    id_rutina=Column(Integer,primary_key=True,index=True,autoincrement=True)
    cantidad_comidas=Column(Integer)
    id_objetivo=Column(Integer,ForeignKey('OBJETIVO.id_objetivo'))
    calorias_diarias=Column(Float)
    vigente=Column(Integer)
    id_usuario=Column(Integer,ForeignKey('USUARIO.id_usuario'))
    objetivo=relationship("Objetivo",back_populates="rutinas")
    persona=relationship("Usuario",back_populates="rutinas_p")


class CategoriaIngrediente(Base):
    __tablename__='CATEGORIA_INGREDIENTE'
    id_categoria=Column(Integer,primary_key=True,index=True,autoincrement=True)
    nombre_categoria=Column(String)
    ingrediente=relationship("Ingrediente",back_populates="categoria")

class EstiloVida(Base):
    __tablename__='ESTILO_VIDA'
    id_estilo=Column(Integer,primary_key=True,index=True,autoincrement=True)
    nombre_estilo=Column(String)
    multiplicador=Column(Float)
    people=relationship("Usuario",back_populates="estilo")

class Receta(Base):
    __tablename__='RECETA'
    id_receta=Column(Integer,primary_key=True,index=True,autoincrement=True)
    nombre_receta=Column(String)
    tipo_comida=Column(String)
    preparacion=Column(String)
    url_imagen=Column(String)
    cantidad_calorias=Column(Float)
    ingredientes_r=relationship("IngredienteReceta",back_populates="recetas")

class ProgresoDiario(Base):
    __tablename__='PROGRESO_DIARIO'
    id_registro=Column(Integer,primary_key=True,index=True,autoincrement=True)
    fecha=Column(Date)
    id_usuario=Column(Integer,ForeignKey('USUARIO.id_usuario'))
    porcentaje_avance=Column(Float)
    usuario_pr=relationship("Usuario",back_populates="progreso")