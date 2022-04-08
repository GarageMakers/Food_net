from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
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
