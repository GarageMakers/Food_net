from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from .utils import DataMixin
from .models import Recipe
from .forms import *
# Авторизация
from django.contrib.auth.forms import AuthenticationForm
# Выход
from django.contrib.auth.views import LoginView


from django.views.generic import CreateView, ListView
# Create your views here.

menu = [{"title": "Главная", "url_name": "index"},
        {"title": "Топ 100", "url_name": "top"},
        {'title': "Вход/Регистрация", "url_name": "register"}]


def base(response):
    recipes = Recipe.objects.all()
    num_visits = response.session.get('num_visits', 0)
    response.session['num_visits'] = num_visits+1
    return render(response, "recipes.html", context={'menu': menu, "recipes": recipes, "num_visits": num_visits})


def top(response):
    return HttpResponse("<h1>top<h1>")


def silence(response):
    return HttpResponse("<h1>silence<h1>")


class IndexView(DataMixin, ListView):
    model = Recipe
    template_name = "index.html"
    context_object_name = "recipes"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items())+list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "register.html"
    success_url = reverse_lazy('accounts')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items())+list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self) -> str:
        return reverse_lazy('index')


class AddRecipe(DataMixin, CreateView):
    model = Recipe
    form_class = AddRecipeForm
    template_name = "addRecipe.html"
    # success_url = reverse_lazy('accounts')

    def get(self, request, object=None, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        recipe_form = AddRecipe
        return self.render_to_response(self.get_context_data(form=form, recipe_form=recipe_form))

    def post(self, request, object=None, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        recipe_form = AddRecipe(self.request.POST)
        if (form.is_valid() and recipe_form.is_valid()):
            return super(AddRecipe, self).form_valid(form, recipe_form)
        else:
            return self.form_invalid(form, recipe_form)

    def form_valid(self, form, recipe_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        recipe_form.instance = self.object
        recipe_form.instance.user = self.request.user
        recipe_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, recipe_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  recipe_form=recipe_form))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить рецепт")
        return dict(list(context.items())+list(c_def.items()))
