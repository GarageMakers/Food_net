from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory


CompanyFormSet = inlineformset_factory(Recipe, Step, fields='__all__')


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = {"last_name", "first_name", "email", "username"}
