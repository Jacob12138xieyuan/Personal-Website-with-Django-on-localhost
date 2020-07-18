from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image/')
    summary = models.TextField()
    detail = models.TextField()
    github_link = models.CharField(
        blank=True, max_length=100)
    submission_date = models.DateTimeField(
        help_text='e.g. 2020-07-16 06:35:08')
