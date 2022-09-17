from django.db import models
from models import Recipe, Ingredient

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)

    def __str__(self):
        return self