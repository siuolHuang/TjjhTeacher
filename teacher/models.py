from django.db import models

class teacher(models.Model):
	name=models.CharField(max_length=10)
	birth=models.DateField(null=False, blank=False)
	
	def __str__(self):
		return self.name

class Position(models.Model):
	title = models.CharField(max_length=30)
	point = models.IntegerField(default=0)
	def __str__(self):
		return self.title


# Create your models here.
