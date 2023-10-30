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
    path('', m.index, name='home'),
    path('about/', m.about, name='about'),
    path('addpage/', m.add_page, name='add_page'),
    path('contact/', m.contact, name='contact'),
    path('login/', m.login, name='login'),
    path('recipe/<int:recipe_id>/', m.show_recipe, name='recipe'),
]
