from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Articolo, Giornalista

# Create your views here.


def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}

    return render(request, "home-news.html", context)


def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}

    return render(request, "articolo-detail.html", context)
