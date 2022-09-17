from django.db import models
from grandmas_kitchen.models import FamilyMember, Relation
from django.contrib.auth.models import User

class FamilyMemberRelation(models.Model):
    family_member = models.ManyToManyField(FamilyMember)
    relation = models.ManyToManyField(Relation)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self