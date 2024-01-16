from django import forms
from django.forms import ModelForm
from .models import Document

class EditDocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ("title", "contents")
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '✨ New markdown document'}),
            'contents': forms.Textarea(
                attrs={'placeholder': 'Hi there! This is **markdown** 👋'}),
        }