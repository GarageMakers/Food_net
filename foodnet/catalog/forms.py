from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory


RecipeStepFormSet = inlineformset_factory(
    Recipe, Step, extra=1, min_num=1, fields=('text_field', 'photo_path'), can_delete=False)


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ['date', "creator"]


class AddStepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = '__all__'


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = {"last_name", "first_name", "email", "username"}
