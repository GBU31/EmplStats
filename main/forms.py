from django import forms
from .models import *


class InterviewForm(forms.ModelForm):
    class Meta:
        model = InterviewModel
        fields = "__all__"
        widgets = {
            'user': forms.TextInput(attrs={'style':'display: none;'}),}
        
        labels = {
            'user': '',}
