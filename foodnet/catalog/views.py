from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
# Create your views here.


def index(response):
    num_recipe = Recipe.objects.all().count()
    return render(response, "index.html", context={'num_recipe': num_recipe})


def recipe(response):
    return HttpResponse("<h1>recipe<h1>")


def account(response):
    return HttpResponse("<h1>account<h1>")


def enter(response):
    return render(response, "enter.html")
