from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Articolo, Giornalista

# Create your views here.


def home(request):
    a = ""
    g = ""

    for art in Articolo.objects.all():
        a += art.titolo + "<br>"

    for gio in Giornalista.objects.all():
        g += gio.nome + " " + gio.cognome + "<br>"

    response = "Articoli:<br>" + a + "Giornalisti:<br>" + g

    return HttpResponse("<h1>" + response + "</h1>")
