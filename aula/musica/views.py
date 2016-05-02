import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from usuarios.models import Usersys
from musica.models import Song
from .forms import AddSong, SongForm


# Create your views here.
def index(request):
    users = Usersys.objects.all()
    songs = Song.objects.all()

    add_song_form = AddSong()
    assign_song_form = SongForm()

    context = {'users': users, 'songs': songs, 'add_song_form': add_song_form, 'assign_song_form': assign_song_form}
    return render(request, 'musica/index.html', context)


def usuario(request):
    users = Usersys.objects.all()
    images = Image.objects.all()
    add_image_form = AddImage()

    if request.method == 'POST':
        assign_image_form = ImageForm(request.POST)
        if assign_image_form.is_valid():
            userId = request.POST['UserOwner']
            user = Usersys.objects.get(pk=userId)
            userImages = UserImage.objects.all()
            userImages = userImages.filter(user=userId)

            for img in userImages:
                img.delete()

            list = request.POST.getlist('musica')
            for item in list:
                img = Image.objects.get(pk=item)
                usrimg = UserImage(user=user, image=img)
                usrimg.save()


            return HttpResponseRedirect('/musica/')

    else:
        assign_image_form = ImageForm()

    print "FOUR"
    context = {'users': users, 'images': images, 'add_image_form': add_image_form, 'assign_image_form': assign_image_form}
    return render(request, 'musica/index.html', context)


def agregar(request):
    users = Usersys.objects.all()
    images = Image.objects.all()
    assign_image_form = ImageForm()

    if request.method == 'POST':
        add_image_form = AddImage(request.POST)
        print "information sent"

        if add_image_form.is_valid():
            print "Query stuff"
            path = request.POST['Path']
            name = request.POST['Name']
            serverId = request.POST['ServerList']

            server = Server.objects.get(pk=serverId)
            newImage = Image(name=name, path=path, server=server)

            newImage.save()
            
            return HttpResponseRedirect('/musica/')
    else:
        add_image_form = AddImage()

    context = {'users': users, 'images': images, 'add_image_form': add_image_form, 'assign_image_form': assign_image_form}
    return render(request, 'musica/index.html', context)


def lista(request):
    list = []
    userId = request.GET['userId']
    images = Image.objects.all()
    images = images.filter(users=userId)

    for row in images:
        list.append ({'imageId': row.pk})

    # data = serializers.serialize("json", list)
    data = json.dumps(list)

    # data['user'] = Usersys.objects.get(pk=userId)
    return HttpResponse(data, content_type='application/json')
