from django import forms
from .models import Recipe, Step, User, Visitor
from django.contrib.auth.forms import UserCreationForm


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class AddStepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = '__all__'


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = {"last_name", "first_name", "email", "username"}
