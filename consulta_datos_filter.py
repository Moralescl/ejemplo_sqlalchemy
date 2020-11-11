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
# la tabla saludo que tengan como valor en 
# el atributo tipo la expresión "formal"
losSaludos = session.query(Saludo).filter(Saludo.tipo=="formal")
# la consulta con .filter con argumento 
# Saludo.tipo=="formal"
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
