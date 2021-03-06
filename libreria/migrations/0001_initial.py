# Generated by Django 3.1.2 on 2020-12-09 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autore_CS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('cognome', models.CharField(max_length=20)),
                ('nazione', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Genere_CS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Libro_CS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13)),
                ('autore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libri', to='libreria.autore_cs')),
                ('genere', models.ManyToManyField(to='libreria.Genere_CS')),
            ],
        ),
    ]
