"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import mainapp.views as m
from django.urls import path


urlpatterns = [
    path('', m.RecipeHome.as_view(), name='home'),
    path('about/', m.about, name='about'),
    path('addpage/', m.AddPage.as_view(), name='add_page'),
    path('contact/', m.contact, name='contact'),
    path('login/', m.LoginUser.as_view(), name='login'),
    path('logout', m.logout_user, name='logout'),
    path('register/', m.RegisterUser.as_view(), name='register'),
    path('recipe/<slug:recipe_slug>/', m.ShowRecipe.as_view(), name='recipe'),
    path('category/<slug:cat_slug>/', m.RecipeCategory.as_view(), name='category'),
]
