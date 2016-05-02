from django.shortcuts import render

from .models import Server


# Create your views here.
def index(request):
    servers = Server.objects.all()

    context = {'servers': servers}
    return render(request, 'multimedia/index.html', context)
