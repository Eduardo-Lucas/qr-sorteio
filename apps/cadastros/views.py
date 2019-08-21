from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from apps.cadastros.models import Cadastro

# TODO: OK - Botão para criar registro
# TODO: OK - Paginação
# TODO: OK - Campo de Pesquisa
# TODO: OK - Quantidade de registros na tela
# TODO: Biblioteca para gerar planilha Excel


class CadastroListView(ListView):
    model = Cadastro
    fields = ['nome_completo', 'email', 'telefone', ]
    template_name = 'cadastros/cadastro_list.html'
    
    def get_queryset(self):
        valor = self.request.GET.get('q')
        if valor:
            object_list = self.model.objects.filter(
                Q(nome_completo__icontains=valor) |
                Q(email__icontains=valor) |
                Q(telefone__icontains=valor)
            )
        else:
            object_list = self.model.objects.all()

        paginator = Paginator(object_list, 15)

        page = self.request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)

        # return object_list
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super(CadastroListView, self).get_context_data(**kwargs)
        context['count'] = Cadastro.objects.count()
        return context
    
    
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
