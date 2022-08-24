from django.db import models

from django.contrib.auth.models import User

class Food(models.Model):
    title =models.CharField(max_length=100)
    fname = models.CharField(max_length=100,null=True )
    lname = models.CharField(max_length=100,null=True)
    phone_number = models.CharField(max_length=100,null=True)
    address = models.TextField(null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    quantity = models.IntegerField(null=True)
    comment = models.TextField(null=True)
    status = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title