from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Category, Recipe
from .forms import AddRecipeForm

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить рецепт", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]


# Create your views here.
def index(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'mainapp/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'mainapp/about.html', context=context)


def add_page(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddRecipeForm()

    context = {
        'form': form,
        'menu': menu,
        'title': 'Добавление рецепта'
    }

    return render(request, 'mainapp/add_page.html', context=context)


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_recipe(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)

    context = {
        'recipe': recipe,
        'menu': menu,
        'title': recipe.title,
        'cat_selected': recipe.cat_id,
    }

    return render(request, 'mainapp/recipe.html', context=context)


def show_category(request, cat_slug):
    recipes = Recipe.objects.filter(cat__slug=cat_slug)

    if len(recipes) == 0:
        raise Http404()

    context = {
        'recipes': recipes,
        'menu': menu,
        'title': 'Отображение по категориям',
        'cat_selected': recipes[0].id,
    }

    return render(request, 'mainapp/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
