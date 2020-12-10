from django.urls.conf import path
from .views import LibroList_CS, AutoreDetail_CS, AutoreList_CS

app_name = "libreria"

urlpatterns = [
    path("", LibroList_CS.as_view(), name="lista_libri"),
    path("autori/<int:pk>", AutoreDetail_CS.as_view(), name="autore_detail"),
    path("autori", AutoreList_CS.as_view(), name="lista_autori")
]
