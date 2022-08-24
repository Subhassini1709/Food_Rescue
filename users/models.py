from django.db import models

class volunteer(models.Model):
    name = models.CharField(max_length=100,null=True )
    phone_number = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)
    status = models.TextField()
    
    def __str__(self):
        return self.name
