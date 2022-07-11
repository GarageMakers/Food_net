
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from .forms import *
from .models import Recipe
from .utils import DataMixin, FormsetMixin


def top(response):
    return HttpResponse("<h1>silence<h1>")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "register.html"
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items())+list(c_def.items()))

    # def get_success_url(self) -> str:
    #     return reverse_lazy('login')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self) -> str:
        return reverse_lazy('index')


class IndexView(DataMixin, ListView):
    model = Recipe
    template_name = "index.html"
    context_object_name = "recipes"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items())+list(c_def.items()))


class RecipeDetail(DetailView, DataMixin):
    model = Recipe
    template_name = 'recipe.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Foodnet")
        context["steps"] = self.get_object().step_set.all()
        return dict(list(context.items())+list(c_def.items()))


class VisitorRecipesView(DataMixin, ListView):
    model = Recipe
    template_name = "recipeList.html"
    context_object_name = "visitor_recipes"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Мои рецепты")
        return dict(list(context.items())+list(c_def.items()))

    def get(self, request, *args, **kwargs):
        self.object_list = Recipe.objects.filter(
            creator=request.user.visitor)
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(('Empty list and “%(class_name)s.allow_empty” is False.') % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        return self.render_to_response(context)


class AddRecipe(FormsetMixin, CreateView, DataMixin):
    model = Recipe
    template_name = 'addRecipe.html'
    form_class = AddRecipeForm
    formset_class = RecipeStepFormSet

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Создание рецепта")
        return dict(list(context.items())+list(c_def.items()))

    def form_valid(self, form, formset):
        form.instance.creator = self.request.user.visitor
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return redirect(self.object.get_absolute_url())


class UpdateRecipeForm(FormsetMixin, DataMixin, UpdateView):
    model = Recipe
    template_name = 'updateRecipe.html'
    form_class = AddRecipeForm
    formset_class = RecipeStepFormSet

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактирование")
        return dict(list(context.items())+list(c_def.items()))


class UpdateStepForm(DataMixin, UpdateView):
    model = Step
    template_name = 'updateStep.html'
    template_name_suffix = '_update_form'
    form_class = AddStepForm
    success_url = reverse_lazy('recipeList')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактирование")
        return dict(list(context.items())+list(c_def.items()))


class DeleteStepForm(DataMixin, DeleteView):
    model = Step
    template_name = 'deleteStep.html'
    success_url = reverse_lazy('recipe')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить шаг")
        return dict(list(context.items())+list(c_def.items()))


class DeleteRecipeForm(DataMixin, DeleteView):
    model = Recipe
    template_name = 'deleteRecipe.html'
    success_url = reverse_lazy('recipeList')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = self.get_object()
        c_def = self.get_user_context(title="Удалить рецепт")
        return dict(list(context.items())+list(c_def.items()))
