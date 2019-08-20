from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView, DeleteView

from apps.cadastros.models import Cadastro


class CadastroListView(ListView):
    model = Cadastro
    fields = ['nome_completo', 'email', 'telefone', ]
    

class CadastroCreateView(SuccessMessageMixin, CreateView):
    model = Cadastro
    fields = ['nome_completo', 'email', 'telefone', ]
    success_message = 'O cadastro de %(nome_completo)s foi realizado com sucesso.'
    

class CadastroUpdateView(SuccessMessageMixin, UpdateView):
    model = Cadastro
    fields = ['nome_completo', 'email', 'telefone', ]
    success_message = 'O cadastro de %(nome_completo)s foi alterado com sucesso.'

    
class CadastroDetailView(DetailView):
    model = Cadastro
    template_name = 'cadastros/cadastro_detail.html'
    

class CadastroDeleteView(DeleteView):
    model = Cadastro
    success_url = reverse_lazy('cadastro_list')
