from django import forms
from .models import *


class AddCatForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sex'].empty_label = 'Не выбран'
        self.fields['breed'].empty_label = 'Не выбрана'

    class Meta:
        model = Cat
        fields = '__all__'


class AddDogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sex'].empty_label = 'Не выбран'
        self.fields['breed'].empty_label = 'Не выбрана'

    class Meta:
        model = Dog
        fields = '__all__'
