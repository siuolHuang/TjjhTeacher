from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Article(models.Model):
	content = models.TextField(blank=True)
	title = models.CharField(max_length=50)
	num1 = models.CharField(max_length=9)
	num2 = models.CharField(max_length=9)
	category = models.ForeignKey('Category',blank=True,null=True)

	def __str__(self):
		return self.title

# Create your models here.
