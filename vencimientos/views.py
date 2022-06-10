from datetime import datetime, timedelta
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, TemplateView

from .models import Venc_Imp, Venc_Cli

#Vencimientos por impuesto ------------------------------------
class VenceImpList(ListView):
    model = Venc_Imp

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Vencimientos por Impuesto'
        context['create_url'] = reverse_lazy('vencimientos:vi_create')
        context['list_url'] = reverse_lazy('vencimientos:vi_list')
        context['entity'] = 'Vencimientos por Impuesto'
        return context
    
class VenceImpCreate(CreateView):
    model = Venc_Imp
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy ('vencimientos:vi_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Vencimiento'
        context['list_url'] = reverse_lazy('vencimientos:vi_list')
        context['entity'] = 'Vencimientos por Impuesto'
        context['action'] = 'add'
        return context

#class VenceImpDetail(DetailView):
#    model = Venc_Imp
# Por el momento no es necesario

class VenceImpUpdate(UpdateView):
    model = Venc_Imp
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy ('vencimientos:vi_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Vencimiento'
        context['list_url'] = reverse_lazy('vencimientos:vi_list')
        context['entity'] = 'Vencimientos por Impuesto'
        context['action'] = 'edit'
        return context

class VenceImpDelete(DeleteView):
    model = Venc_Imp

    def get_success_url(self):
        return reverse_lazy ('vencimientos:vi_list')

#Vencimientos por cliente ------------------------------------
class VenceEmpList(ListView):
    model = Venc_Cli

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Vencimientos por Empresa'
        context['create_url'] = reverse_lazy('vencimientos:ve_create')
        context['list_url'] = reverse_lazy('vencimientos:ve_list')
        context['entity'] = 'Vencimientos por Empresa'
        return context
    
class VenceEmpCreate(CreateView):
    model = Venc_Cli
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy ('vencimientos:ve_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Vencimiento'
        context['list_url'] = reverse_lazy('vencimientos:ve_list')
        context['entity'] = 'Vencimientos por Empresa'
        context['action'] = 'add'
        return context

#class VenceEmpDetail(DetailView):
#    model = Venc_Cli
# Por el momento no es necesario

class VenceEmpUpdate(UpdateView):
    model = Venc_Cli
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy ('vencimientos:ve_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Vencimiento'
        context['list_url'] = reverse_lazy('vencimientos:ve_list')
        context['entity'] = 'Vencimientos por Empresa'
        context['action'] = 'edit'
        return context

class VenceEmpDelete(DeleteView):
    model = Venc_Cli

    def get_success_url(self):
        return reverse_lazy ('vencimientos:ve_list')

#Generate ------------------------------------
class VenceGenerate(TemplateView):
    template_name = 'vencimientos/venc_generate.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # start_month = datetime.today().replace(day=1)

        # if start_month.month == 12:
        #     end_month = start_month.replace(day=1)
        # else:
        #     end_month = start_month.replace(month=start_month.month+1) - timedelta(days=1)
         
        # context['desde'] = start_month
        # context['hasta'] = end_month
        return context

