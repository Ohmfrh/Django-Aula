from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from usuarios.models import Usersys
from imagenes.models import Image
from .forms import AddImage


# Create your views here.
def index(request):
    users = Usersys.objects.all()
    images = Image.objects.all()
    form = AddImage()
    context = {'users': users, 'images': images, 'form': form}
    return render(request, 'imagenes/index.html', context)


def usuario(request):
    data = 'From View'

    return HttpResponse(data)


def agregar(request):
    users = Usersys.objects.all()
    images = Image.objects.all()
    if request.method == 'POST':
        form = AddImage(request.POST)
        print "information sent"

        if form.is_valid():
            print "Query stuff"

            return HttpResponseRedirect('/musica/')
    else:
        form = AddImage()

    context = {'users': users, 'images': images, 'form': form}
    return render(request, 'musica/index.html', context)
