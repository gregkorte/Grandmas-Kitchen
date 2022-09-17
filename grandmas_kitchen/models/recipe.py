from django.db import models
from models import User, Family, FamilyMember, Category, Type

class FamilyMember(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    user = models.ForeignKey(User)
    family = models.ForeignKey(Family)
    family_member = models.ForeignKey(FamilyMember)
    category = models.ForeignKey(Category)
    type = models.ForeignKey(Type)

    def __str__(self):
        return self.name