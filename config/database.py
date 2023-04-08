import os
from sqlalchemy import create_engine #motor bd
from sqlalchemy.orm.session import sessionmaker #crear sesion
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = "../database.sqlite" #nombre base de datos
base_dir = os.path.dirname(os.path.realpath(__file__)) #direccion bd

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}" #llamas a la bd y unes el name y la direccion

engine = create_engine(database_url, echo=True) #crear motor bd // echo dice por consola lo que esta haciendo

Session = sessionmaker(bind=engine) #crear sesion para conectarte a la db // bind se enlaza al motor de la bd

Base = declarative_base() #una instancia