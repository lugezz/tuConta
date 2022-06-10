from django.db import models

from main.models import Empresa, Impuesto

class ReglaVencimiento(models.Model):
    #Si todas son la misma fecha no genera un registro, por ejemplo Com e Ind día 15
    impuesto = models.ForeignKey(Impuesto, on_delete=models.CASCADE)
    cuit_d = models.IntegerField(default=0)
    cuit_h = models.IntegerField(default=9)
    dia = models.IntegerField() #Si no está es día inicio y luego suma a este

    def __str__(self):
        return f'{self.impuesto} - {self.cuit_d} a {self.cuit_h} - Día {self.dia}'
    
    class Meta:
        ordering = ['impuesto', 'dia']

class Venc_Imp(models.Model):
    periodo = models.DateField() #dia 1 del mes o del año
    impuesto = models.ForeignKey(Impuesto, on_delete=models.CASCADE)
    cuit_d = models.IntegerField(default=0)
    cuit_h = models.IntegerField(default=9)
    fecha = models.DateField()

    def __str__(self):
        return f'{self.periodo.strftime("%m/%Y")} - {self.impuesto} - {self.fecha.strftime("%d/%m/%Y")}'

class Venc_Cli (models.Model):
    periodo = models.DateField() #dia 1 del mes o del año
    impuesto = models.ForeignKey(Impuesto, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f'{self.empresa} - {self.impuesto} - {self.periodo.strftime("%m/%Y")}'
