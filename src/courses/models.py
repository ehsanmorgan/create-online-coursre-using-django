from django.db import models
from taggit.managers import TaggableManager


# Create your models here.

class course(models.Model):
    title=models.CharField(max_length=100)
    
    content=models.TextField(max_length=100000)
    sub_title=models.TextField()
    author=models.CharField(max_length=100)
    reviwes=models.TextField()
    tags = TaggableManager()





    













    def __str__(self):
        return self.title