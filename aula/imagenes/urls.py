from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^usuario/$', views.usuario, name='usuario'),
    url(r'^agregar/$', views.agregar, name='agregar'),
]
