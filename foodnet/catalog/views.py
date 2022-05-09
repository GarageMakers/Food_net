from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Recipe
from .forms import *
# Авторизация
from django.contrib.auth.forms import AuthenticationForm
# Выход
from django.contrib.auth import logout


from django.views.generic import CreateView
# Create your views here.

menu = [{"title": "Главная", "url_name": "index"},
        {"title": "Топ 100", "url_name": "top"},
        {'title': "Вход/Регистрация", "url_name": "register"}]


def base(response):
    recipes = Recipe.objects.all()
    num_visits = response.session.get('num_visits', 0)
    response.session['num_visits'] = num_visits+1
    return render(response, "recipes.html", context={'menu': menu, "recipes": recipes, "num_visits": num_visits})


def login(response):
    return render(response, "login.html")


def top(response):
    return HttpResponse("<h1>top<h1>")


def register(response):
    return render(response, "register.html", context={"title": "Регистрация", "menu": menu})


def addRecipe(response):
    recipe = AddRecipeForm()
    step = AddStepForm()
    return render(response, 'recipe.html', context={"recipeForm": recipe, "title": "Добавить рецепт", "stepForm": step})


# class RegisterUser(CreateView):
#     form_class = RegisterUserForm
#     template_name = "register.html"
#     success_url = reverse_lazy('login')
