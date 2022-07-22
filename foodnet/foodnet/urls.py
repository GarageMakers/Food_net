"""foodnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from catalog import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# from django.contrib.auth.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('recipeList/recipe/<int:pk>',
         views.RecipeDetail.as_view(), name='own_recipe'),
    path('recipe/<int:pk>', views.RecipeDetail.as_view(), name='recipe'),
    path('accounts/login/', views.LoginUser.as_view(), name='login'),
    path('top/', views.top, name="top"),
    path('addRecipe/', views.AddRecipe.as_view(), name="addRecipe"),
    path('accounts/register/', views.RegisterUser.as_view(), name='register'),
    path('recipeList/', views.VisitorRecipesView.as_view(), name="recipeList"),
    path('recipeList/updateStep/<int:pk>',
         views.UpdateStepForm.as_view(), name='updateStep'),
    path('recipeList/deleteStep/<int:pk>',
         views.DeleteStepForm.as_view(), name='deleteStep'),
    path('recipeList/deleteRecipe/<int:pk>',
         views.DeleteRecipeForm.as_view(), name='deleteRecipe'),
    path('comment-form/<int:pk>',
         views.CommentFormView.as_view(), name='comment_form'),


]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
