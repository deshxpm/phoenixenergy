from django.db import models


class Energy(models.Model):
	time_series = models.DateTimeField()
	voltage 	= models.IntegerField()
	current 	= models.IntegerField()

	def __str__(self):
		return str(self.voltage)