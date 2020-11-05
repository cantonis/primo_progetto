from django.urls import path
from .views import home, articoloDetailViewCB

app_name = "news"

urlpatterns = [
    path("", home, name="homeview"),
    path("articoli/<int:pk>", articoloDetailViewCB.as_view(), name="articolo_detail")
]
