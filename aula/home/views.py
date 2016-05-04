from django.shortcuts import render
from usuarios.models import Usersys

# Create your views here.
def index(request):
    users = Usersys.objects.all()
    context = {'users': users}
    return render(request, 'home/index.html', context)
