from django import forms


class EditForm(forms.Form):
    name = forms.CharField(label='name', max_length=30)
    image = forms.ImageField()
    summary = forms.CharField(label='summary', max_length=30)
    detail = forms.CharField(label='detail', max_length=30)
    submission_date = forms.DateTimeField()
