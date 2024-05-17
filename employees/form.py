from django import forms
from .models import employees

class employeeform(forms.ModelForm):
    class Meta:
        model = employees
        fields = ['name', 'position', 'avata', 'file_image']