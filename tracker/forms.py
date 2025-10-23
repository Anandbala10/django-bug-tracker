# tracker/forms.py
from django import forms
from .models import Bug

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        # Add 'priority' to this list
        fields = ['title', 'description', 'status', 'priority']