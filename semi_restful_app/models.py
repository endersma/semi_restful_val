from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    def validate(self, formData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(formData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(formData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(formData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters"
        if datetime.strptime(formData['release_date'], '%Y-%m-%d') > datetime.now(): 
            errors['release_date'] = 'Release Date should be in the past'
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()