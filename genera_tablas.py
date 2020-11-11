from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///demobase2.db')

Base = declarative_base()

class Saludo(Base):
    __tablename__ = 'saludo'
    #  __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    mensaje = Column(String)
    tipo = Column(String)

Base.metadata.create_all(engine)
