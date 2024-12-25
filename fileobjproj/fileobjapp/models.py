from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50, unique=True)
    filepath = models.CharField(max_length=100,default="")

    def __str__(self):
        return f"name: {self.name}, filepath:{self.filepath}"
    