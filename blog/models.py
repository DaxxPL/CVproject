from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.datetime.now())
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts')


    def __str__(self):
        return self.title

