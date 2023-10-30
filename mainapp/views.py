from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import Category, Recipe

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить рецепт", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]


# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'recipes': recipes,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'mainapp/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'mainapp/about.html', context=context)


def add_page(request):
    return HttpResponse("Добавление рецепта")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_recipe(request, recipe_id):
    return HttpResponse(f"Отображение рецепта с id = {recipe_id}")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
