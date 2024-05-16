from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name



class CustomUser(AbstractUser):
    TYPE_CHOICES = (
        ('professionnel', 'Professionnel'),
        ('amateur', 'Amateur'),
    )

    pseudo = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return self.pseudo, self.type