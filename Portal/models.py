from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

HOUSE_CHOICES = [
    ('NONE', 'None'),
    ('AMON RE', 'Amonre'),
    ('SURYAS', 'Suryas'),
    ('HELIOS', 'Helios'),
    ('MITHRAS', 'Mithras'),
    ('SOL', 'Sol')
]

class Voter(AbstractUser):
    name = models.CharField(max_length=50)
    class_sec = models.CharField(max_length=50)
    house = models.CharField(max_length=50, choices=HOUSE_CHOICES , default='NONE')
    stage = models.CharField(max_length=50, default='index')

    def __str__(self):
        return self.username

class Post(models.Model):

    POST_TYPES = [
        ('General', 'General Elections'),
        ('House', 'House Elections')
    ]

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=POST_TYPES , default='General')

    def __str__(self):
        return self.name

class Nominee(models.Model):

    name = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    house = models.CharField(max_length=50, choices=HOUSE_CHOICES , default='NONE')
    votes = models.PositiveIntegerField(default=0)
    symbol = models.CharField(max_length=50)

    def __str__(self):
        return self.name
