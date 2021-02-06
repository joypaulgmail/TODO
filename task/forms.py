from .models import task
from django import forms

class Taskforms(forms.ModelForm):
    class Meta:

        model=task
        fields="__all__"