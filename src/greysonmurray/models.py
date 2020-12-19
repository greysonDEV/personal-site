"""
src/greysonmurray/models.py
"""

from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=200)

	def __str__(self):
		return f"{self.title}: {self.description}"
