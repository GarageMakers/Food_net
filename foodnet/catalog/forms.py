from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.forms import inlineformset_factory


RecipeStepFormSet = inlineformset_factory(
    Recipe, Step,  fields=('text_field', 'photo_path'), extra=1, can_delete=False)


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


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
