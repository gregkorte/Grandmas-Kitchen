from pyexpat import model
from django.db import models
from grandmas_kitchen.models import Recipe

class Step(models.Model):
    description = models.TextField(max_length=5000)
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)

    def __str__(self):
        return self.description