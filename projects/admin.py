from django.contrib import admin
from .models import Project
# Register your models here.


@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'summary', 'submission_date']
