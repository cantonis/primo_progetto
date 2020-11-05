from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Articolo, Giornalista

# Create your views here.


def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}

    return render(request, "home-news.html", context)
