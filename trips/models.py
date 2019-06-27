from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	photo = models.URLField(blank=True)
	location = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Teacher(models.Model):
	name = models.CharField(max_length=30)
	remark = models.TextField(blank=True)
	
	def __str__(self):
		return self.name

# Create your models here.
