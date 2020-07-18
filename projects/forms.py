from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image', 'summary', 'detail', 'submission_date']
        field_classes = {
            'image': forms.ImageField,
            'submission_date': forms.DateTimeField
        }
