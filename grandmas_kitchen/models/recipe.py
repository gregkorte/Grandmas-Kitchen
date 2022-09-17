from django.db import models
from grandmas_kitchen.models import Family, FamilyMember, Category, Type
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    family = models.ForeignKey(Family,on_delete=models.CASCADE)
    family_member = models.ForeignKey(FamilyMember,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    type = models.ForeignKey(Type,on_delete=models.CASCADE)

    def __str__(self):
        return self.name