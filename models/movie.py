from config.database import Base #se llama a la config
from sqlalchemy import Column, Integer, String, Float #se exporta

class Movie(Base): #se hereda de base

    __tablename__ = "movies"
 #campos de la tabla
    id = Column(Integer, primary_key = True) #primary key: clave primaria
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
