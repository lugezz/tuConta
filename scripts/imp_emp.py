import csv  # https://docs.python.org/3/library/csv.html
from main.models import Empresa, Impuesto, ImpXEmp

def run():
    fhand = open('exporta/impxemp.csv')
    reader = csv.reader(fhand, delimiter=';')
    next(reader)  # Advance past the header

    #Person.objects.all().delete()
    #Course.objects.all().delete()
    #Membership.objects.all().delete()

    for row in reader:
        print(row)

        e, created = Empresa.objects.get_or_create(cuit=row[1], nombre=row[0])
        i, created = Impuesto.objects.get_or_create(nombre=row[2])

        m = ImpXEmp(empresa=e, impuesto=i)
        m.save()
