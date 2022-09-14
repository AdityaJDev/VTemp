from django.db import models


class Blogger(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Blog(models.Model):
    text = models.CharField(max_length=255)
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
