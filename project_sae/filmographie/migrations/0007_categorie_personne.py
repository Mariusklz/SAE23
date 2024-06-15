# Generated by Django 5.0.6 on 2024-05-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmographie', '0006_rename_acteurs_acteur_rename_films_film'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('descriptif', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=100, unique=True)),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('prenom', models.CharField(max_length=100, unique=True)),
                ('mail', models.EmailField(max_length=254, unique=True)),
                ('mdp', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('professionnel', 'Professionnel'), ('amateur', 'Amateur')], max_length=20)),
            ],
        ),
    ]
