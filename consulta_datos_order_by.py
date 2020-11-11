from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Saludo

# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///demobase2.db')

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la tabla saludo ordenados por el atribut
# mensaje
losSaludos = session.query(Saludo).order_by(Saludo.mensaje)
# la consulta con .order_by, ordena los resultados en función del 
# atributo de la clase Saludo, mensaje, 
# Devuelve una lista de objetos de tipo Saludo
# y se le asigna como valor a la variable
# losSaludos

# Se recorre la lista a través de un ciclo
# repetitivo for en python

for s in losSaludos:
    print("Mensaje: %s" % (s.mensaje))
    print("Tipo: %s" % (s.tipo))
    print("id: %s" % (s.id))
    print("---------")
