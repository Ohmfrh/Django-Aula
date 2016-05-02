import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from usuarios.models import Usersys
from musica.models import Song, UserSong
from .forms import AddSong, SongForm
from multimedia.models import Server


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
    songs = Song.objects.all()
    add_song_form = AddSong()

    if request.method == 'POST':
        assign_song_form = SongForm(request.POST)
        if assign_song_form.is_valid():
            print "????"
            userId = request.POST['UserOwner']
            user = Usersys.objects.get(pk=userId)
            userSongs = UserSong.objects.all()
            userSongs = userSongs.filter(user=userId)

            for song in userSongs:
                print "IN SONG FOR"
                song.delete()
            print request.POST
            list = request.POST.getlist('Canciones')
            print list
            for item in list:
                print "LIST"
                song = Song.objects.get(pk=item)
                usrsng = UserSong(user=user, song=song)
                usrsng.save()


            return HttpResponseRedirect('/musica/')

    else:
        assign_song_form = SongForm()

    print "FOUR"
    context = {'users': users, 'images': songs, 'add_image_form': add_song_form, 'assign_image_form': assign_song_form}
    return render(request, 'musica/index.html', context)


def agregar(request):
    users = Usersys.objects.all()
    songs = Song.objects.all()
    assign_song_form = SongForm()

    if request.method == 'POST':
        add_song_form = AddSong(request.POST)
        print "information sent"

        if add_song_form.is_valid():
            print "Query stuff"
            path = request.POST['Path']
            name = request.POST['Name']
            serverId = request.POST['ServerList']

            server = Server.objects.get(pk=serverId)
            newSong = Song(name=name, path=path, server=server)

            newSong.save()
            
            return HttpResponseRedirect('/musica/')
    else:
        add_image_form = AddSong()

    context = {'users': users, 'images': songs, 'add_image_form': add_song_form, 'assign_image_form': assign_song_form}
    return render(request, 'musica/index.html', context)


def lista(request):
    list = []
    userId = request.GET['userId']
    songs = Song.objects.all()
    songs = songs.filter(users=userId)

    for row in songs:
        list.append({'songId': row.pk})

    # data = serializers.serialize("json", list)
    data = json.dumps(list)

    # data['user'] = Usersys.objects.get(pk=userId)
    return HttpResponse(data, content_type='application/json')
