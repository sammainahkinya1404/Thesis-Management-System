# theses/forms.py
from django import forms
from .models import *
from users.models import CustomUser



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Thesis
        fields = ['feedback', 'status']
from .models import ThesisProgress

class ProgressForm(forms.ModelForm):
    class Meta:
        model = ThesisProgress
        fields = ['milestone', 'due_date', 'completed']


class ThesisForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(role='teacher'),
        empty_label="Select a Teacher",
        required=True,
        label="Assign Teacher",
    )

    class Meta:
        model = Thesis
        fields = ['title', 'abstract', 'file', 'teacher']
