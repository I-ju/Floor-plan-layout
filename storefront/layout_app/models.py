from django.db import models

class Furniture(models.Model):
    x = models.FloatField(default=0)      
    y = models.FloatField(default=0)
    width = models.FloatField(default=50)
    height = models.FloatField(default=50)

    name = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=20, default='#FFF68F')

    def __str__(self):
        return f'Furniture {self.id} ({self.x}, {self.y}, {self.width}, {self.height})'