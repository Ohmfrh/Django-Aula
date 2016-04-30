from django.http import HttpResponse
from django.shortcuts import render

from usuarios.models import Usersys
from imagenes.models import Image


# Create your views here.
def index(request):
    users = Usersys.objects.all()
    images = Image.objects.all()
    context = {'users': users, 'images': images}
    return render(request, 'imagenes/index.html', context)


def usuario(request):
    data = 'hola'
    HttpResponse(data)
