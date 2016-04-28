from django.shortcuts import render
from .models import Usersys

# Create your views here.
def index(request):
    users = Usersys.objects.all()
    context = {'users': users}

    return render(request, 'usuarios/index.html', context)

def nuevo(request):
    #print request
    print "NUEVOOO"
    users = Usersys.objects.all()
    context = {'users': users}

    return render(request, 'usuarios/index.html', context)
