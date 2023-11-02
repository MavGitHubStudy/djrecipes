from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category, Recipe
from .forms import AddRecipeForm
from .utils import *


class RecipeHome(DataMixin, ListView):
    model = Recipe
    template_name = 'mainapp/index.html'
    context_object_name = 'recipes'
    # extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


    def get_queryset(self):
        return Recipe.objects.filter(is_published=True)


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'mainapp/about.html', context=context)


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddRecipeForm
    template_name = 'mainapp/add_page.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True  # 403 - доступ запрещён

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


class ShowRecipe(DataMixin, DetailView):
    model = Recipe
    template_name = 'mainapp/recipe.html'
    slug_url_kwarg = 'recipe_slug'
    # pk_url_kwarg = 'pk'
    context_object_name = 'recipe'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['recipe'])
        return dict(list(context.items()) + list(c_def.items()))


class RecipeCategory(DataMixin, ListView):
    model = Recipe
    template_name = 'mainapp/index.html'
    context_object_name = 'recipes'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Категория - ' + str(context['recipes'][0].cat),
            cat_selected=context['recipes'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Recipe.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
