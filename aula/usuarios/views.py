from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Usersys

from .forms import NameForm


# Create your views here.
def index(request):
    users = Usersys.objects.all()

    # print request
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            print request.POST['name']
            print request.POST['last_names']
            print request.POST['email']
            try:
                newUser = Usersys(name=request.POST['name'], last_names=request.POST['last_names'], email=request.POST['email'])
                newUser.save()
            except:
                print ":("

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/usuarios/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    context = {'users': users, 'form': form}
    return render(request, 'usuarios/index.html', context)


def nuevo(request):
    print request
    context = ""
    return render(request, 'usuarios/index.html', context)

