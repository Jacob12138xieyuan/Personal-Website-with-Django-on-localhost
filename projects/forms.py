from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image', 'summary', 'detail', 'submission_date']
