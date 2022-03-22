from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(response):
    return render(response, "index.html")


def recipe(response):
    return HttpResponse("<h1>recipe<h1>")


def account(response):
    return HttpResponse("<h1>account<h1>")


def enter(response):
    return render(response, "enter.html")
