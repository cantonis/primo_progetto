from django.contrib import admin

# Register your models here.

from .models import Giornalista, Articolo

admin.site.register(Giornalista)
admin.site.register(Articolo)
