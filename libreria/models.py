from django.db import models
from django.urls import reverse

# Create your models here.


class Genere_CS(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Genere"
        verbose_name_plural = "Generi"


class Autore_CS(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    nazione = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + " " + self.cognome

    def get_absolute_url(self):
        return reverse("libreria:autore_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Autore"
        verbose_name_plural = "Autori"


class Libro_CS(models.Model):
    titolo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    autore = models.ForeignKey(
        Autore_CS, on_delete=models.CASCADE, related_name="libri")
    genere = models.ManyToManyField(Genere_CS)

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libri"
