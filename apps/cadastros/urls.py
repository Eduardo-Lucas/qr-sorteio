from django.conf.urls import url

from apps.cadastros.views import CadastroCreateView, CadastroDetailView, CadastroListView, \
    CadastroUpdateView, CadastroDeleteView

urlpatterns = [
    url(r'^list', CadastroListView.as_view(), name='cadastro_list'),
    url(r'^create', CadastroCreateView.as_view(), name='cadastro_create'),
    url(r'^detail/(?P<pk>\d+)/$', CadastroDetailView.as_view(), name='cadastro_detail'),
    url(r'^edit/(?P<pk>\d+)/$', CadastroUpdateView.as_view(), name='cadastro_edit'),
    url(r'^delete/(?P<pk>\d+)/$', CadastroDeleteView.as_view(), name='cadastro_delete'),
    
]
