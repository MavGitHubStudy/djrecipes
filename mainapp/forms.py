from django import forms
from .models import *


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=255, label="Заголовок",
                            widget=forms.TextInput(
                                attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label="URL")
    content = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 60, 'rows': 10}), label="Описание")
    cooking_steps = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        label="Шаги пригот.")
    cooking_time = forms.IntegerField(label="Время в мин")
    is_published = forms.BooleanField(label="Публикация", required=False,
                                      initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 label="Категория",
                                 empty_label="Категория не выбрана")
