from django.http import HttpResponseRedirect
from django.shortcuts import render
from usuarios.models import Usersys

from .models import Type, Identify
from .forms import AddId


# Create your views here.
def index(request):
    users = Usersys.objects.all()

    form = AddId()

    context = {'users': users, 'form': form}
    return render(request, 'identificacion/index.html', context)


def nuevo(request):
    users = Usersys.objects.all()

    # print request
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddId(request.POST)

        # check whether it's valid:
        if form.is_valid():
            rfid = Type.objects.get(name='rfid')
            user = Usersys.objects.get(pk=request.POST['Usuario'])
            new = Identify(string=request.POST['String'], usersys=user, type=rfid)
            new.save()

            print rfid
            print user


            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/identificacion/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddId()

    context = {'users': users, 'form': form}
    return render(request, 'identificacion/index.html', context)