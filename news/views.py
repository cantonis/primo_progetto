from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.detail import DetailView

from .models import Articolo, Giornalista

# Create your views here.


def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}

    return render(request, "home-news.html", context)


class articoloDetailViewCB(DetailView):
    model = Articolo
    template_name = "articolo-detail.html"
