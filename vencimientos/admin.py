from django.contrib import admin

from .models import Venc_Cli, Venc_Imp, ReglaVencimiento

admin.site.register(Venc_Cli)
admin.site.register(Venc_Imp)
admin.site.register(ReglaVencimiento)
