from dataclasses import fields
from django import forms
from .models import Recipe, Step


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class AddStepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = '__all__'
