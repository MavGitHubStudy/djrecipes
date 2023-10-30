from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import Category, Recipe

menu = ["О сайте", "Добавить рецепт", "Обратная связь", "Войти"]


# Create your views here.
def index(request):
    posts = Recipe.objects.all()
    categories = Category.objects.all()
    return render(request, 'mainapp/index.html',
                  {'categories': categories, 'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return HttpResponse("About djrecipes")