# Generated by Django 5.0.6 on 2024-05-16 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmographie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acteurs',
            name='photos',
            field=models.ImageField(upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='films',
            name='affiche',
            field=models.ImageField(upload_to='affiches/'),
        ),
    ]