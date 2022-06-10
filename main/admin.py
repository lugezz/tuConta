from django.contrib import admin

from .models import Empresa, Impuesto, ImpXEmp, Feriado

admin.site.register(Empresa)
admin.site.register(Impuesto)
admin.site.register(ImpXEmp)
admin.site.register(Feriado)