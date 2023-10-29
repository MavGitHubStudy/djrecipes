from django.contrib import admin
from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
