from django.db import models


# Create your models here.

class Message(models.Model):
    email = models.EmailField()

    author_name = models.CharField(max_length=20)

    content = models.TextField()

    published_time = models.DateTimeField()
