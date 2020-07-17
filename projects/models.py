from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image/')
    summary = models.TextField()
    detail = models.TextField()
    submission_date = models.DateTimeField()
