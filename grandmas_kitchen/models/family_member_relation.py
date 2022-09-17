from django.db import models
from models import User, FamilyMember, Relation

class FamilyMemberRelation(models.Model):
    family_member = models.ForeignKey(FamilyMember)
    relation = models.ForeignKey(Relation)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self