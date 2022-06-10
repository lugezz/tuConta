from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView

from .models import Empresa, Impuesto

class MainView(View):
    def get(self, request):
        context = {}

        return render(request, 'main/main.html', context)


# Empresas ---------------------------------------------------------------
class EmpresaList(ListView):
    model = Empresa

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['create_url'] = reverse_lazy('empresa_create')
        context['list_url'] = reverse_lazy('empresas_list')
        context['entity'] = 'Clientes'
        return context
    
class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nombre', 'cuit', 'direccion', 'mes_cierre']

    def get_success_url(self):
        return reverse_lazy ('empresas_list')
    
    def get_context_data(self, **kwargs):
        impuestos = Impuesto.objects.all()
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Cliente'
        context['list_url'] = reverse_lazy('empresas_list')
        context['entity'] = 'Clientes'
        context['action'] = 'add'
        context['impuestos'] = impuestos
        return context

class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = ['nombre', 'cuit', 'direccion', 'mes_cierre', 'impuestos']

    def get_success_url(self):
        return reverse_lazy ('empresas_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Cliente'
        context['list_url'] = reverse_lazy('empresas_list')
        context['entity'] = 'Clientes'
        context['action'] = 'edit'
        return context

class EmpresaDelete(DeleteView):
    model = Empresa

    def get_success_url(self):
        return reverse_lazy ('empresas_list')
