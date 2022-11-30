from django.db import models


# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='image')
    desc=models.TextField()


