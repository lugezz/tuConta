from django.db import models

class Impuesto(models.Model):
    nombre = models.CharField(max_length=100)

    MENSUAL = 1
    SEMANAL = 2
    QUINCENAL = 3
    TRIMESTRAL = 4
    ANUAL = 12
    
    PERIOD_CHOICES = (
        ( MENSUAL, 'Mensual'),
        ( SEMANAL, 'Semanal' ),
        ( QUINCENAL, 'Quincenal' ),
        ( TRIMESTRAL, 'Trimestral' ),
        ( ANUAL, 'Anual' ),
    )
    
    periodicidad = models.IntegerField(
        choices=PERIOD_CHOICES,
        default=MENSUAL,
    )
    ini_venc = models.IntegerField(default=10)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']


class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    cuit = models.CharField(max_length=11)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    mes_cierre = models.IntegerField(default=12)
    impuestos = models.ManyToManyField(Impuesto, through='ImpXEmp', related_name="impuestos_x_empresa")

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']

class ImpXEmp (models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    impuesto = models.ForeignKey(Impuesto, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.empresa} - {self.impuesto}'

class Feriado (models.Model):
    fecha = models.DateField(unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.fecha.strftime("%d/%m/%Y")} - {self.nombre}'

    class Meta:
        ordering = ['fecha']
    
