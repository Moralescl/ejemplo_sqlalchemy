from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

from genera_tablas import Saludo

# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///demobase2.db')

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la tabla saludo que tengan la vocal "o" en el atributo mensaje
# y sean de tipo "informal"
losSaludos = session.query(Saludo).filter(and_(Saludo.mensaje.like("%o%"), \
        Saludo.tipo=="informal")) 
# a la consulta con .filter 
# se le agrega una expresión lógica AND
# la primera parte de la expresión usa el 
# operador like para determinar todos los registros
# que tengan la vocal "o" en el atributo mensaje;
# la segunda parte de la expresión, filtra todos 
# los registros que tienen como valor en el atributo tipo
# "informal"
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
