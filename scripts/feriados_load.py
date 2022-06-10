import csv  # https://docs.python.org/3/library/csv.html

from main.models import Empresa, Feriado
from datetime import datetime

def run():
    fhand = open('exporta/feriados.csv')
    reader = csv.reader(fhand, delimiter=';')
    next(reader)  # Advance past the header

    Feriado.objects.all().delete() #Opcional
    
    for row in reader:
        print(row)
        #row[0] viene como día-mm-año
        mFecha = datetime.strptime(row[0], '%d/%m/%Y')

        c = Feriado.objects.create(fecha = mFecha, nombre = row [1])
        c.save()
