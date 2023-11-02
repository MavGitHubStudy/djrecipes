from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView

from .models import Category, Recipe
from .forms import AddRecipeForm

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить рецепт", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]


class RecipeHome(ListView):
    model = Recipe
    template_name = 'mainapp/index.html'
    context_object_name = 'recipes'
    # extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Recipe.objects.filter(is_published=True)

# Create your views here.
# def index(request):
#     recipes = Recipe.objects.all()
#
#     context = {
#         'recipes': recipes,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'mainapp/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'mainapp/about.html', context=context)


class AddPage(CreateView):
    form_class = AddRecipeForm
    template_name = 'mainapp/add_page.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление рецепта'
        return context

# def add_page(request):
#     if request.method == 'POST':
#         form = AddRecipeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddRecipeForm()
#
#     context = {
#         'form': form,
#         'menu': menu,
#         'title': 'Добавление рецепта'
#     }
#
#     return render(request, 'mainapp/add_page.html', context=context)


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


class ShowRecipe(DetailView):
    model = Recipe
    template_name = 'mainapp/recipe.html'
    slug_url_kwarg = 'recipe_slug'
    # pk_url_kwarg = 'pk'
    context_object_name = 'recipe'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['recipe']
        return context


# def show_recipe(request, recipe_slug):
#     recipe = get_object_or_404(Recipe, slug=recipe_slug)
#
#     context = {
#         'recipe': recipe,
#         'menu': menu,
#         'title': recipe.title,
#         'cat_selected': recipe.cat_id,
#     }
#
#     return render(request, 'mainapp/recipe.html', context=context)


class RecipeCategory(ListView):
    model = Recipe
    template_name = 'mainapp/index.html'
    context_object_name = 'recipes'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['recipes'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['recipes'][0].cat_id
        return context

    def get_queryset(self):
        return Recipe.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

# def show_category(request, cat_slug):
#     recipes = Recipe.objects.filter(cat__slug=cat_slug)
#
#     if len(recipes) == 0:
#         raise Http404()
#
#     context = {
#         'recipes': recipes,
#         'menu': menu,
#         'title': 'Отображение по категориям',
#         'cat_selected': recipes[0].id,
#     }
#
#     return render(request, 'mainapp/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
