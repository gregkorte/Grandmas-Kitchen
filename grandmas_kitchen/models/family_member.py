from tkinter import CASCADE
from django.db import models
from grandmas_kitchen.models import Family
from django.db.models.functions import Concat

class FamilyMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = Concat(first_name,' ', last_name)
    family = models.ForeignKey(Family,on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name