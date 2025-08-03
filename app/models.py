from django.db import models

# Create your models here.
class database(models.Model):
    name=models.CharField(max_length=30)
    images=models.ImageField( upload_to='images')

    def __str__(self):
        return self.name
    
