from django.conf.urls import url

from apps.entrada.views import home

urlpatterns = [
    url(r'', home, name='home'),
    
]
