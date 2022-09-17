from django.db import models
from grandmas_kitchen.models import Recipe, Ingredient

class RecipeIngredient(models.Model):
    recipe = models.ManyToManyField(Recipe)
    ingredient = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self