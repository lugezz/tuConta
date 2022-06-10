from django.urls import path

from .views import *

app_name = 'vencimientos'

urlpatterns = [
    #Generador Vencimientos
    path('generate', VenceGenerate.as_view(), name = 'generate'),
    #Vencimientos por impuesto
    path('vi/', VenceImpList.as_view(), name='vi_list'),
    path('vi/create', VenceImpCreate.as_view(), name = 'vi_create'),
    path('vi/<str:pk>/update', VenceImpUpdate.as_view(), name = 'vi_update'),
    path('vi/<str:pk>/delete', VenceImpDelete.as_view(), name = 'vi_delete'),
    
    #Vencimientos por cliente
    path('ve/', VenceEmpList.as_view(), name='ve_list'),
    path('ve/create', VenceEmpCreate.as_view(), name = 've_create'),
    path('ve/<str:pk>/update', VenceEmpUpdate.as_view(), name = 've_update'),
    path('ve/<str:pk>/delete', VenceEmpDelete.as_view(), name = 've_delete'),
]