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
    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Адрес электронной почты', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = {"last_name", "first_name", "email", "username"}
        field_order = ['username', 'email', 'password1',
                       'password2', 'first_name', 'last_name']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
