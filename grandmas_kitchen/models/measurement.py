from django.db import models

class Measurement(models.Model):
	amount = models.CharField(max_length=100)

	def __str__(self):
		return self.amount