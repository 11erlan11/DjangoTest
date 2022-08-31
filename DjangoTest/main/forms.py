from .models import Taski
from django.forms import ModelForm, TextInput, Textarea

class TaskiForm(ModelForm):
    class Meta:
        model = Taski
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }