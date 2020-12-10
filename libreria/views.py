from django.urls.base import reverse
from libreria.models import Autore_CS, Libro_CS
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.


class AutoreDetail_CS(DetailView):
    model = Autore_CS
    template_name = "dettaglio_autore.html"


class AutoreList_CS(ListView):
    model = Autore_CS
    template_name = "autore_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["autori"] = Autore_CS.objects.all()
        return context


class LibroList_CS(ListView):
    model = Libro_CS
    template_name = "libro_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["libri"] = Libro_CS.objects.all()
        return context
