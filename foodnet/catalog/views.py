from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(response):
    return HttpResponse("<h1>index<h1>")


def recipe(response):
    return HttpResponse("<h1>recipe<h1>")


def account(response):
    return HttpResponse("<h1>account<h1>")
