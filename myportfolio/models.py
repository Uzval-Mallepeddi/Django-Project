from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class ContactInfo(models.Model):
    firstname = models.CharField(max_length=264)
    lastname = models.CharField(max_length=264)
    email = models.EmailField(blank=False)
    phone = models.PositiveIntegerField(blank=True)
    comments = models.TextField(blank=True)

class NewProject(models.Model):
    project_title = models.CharField(max_length=264, blank=False)
    project_description = models.TextField(blank=False)
    image_location = models.URLField(blank=True)
    github_location = models.URLField(blank=False)
