from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    
    topic = models.CharField( max_length=100)
    link = models.URLField()
    status = models.CharField(max_length=50)
    date = models.DateTimeField( auto_now= True )
    author = models.ForeignKey(
        User,
        on_delete= models.CASCADE,
    )
    def __str__(self):
        return self.topic


class Editor(models.Model):
    topic = models.CharField( max_length=100)
    
    sermon = models.CharField(max_length=50)
    date = models.DateTimeField( auto_now= True )

    def __str__(self):
        return self.topic
