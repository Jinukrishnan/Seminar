from django.db import models


class Phone(models.Model):
    name=models.CharField(max_length=250)
    phone=models.IntegerField()
    
    def __str__(self):
        return self.name