from django import forms
from .models import *

class LetterCreateForm(forms.ModelForm):
    class Meta:
        model = letter
        fields = ('name','description','path','image')
        widgets = {
            'name': forms.TextInput(attrs={'class':"input-1", "placeholder":"Введите оглавление "}),
            'description':forms.TextInput(attrs={'class':"input-1", "placeholder":"Введите описание "}),
            'path': forms.FileInput(),
            'image': forms.ClearableFileInput(),

        }

class LetterSendForm(forms.Form):
    title = forms.CharField(max_length=63, widget=forms.TextInput(attrs={'class':"input-1", "placeholder":"Введите оглавление "}))
    description = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':"input-1", "placeholder":"Введите текст "}))
    mail = forms.EmailField(widget=forms.EmailInput(attrs={'class':"input-1", "placeholder":"Введите почту получателя "}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 
                                                        'class': 'input-1'}))