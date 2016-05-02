from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Server
from .forms import ServerForm


# Create your views here.
def index(request):
    servers = Server.objects.all()
    form = ServerForm()

    context = {'servers': servers, 'form': form}
    return render(request, 'multimedia/index.html', context)


def crear(request):
    print request.POST
    servers = Server.objects.all()
    if request.method == 'POST':
        form = ServerForm(request.POST)

        if form.is_valid():
            print "SUCCESS"
            usr = request.POST['usuario']
            passwd = request.POST['contrasena']
            addr = request.POST['direccion']

            print usr + ' ' + passwd + ' ' + addr
            newServer = Server(address=addr, user=usr, password=passwd)
            newServer.save()

            return HttpResponseRedirect('/multimedia/')
    else:
        form = ServerForm()


    context = {'servers': servers, 'form': form}
    return render(request, 'multimedia/index.html', context)


