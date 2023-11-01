from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL")
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Recipe(models.Model):
    title = models.CharField(max_length=255, db_index=True,
                             verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Описание")
    cooking_steps = models.TextField(blank=True,
                                     verbose_name="Шаги пригот.")
    cooking_time = models.IntegerField(
        null=True, blank=True, verbose_name="Время приготовления в минутах")
    image = models.ImageField(upload_to="images/%Y/%m/%d/",
                              default="images/None/no-img.jpg",
                              verbose_name="Изображение")
    author = models.CharField(max_length=255, verbose_name="Автор")
    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True,
                                       verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,
                            verbose_name="Категории")

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe', kwargs={'recipe_slug': self.slug})
