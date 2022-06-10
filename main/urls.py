from django.urls import path

from .views import *

# Sólo para deploy .........
from django.conf import settings
from django.conf.urls.static import static
#  .........

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('clientes/', EmpresaList.as_view(), name='empresas_list'),
    path('clientes/create', EmpresaCreate.as_view(), name = 'empresa_create'),
    path('clientes/<str:pk>/update', EmpresaUpdate.as_view(), name = 'empresa_update'),
    path('clientes/<str:pk>/delete', EmpresaDelete.as_view(), name = 'empresa_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)