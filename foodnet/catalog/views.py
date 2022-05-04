from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from .forms import *
# Create your views here.

menu = [{"title": "Главная", "url_name": "index"},
        {"title": "Топ 100", "url_name": "top"},
        {'title': "Вход/Регистрация", "url_name": "enter"}]


def base(response):
    recipes = Recipe.objects.all()
    return render(response, "recipes.html", context={'menu': menu, "recipes": recipes})


def account(response):
    return HttpResponse("<h1>account<h1>")


def enter(response):
    return render(response, "enter.html")


def top(response):
    return HttpResponse("<h1>top<h1>")


def register(response):
    return render(response, "register.html", context={"title": "Регистрация", "menu": menu})


def addRecipe(response):
    recipe = AddRecipeForm()
    step = AddStepForm()
    return render(response, 'recipe.html', context={"recipeForm": recipe, "title": "Добавить рецепт", "stepForm": step})
