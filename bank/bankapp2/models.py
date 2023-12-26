from django.db import models

# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Branch(models.Model):
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class type(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name


class Data(models.Model):
    name = models.CharField(max_length=300)
    dob = models.DateField()
    age = models.IntegerField(default=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='male',
    )
    phone = models.CharField(max_length=300)
    mail = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True,null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True,null=True)
    account_type=models.ForeignKey(type,on_delete=models.SET_NULL,blank=True,null=True)
    material = models.ManyToManyField('Material',blank=True)

    def __str__(self):

        return self.name

class Material(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Gender(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name