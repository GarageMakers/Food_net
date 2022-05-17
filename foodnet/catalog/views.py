from urllib import request
from winreg import REG_WHOLE_HIVE_VOLATILE
from django.forms import formset_factory
from django.shortcuts import redirect, render
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


class FormsetMixin():
    object = None

    def get(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def get_formset_class(self):
        return self.formset_class

    def get_formset(self, formset_class):
        return formset_class(**self.get_formset_kwargs())

    def get_formset_kwargs(self):
        kwargs = {
            'instance': self.object
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return redirect(self.object.get_absolute_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class AddRecipe(FormsetMixin, DataMixin, CreateView):
    model = Recipe
    template_name = 'addRecipe.html'
    form_class = AddRecipeForm
    formset_class = RecipeStepFormSet

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Создание рецепта")
        return dict(list(context.items())+list(c_def.items()))
