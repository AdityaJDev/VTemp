from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=15)


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.CharField(max_length=255)
