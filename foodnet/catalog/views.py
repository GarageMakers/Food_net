
from django.contrib.auth.views import LoginView
from django.http import Http404, HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, UpdateView)
from django.views.generic.detail import SingleObjectMixin

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
        # c_def = self.get_user_context(title="Создание рецепта")
        return dict(list(context.items()))

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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удалить шаг")
        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self) -> str:
        return reverse("recipe", kwargs={'pk': self.object.recept_id.pk})


class DeleteRecipeForm(DataMixin, DeleteView):
    model = Recipe
    template_name = 'deleteRecipe.html'
    success_url = reverse_lazy('recipeList')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = self.get_object()
        c_def = self.get_user_context(title="Удалить рецепт")
        return dict(list(context.items())+list(c_def.items()))

# without ajax


# class RecipeDetail(DetailView, DataMixin):
#     model = Recipe
#     template_name = 'recipe.html'

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Foodnet")
#         context["steps"] = self.get_object().step_set.all()
#         if self.request.user.is_authenticated:
#             context['form'] = CommentForm
#         return dict(list(context.items())+list(c_def.items()))


# class CommentInterestFormView(SingleObjectMixin, FormView):
#     template_name = 'books/author_detail.html'
#     form_class = CommentForm
#     model = Recipe

#     def post(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return HttpResponseForbidden()
#         self.object = self.get_object()
#         form = self.get_form()
#         form.instance.user_id = request.user.visitor
#         form.instance.recipe_id = self.get_object()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse('recipe', kwargs={'pk': self.object.pk})


# class RecipeView(View):
#     def get(self, request, *args, **kwargs):
#         view = RecipeDetail.as_view()
#         return view(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         view = CommentInterestFormView.as_view()
#         return view(request, *args, **kwargs)
# without ajax
# with ajax


class RecipeDetail(DetailView, DataMixin):
    model = Recipe
    template_name = 'recipe.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Foodnet")
        context["steps"] = self.get_object().step_set.all()
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm
            context['grade_form'] = GradeForm
        return dict(list(context.items())+list(c_def.items()))

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     context = self.get_context_data(object=self.object)
    #     return self.render_to_response(context)


class CommentFormView(SingleObjectMixin, FormView):
    template_name = 'recipe.html'
    form_class = CommentForm
    model = Recipe

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        form.instance.user_id = request.user.visitor
        form.instance.recipe_id = self.get_object()
        if form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        """
        Если форма валидна, вернем код 200
        вместе с именем пользователя
        """
        text_field = form.cleaned_data['text_field']
        form.save()
        return JsonResponse({"text_field": text_field}, status=200)

    def form_invalid(self, form):
        """
        Если форма невалидна, возвращаем код 400 с ошибками.
        """
        errors = form.errors.as_json()
        return JsonResponse({"errors": errors}, status=400)

    def get_success_url(self):
        return reverse('recipe', kwargs={'pk': self.object.pk})


class CreateGrade(SingleObjectMixin, FormView):
    template_name = 'recipe.html'
    form_class = GradeForm
    model = Recipe

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        form.instance.user = request.user.visitor
        form.instance.recipe = self.get_object()
        if form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        """
        Если форма валидна, вернем код 200
        вместе с именем пользователя
        """
        grade = form.cleaned_data['grade']
        form.save()
        return JsonResponse({"grade": grade}, status=200)

    def form_invalid(self, form):
        """
        Если форма невалидна, возвращаем код 400 с ошибками.
        """
        errors = form.errors.as_json()
        return JsonResponse({"errors": errors}, status=400)

    def get_success_url(self):
        return reverse('recipe', kwargs={'pk': self.object.pk})
