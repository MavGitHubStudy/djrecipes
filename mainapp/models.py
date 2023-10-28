from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
