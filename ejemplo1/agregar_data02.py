from sqlalchemy.orm import sessionmaker

from crear_base import Saludo2
from configuracion import engine
import csv

Session = sessionmaker(bind=engine)
session = Session()


lista_datos = []
# Leer el archivo CSV y cargar los datos en una lista de diccionarios
with open('data/saludos_mundo.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lista_datos.append(row)

for i in range(len(lista_datos)):
    miSaludo = Saludo2()
    miSaludo.saludo = (lista_datos[i]['saludo'])
    miSaludo.tipo = (lista_datos[i]['tipo'])
    miSaludo.origen = (lista_datos[i]['origen'])
    session.add(miSaludo)

session.commit()
