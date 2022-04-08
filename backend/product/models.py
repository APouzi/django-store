from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(blank=True, max_length = 150)
    description = models.TextField(blank=True)
    inv_num = models.IntegerField(null = True)
    
    def __str__(self):
        return f'{self.name} and id is: {self.id}'


