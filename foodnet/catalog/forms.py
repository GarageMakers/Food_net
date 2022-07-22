from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import inlineformset_factory

from .models import *

RecipeStepFormSet = inlineformset_factory(
    Recipe, Step, fields=("order", "text_field", "photo_path"), extra=1, can_delete=False,
    labels={'order': "Номер шага",
            "text_field": "Текст шага", "photo_path": "Фото"},
    widgets={'order': forms.HiddenInput(),
             "text_field": forms.Textarea(attrs={"class": "form-control"}),
             "photo_path": forms.FileInput(attrs={"class": "form-control"})})


class AddRecipeForm(forms.ModelForm):
    name = forms.CharField(label="Имя рецепта", widget=forms.TextInput(
        attrs={'class': "form-control"}))

    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ['date', "creator"]


class AddStepForm(forms.ModelForm):
    text_field = forms.CharField(label='Текст', widget=forms.Textarea(
        attrs={'class': "form-control"}))

    class Meta:
        model = Step
        fields = '__all__'
        exclude = ['order', "recept_id"]


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


class CommentForm(forms.ModelForm):
    text_field = forms.CharField(label='Комментарий', widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['user_id', 'recipe_id']
