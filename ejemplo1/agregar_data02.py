from sqlalchemy.orm import sessionmaker

from crear_base import Saludo2
from configuracion import engine
import csv

Session = sessionmaker(bind=engine)
session = Session()


lista_datos = []
with open('data/saludos_mundo.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')  # usa '|' como delimitador
    reader.fieldnames = [campo.strip() for campo in reader.fieldnames]  # limpia encabezados

    for row in reader:
        fila_limpia = {k.strip(): v.strip() for k, v in row.items()}  # limpia claves y valores
        lista_datos.append(fila_limpia)


for i in range(len(lista_datos)):
    miSaludo = Saludo2()
    miSaludo.mensaje = (lista_datos[i]['saludo'])
    miSaludo.tipo = (lista_datos[i]['tipo'])
    miSaludo.origen = (lista_datos[i]['origen'])
    session.add(miSaludo)

session.commit()
