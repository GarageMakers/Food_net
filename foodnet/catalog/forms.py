from dataclasses import fields
from django import forms
from .models import Recipe


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
