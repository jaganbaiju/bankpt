from django.db import models

# Create your models here.
class MainDetails(models.Model):
    img=models.ImageField(upload_to='mainimage')
    heading=models.CharField(max_length=250)
    desc=models.TextField(default=True)

    def __str__(self):
        return self.heading

class Faclities(models.Model):
    img=models.ImageField(upload_to='faclities')
    name=models.CharField(max_length=250)
    desc=models.TextField()

    def __str__(self):
        return self.name