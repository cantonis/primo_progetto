# Generated by Django 3.1.2 on 2020-12-09 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autore_cs',
            options={'verbose_name': 'Autore', 'verbose_name_plural': 'Autori'},
        ),
        migrations.AlterModelOptions(
            name='genere_cs',
            options={'verbose_name': 'Genere', 'verbose_name_plural': 'Generi'},
        ),
        migrations.AlterModelOptions(
            name='libro_cs',
            options={'verbose_name': 'Libro', 'verbose_name_plural': 'Libri'},
        ),
    ]
