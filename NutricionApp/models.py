from sqlalchemy import Column, Integer, String, ForeignKey, Date
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

class Ingrediente(Base):
    __tablename__='INGREDIENTE'
    id_ingrediente=Column(Integer,primary_key=True,index=True,autoincrement=True)
    nombre_ingrediente=Column(String)
    cantidad_calorias=Column(Integer)
    id_categoria=Column(Integer,ForeignKey('CATEGORIA_INGREDIENTE.id_categoria'))
    categoria=relationship("CategoriaIngrediente",back_populates="ingrediente")
    alergia=relationship("Alergia",back_populates="ingrediente")

class Alergia(Base):
    __tablename__='ALERGIA'
    id_usuario=Column(Integer,ForeignKey('USUARIO.id_usuario'),primary_key=True,index=True)
    id_ingrediente=Column(Integer,ForeignKey('INGREDIENTE.id_ingrediente'),primary_key=True,index=True)
    usuario=relationship("Usuario",back_populates='alergias')
    ingrediente=relationship("Ingrediente",back_populates='alergia')

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