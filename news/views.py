from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Articolo, Giornalista

# Create your views here.


def home(request):
    a = []
    g = []

    for art in Articolo.objects.all():
        a.append(art.titolo)

    for gio in Giornalista.objects.all():
        g.append(gio.nome + " " + gio.cognome)

    response = str(a) + "<br>" + str(g)

    return HttpResponse("<h1>" + response + "</h1>")
