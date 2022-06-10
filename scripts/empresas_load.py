import csv  # https://docs.python.org/3/library/csv.html

from main.models import Empresa, Feriado

def run():
    fhand = open('exporta/empresas.csv')
    reader = csv.reader(fhand, delimiter=';')
    next(reader)  # Advance past the header

    Empresa.objects.all().delete() #Opcional
    
    for row in reader:
        print(row)

        c = Empresa.objects.create(nombre = row[0], cuit = row [1])
        c.save()
