from django.db import models

## ORM object realational model


# Create your models here.
class Post(models.Model):
    thumbnail = models.ImageField(upload_to="thumbnails")
    title = models.CharField(max_length=200)
    content = models.TextField()
