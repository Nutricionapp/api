from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from NutricionApp.database import Base
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__='USUARIO'
    id_usuario=Column(Integer,primary_key=True,index=True,autoincrement=True)
    nombre_usuario=Column(String)
    fecha_nacimiento=Column(Date)
    id_estilo_vida=Column(Integer,ForeignKey('ESTILO_VIDA.id_estilo'))
    estilo=relationship("EstiloVida",back_populates="people")
    alergias=relationship("Alergia",back_populates="usuario")
    estaturas=relationship("Estatura",back_populates="usuario_e")
    pesos=relationship("Peso",back_populates="usuario_p")

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
    recetas=relationship("Receta",back_populates="ingredientes_r")
    ingredientes=relationship("Ingrediente",back_populates="receta")



class CategoriaIngrediente(Base):
    __tablename__='CATEGORIA_INGREDIENTE'
    id_categoria=Column(Integer,primary_key=True,index=True,autoincrement=True)
    nombre_categoria=Column(String)
    ingrediente=relationship("Ingrediente",back_populates="categoria")

class EstiloVida(Base):
    __tablename__='ESTILO_VIDA'
    id_estilo=Column(Integer,primary_key=True,index=True,autoincrement=True)
    nombre_estilo=Column(String)
    people=relationship("Usuario",back_populates="estilo")

class Receta(Base):
    __tablename__='RECETA'
    id_receta=Column(Integer,primary_key=True,index=True,autoincrement=True)
    nombre_receta=Column(String)
    tipo_comida=Column(String)
    preparacion=Column(String)
    ingredientes_r=relationship("IngredienteReciente",back_populates="recetas")