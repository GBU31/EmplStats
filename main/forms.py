from django import forms
from .models import *


class InterviewForm(forms.ModelForm):
    class Meta:
        model = InterviewModel
        fields = '__all__'
