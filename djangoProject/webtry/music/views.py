from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import album 
from .models import song 
from django.shortcuts import get_object_or_404
# Create your views here.

new_album= album.objects.all()

def index(request):
    return render(request,"music/index.html",{"albums":new_album})

def detail(request,number):
    albumx=get_object_or_404(album,pk=number)
    return render(request,"music/detail.html",{"album":albumx})

def favorite(request,number):
    #Write the code here that new boston wrote .
    albumnew=get_object_or_404(album,pk=number)
    try:
        selected_song=albumnew.song_set.get(pk=request.POST['song'])
    except (KeyError,song.DoesNotExist):
        return render(request,"music/detail.html",{
            "album":albumnew,
            "error_message":"You did not select a song or song selection is not valid"
            })
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request,"music/detail.html",{"album":new_album})