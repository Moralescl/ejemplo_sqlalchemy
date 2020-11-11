from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Saludo

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///demobase2.db')

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la tabla saludo
losSaludos = session.query(Saludo).all()
# la consulta con .all(), devuelve
# una lista de objetos de tipo Saludo
# que se le asigna como valor a la variable
# losSaludos
# Se recorre la lista a través de un ciclo
# repetitivo for en python

for s in losSaludos:
    print(s.mensaje)
    print(s.tipo)
    print("---------")
